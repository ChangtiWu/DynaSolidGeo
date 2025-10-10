import json
import argparse
import os
from tqdm import tqdm

from geo_evaluate import compute_score

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', "--response_file", type=str, required=True, help="Path to the response JSONL file.")
    parser.add_argument('-o', "--output_file", type=str, default=None, help="Path to the output JSONL file.")
    return parser.parse_args()

def evaluate_solutions(response_file, output_file=None):
    """
    Evaluate solutions by comparing response with ground truth solution
    
    Args:
        response_file: Path to the JSONL file containing model responses
        output_file: Path to the output JSONL file with evaluation results
    """
    if not os.path.exists(response_file):
        raise FileNotFoundError(f"Response file {response_file} does not exist.")
    
    # Set default output file path if not provided
    if output_file is None:
        input_dir = os.path.dirname(response_file)
        output_file = os.path.join(input_dir, "response_dec.jsonl")
    
    # Ensure output directory exists
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Statistics variables
    total_items = 0
    correct_items = 0
    error_items = 0
    
    print(f"Evaluating file: {response_file}")
    print(f"Output file: {output_file}")
    print("-" * 70)
    
    # Read all data and process
    with open(response_file, "r", encoding="utf-8") as fin:
        lines = fin.readlines()
    
    results = []
    
    for line in tqdm(lines, desc="Evaluating"):
        if not line.strip():
            continue
            
        try:
            item = json.loads(line.strip())
            
            # Get required fields
            item_id = item.get("id", "UNKNOWN")
            model_response = item.get("response", "")
            ground_truth = item.get("solution", "")

            # if model_response contains <|begin_of_box|> and <|end_of_box|>, extract the content between them as model_response
            if "<|begin_of_box|>" in model_response and "<|end_of_box|>" in model_response: 
                import re
                match = re.search(r"<\|begin_of_box\|>(.*?)<\|end_of_box\|>", model_response, re.DOTALL)
                if match:
                    model_response = "\\boxed{"+match.group(1).strip()+"}"
            
            if not model_response or not ground_truth:
                print(f"Warning: Missing response or solution for item {item_id}")
                item["solution_dec"] = 0
                error_items += 1
            else:
                # Compute score
                try:
                    score, extracted = compute_score(model_response, ground_truth)
                    item["solution_dec"] = 1 if score == 1.0 else 0
                    
                    if score == 1.0:
                        correct_items += 1
                        
                except Exception as e:
                    print(f"Error computing score for item {item_id}: {e}")
                    item["solution_dec"] = 0
                    error_items += 1
            
            total_items += 1
            results.append(item)
            
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON line: {e}")
            error_items += 1
            continue
    
    # Write results to output file (create new or overwrite existing)
    with open(output_file, "w", encoding="utf-8") as fout:
        for item in results:
            fout.write(json.dumps(item, ensure_ascii=False) + "\n")
    
    # Calculate and print statistics
    accuracy = correct_items / total_items if total_items > 0 else 0.0
    
    print("\n" + "=" * 70)
    print("Evaluation Results:")
    print("=" * 70)
    print(f"Total items: {total_items}")
    print(f"Correct answers: {correct_items} ({accuracy*100:.2f}%)")
    print(f"Evaluation errors: {error_items}")
    print(f"Results saved to: {output_file}")

def main():
    args = parse_args()
    evaluate_solutions(args.response_file, args.output_file)

if __name__ == "__main__":
    main()
