import os
import json
import argparse
import asyncio
from tqdm import tqdm

try:
    from openai import AsyncOpenAI
    BASE_URL = os.getenv('BASE_URL', 'https://api.openai.com/v1')
    API_KEY = os.getenv('API_KEY', 'DONT_FINE_OPENAI_KEY')
    MODEL_NAME = os.getenv('MODEL_NAME', 'gpt-4o')
    if API_KEY == 'DONT_FINE_OPENAI_KEY':
        raise ValueError("API key for OpenAI is not set. Please set the API_KEY environment variable.")
    client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)
except ImportError:
    print("To use openai, please install it first by running `pip install openai`.")

EVALUATION_PROMPT = r'''
You are a professional judge of geometric reasoning.
Score whether the TARGET reasoning response CAUSALLY SUPPORTS its final answer, under the rubric below.
Judge only the TARGET; ignore stylistic similarity to the reference.

== REFERENCE ==
Problem:
{reference_problem}

Reference reasoning process:
{reference_thinking}

== RESPONSE TO EVALUATE ==
{response}

== EVALUATION CRITERIA (set upper bounds if violated) ==
S1 Logical Alignment (required):
   The response presents a coherent derivation whose reasoning leads to the response's stated result with matching variables/units and no conclusion jump.
   If violated, cap score at 0.50.

S2 No Extraneous Information (required):
   The response does not introduce unseen quantities or facts as essential premises (standard geometric axioms/theorems are allowed).
   If violated, cap score at 0.50.

S3 Use of Key Dependencies (strong constraint):
   The response explicitly uses key geometric relations from the problem (parallel/similar/perpendicular/collinear/ratio/angle, etc.), rather than skipping conditions and merely reporting a result.
   If violated, cap score at 0.75.

== SCORE BANDS (choose exactly one, respecting any caps) ==
1.00  Full Causality: satisfies S1–S3; contains a complete, traceable derivation from given conditions to the stated result; variables/units consistent; no contradictions.
0.75  Near Causality: satisfies S1–S3; overall sound with one minor lapse (e.g., trivial arithmetic/notation slip or an implicit standard step) that is easily fixed.
0.50  Partial Support: at least satisfies S1; captures some key relations but is insufficient to reach the stated result (a conclusion jump/missing closure), or contains minor non-essential extraneous reference.
0.25  Marginally Related: includes a few correct but weakly connected facts; little causal progress toward the stated result.
0.00  Not Supportive/Incorrect: contradictions, circular reasoning, wrong core dependency, or clear mismatch between reasoning and stated result.

== CONSTRAINTS ==
- Do NOT use numeric content or steps from the reference to score the response.
- If uncertain, choose the lower band.
- Output must be EXACTLY one of: 0, 0.25, 0.5, 0.75, 1.00 — print the number only, with no other text or spaces.

== Output Format ==
Output ONE number only: 0, 0.25, 0.5, 0.75, or 1.00.
'''.strip()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', "--response_dec_file", type=str, required=True, help="Path to the response_dec JSONL file.")
    parser.add_argument('-m', "--model_name", type=str, default=None, help="The model name to use for generation.")
    parser.add_argument("--max_concurrent", type=int, default=5, help="Maximum number of concurrent requests.")
    return parser.parse_args()

def load_thinking_data():
    """Load the thinking data from dynasolidgeo_thinking.json in the same directory"""
    thinking_data = {}
    script_dir = os.path.dirname(os.path.abspath(__file__))
    thinking_file = os.path.join(script_dir, "dynasolidgeo_thinking.json")
    
    if os.path.exists(thinking_file):
        try:
            with open(thinking_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    thinking_data[item.get("id")] = {
                        "en_problem": item.get("en_problem", ""),
                        "en_think": item.get("en_think", "")
                    }
        except Exception as e:
            print(f"Warning: Error reading thinking file: {e}")
    else:
        print(f"Warning: Thinking file {thinking_file} does not exist.")
    
    return thinking_data

def load_completed_ids(response_dec_file):
    """Load the list of items that already have process_dec scores (excluding -1)"""
    completed_ids = set()
    if os.path.exists(response_dec_file):
        try:
            with open(response_dec_file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        data = json.loads(line)
                        # Only consider items with valid process_dec scores (not -1)
                        if "process_dec" in data and data["process_dec"] != -1:
                            completed_ids.add(data.get("id", ""))
        except Exception as e:
            print(f"Warning: Error reading existing file: {e}")
    return completed_ids

async def evaluate_single_response(item, model_name, semaphore, thinking_data):
    """Async function to evaluate a single response's reasoning process"""
    async with semaphore:
        try:
            item_id = item.get("id", "UNKNOWN")
            response = item.get("response", "")
            
            if not response:
                print(f"Warning: Empty response for item {item_id}")
                return item_id, 0.0
            
            # Get thinking data for this item
            thinking_info = thinking_data.get(item_id, {})
            reference_problem = thinking_info.get("en_problem", "")
            reference_thinking = thinking_info.get("en_think", "")
            
            if not reference_problem or not reference_thinking:
                print(f"Warning: Missing problem or reference thinking for item {item_id}")
                return item_id, 0.0
            
            evaluation_prompt = EVALUATION_PROMPT.format(
                reference_problem=reference_problem,
                reference_thinking=reference_thinking,
                response=response
            )
            
            completion = await client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "https://github.com/ChangtiWu/DynaSolidGeo",
                    "X-Title": "DynaSolidGeo Process Evaluation",
                },
                extra_body={},
                model=model_name,
                messages=[
                    {
                        "role": "user",
                        "content": evaluation_prompt
                    }
                ],
                temperature=0.0
            )
            
            evaluation_result = completion.choices[0].message.content.strip()
            
            # Extract numerical score from the response
            try:
                # Try to find the last number between 0 and 1
                import re
                matches = list(re.finditer(r'([0-1](?:\.\d+)?)', evaluation_result))
                if matches:
                    last_match = matches[-1]
                    score = float(last_match.group(1))
                    score = max(0.0, min(1.0, score))  # Clamp to [0, 1]
                else:
                    print(f"Warning: Could not extract score from evaluation result for item {item_id}: {evaluation_result}")
                    score = 0.0
            except (ValueError, AttributeError):
                print(f"Warning: Invalid score format for item {item_id}: {evaluation_result}")
                score = 0.0
            
            return item_id, score
            
        except Exception as e:
            print(f"Error evaluating item {item.get('id', 'UNKNOWN')}: {e}")
            return item.get("id", "UNKNOWN"), -1

async def main():
    args = parse_args()
    response_dec_file = args.response_dec_file
    model_name = args.model_name if args.model_name else MODEL_NAME
    max_concurrent = args.max_concurrent
    
    if not os.path.exists(response_dec_file):
        raise FileNotFoundError(f"Response file {response_dec_file} does not exist.")
    
    # Load thinking data
    thinking_data = load_thinking_data()
    print(f"Loaded thinking data for {len(thinking_data)} items.")
    
    # Load completed IDs
    completed_ids = load_completed_ids(response_dec_file)
    print(f"Found {len(completed_ids)} items already evaluated.")
    
    # Read all data
    all_items = []
    items_to_evaluate = []
    
    with open(response_dec_file, "r", encoding="utf-8") as fin:
        for line in fin:
            if line.strip():
                item = json.loads(line)
                all_items.append(item)
                # Only evaluate items that don't have valid process_dec yet (including -1)
                if ("process_dec" not in item or item.get("process_dec") == -1) and item.get("id") not in completed_ids:
                    # If solution_dec is 0, directly set process_dec to 0
                    if item.get("solution_dec", 1) == 0:
                        item["process_dec"] = 0.0
                    else:
                        items_to_evaluate.append(item)
    
    print(f"Total items: {len(all_items)}")
    print(f"Items to evaluate: {len(items_to_evaluate)}")
    
    if not items_to_evaluate:
        print("No new items to evaluate.")
        # Still need to write back the file in case we set some process_dec to 0
        with open(response_dec_file, "w", encoding="utf-8") as fout:
            for item in all_items:
                fout.write(json.dumps(item, ensure_ascii=False) + "\n")
        return
    
    # Create semaphore to limit concurrency
    semaphore = asyncio.Semaphore(max_concurrent)
    
    # Create async tasks
    tasks = [evaluate_single_response(item, model_name, semaphore, thinking_data) for item in items_to_evaluate]
    
    # Collect evaluation results
    evaluation_results = {}
    
    with tqdm(total=len(tasks), desc="Evaluating processes") as pbar:
        for coro in asyncio.as_completed(tasks):
            item_id, score = await coro
            evaluation_results[item_id] = score
            pbar.update(1)
    
    # Update all items with evaluation results
    updated_items = []
    for item in all_items:
        item_id = item.get("id")
        if item_id in evaluation_results:
            item["process_dec"] = evaluation_results[item_id]
        updated_items.append(item)
    
    # Write updated data back to file
    with open(response_dec_file, "w", encoding="utf-8") as fout:
        for item in updated_items:
            fout.write(json.dumps(item, ensure_ascii=False) + "\n")
    
    # Print statistics
    total_evaluated = len(evaluation_results)
    if total_evaluated > 0:
        # Filter out -1 scores for statistics
        valid_scores = [score for score in evaluation_results.values() if score != -1]
        error_count = sum(1 for score in evaluation_results.values() if score == -1)
        
        if valid_scores:
            avg_score = sum(valid_scores) / len(valid_scores)
            high_quality = sum(1 for score in valid_scores if score >= 0.75)
            
            print("\n" + "=" * 70)
            print("Process Evaluation Results:")
            print("=" * 70)
            print(f"Items evaluated: {total_evaluated}")
            print(f"Valid evaluations: {len(valid_scores)}")
            print(f"Evaluation errors: {error_count}")
            print(f"Average process score: {avg_score:.3f}")
            print(f"Qualified processes (≥0.75): {high_quality} ({high_quality/len(valid_scores)*100:.1f}%)")
            print(f"Results saved to: {response_dec_file}")
        else:
            print("\n" + "=" * 70)
            print("Process Evaluation Results:")
            print("=" * 70)
            print(f"Items evaluated: {total_evaluated}")
            print(f"All evaluations failed with errors")
            print(f"Results saved to: {response_dec_file}")

if __name__ == "__main__":
    asyncio.run(main())
