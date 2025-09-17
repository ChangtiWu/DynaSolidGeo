import json
import argparse
import os
import tempfile
import shutil
from tqdm import tqdm

from evalute_util import compute_score

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--response_file", type=str, required=True, help="Path to the response JSONL file.")
    return parser.parse_args()

def evaluate_responses_inplace(response_file):
    """
    Evaluate responses in-place, compute scores and add to the original file
    
    Args:
        response_file: Path to the JSONL file containing model responses
    """
    if not os.path.exists(response_file):
        raise FileNotFoundError(f"Response file {response_file} does not exist.")
    
    # Statistics variables
    total_items = 0
    correct_items = 0
    error_items = 0
    scores = []
    tokens = []  # Token statistics
    updated_items = []
    
    print(f"Evaluating file: {response_file}")
    print("-" * 60)
    
    # Read all data and process
    with open(response_file, "r", encoding="utf-8") as fin:
        lines = fin.readlines()
    
    for line in tqdm(lines, desc="Evaluating"):
        if not line.strip():
            updated_items.append(line)
            continue
            
        try:
            item = json.loads(line.strip())
            
            # Get required fields
            item_id = item.get("id", "UNKNOWN")
            model_response = item.get("response", "")
            ground_truth = item.get("solution", "")
            output_token = item.get("output_token", "N/A")
            
            # Collect token statistics (skip N/A)
            if output_token != "N/A" and output_token is not None:
                try:
                    token_count = int(output_token) if isinstance(output_token, str) else output_token
                    tokens.append(token_count)
                except (ValueError, TypeError):
                    pass  # Skip tokens that cannot be converted to numbers
            
            # Check if already scored
            if "expected_score" in item:
                scores.append(item["expected_score"])
                if item["expected_score"] == 1.0:
                    correct_items += 1
                updated_items.append(json.dumps(item, ensure_ascii=False) + "\n")
                total_items += 1
                continue
            
            if not model_response or not ground_truth:
                print(f"Warning: Missing response or solution for item {item_id}")
                item["expected_score"] = 0.0
                item["extracted_answer"] = ""
                error_items += 1
            else:
                # Compute score
                try:
                    score, extracted = compute_score(model_response, ground_truth)
                    item["expected_score"] = score
                    item["extracted_answer"] = extracted
                    
                    scores.append(score)
                    if score == 1.0:
                        correct_items += 1
                        
                except Exception as e:
                    print(f"Error computing score for item {item_id}: {e}")
                    item["expected_score"] = 0.0
                    item["extracted_answer"] = ""
                    error_items += 1
            
            total_items += 1
            updated_items.append(json.dumps(item, ensure_ascii=False) + "\n")
            
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON line: {e}")
            error_items += 1
            updated_items.append(line)  # Keep original line
            continue
    
    # Safely update original file using temporary file
    temp_file = response_file + ".tmp"
    try:
        with open(temp_file, "w", encoding="utf-8") as fout:
            fout.writelines(updated_items)
        
        # Atomic replacement of original file
        shutil.move(temp_file, response_file)
        print(f"✓ File updated in-place: {response_file}")
        
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        raise e
    
    # Calculate statistics
    if scores:
        accuracy = correct_items / len(scores)
        average_score = sum(scores) / len(scores)
    else:
        accuracy = 0.0
        average_score = 0.0
    
    # Calculate token statistics
    if tokens:
        average_tokens = sum(tokens) / len(tokens)
        total_tokens = sum(tokens)
        min_tokens = min(tokens)
        max_tokens = max(tokens)
        median_tokens = sorted(tokens)[len(tokens)//2]
    else:
        average_tokens = 0.0
        total_tokens = 0
        min_tokens = 0
        max_tokens = 0
        median_tokens = 0
    
    # Print statistics
    print("\n" + "=" * 60)
    print("Evaluation Results:")
    print("=" * 60)
    print(f"Total items: {total_items}")
    print(f"Successfully evaluated: {len(scores)}")
    print(f"Evaluation errors: {error_items}")
    print(f"Correct answers: {correct_items}")
    print(f"Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"Average score: {average_score:.4f}")
    
    print("\n" + "-" * 40)
    print("Token Usage Statistics:")
    print("-" * 40)
    print(f"Valid token records: {len(tokens)}")
    print(f"Total tokens: {total_tokens:,}")
    print(f"Average tokens: {average_tokens:.2f}")
    print(f"Min tokens: {min_tokens}")
    print(f"Max tokens: {max_tokens}")
    print(f"Median tokens: {median_tokens}")
    
    return {
        "total_items": total_items,
        "evaluated_items": len(scores),
        "error_items": error_items,
        "correct_items": correct_items,
        "accuracy": accuracy,
        "average_score": average_score,
        "scores": scores,
        "tokens": tokens,
        "average_tokens": average_tokens,
        "total_tokens": total_tokens
    }

def print_detailed_statistics(stats):
    """Print detailed statistics"""
    scores = stats["scores"]
    tokens = stats["tokens"]
    
    if not scores:
        print("No valid scoring data")
        return
    
    print("\n" + "=" * 60)
    print("Detailed Statistics:")
    print("=" * 60)
    
    # Score distribution (only 0.0 and 1.0)
    correct_count = sum(1 for score in scores if score == 1.0)
    incorrect_count = len(scores) - correct_count
    
    print("Score Distribution:")
    print(f"  Correct (1.0): {correct_count:4d} items ({correct_count/len(scores)*100:5.1f}%)")
    print(f"  Incorrect (0.0): {incorrect_count:4d} items ({incorrect_count/len(scores)*100:5.1f}%)")
    
    # Token detailed statistics
    if tokens:
        print(f"\n" + "=" * 60)
        print("Token Usage Detailed Statistics:")
        print("=" * 60)
        
        # Token distribution ranges
        token_ranges = [
            (0, 2000, "0-2000"),
            (2001, 5000, "2000-5000"),
            (5001, 10000, "5000-10000"),
            (10001, 20000, "10000-20000"),
            (20001, 30000, "20000-30000"),
            (30001, 50000, "30000-50000"),
            (50001, float('inf'), "50000+")
        ]
        
        print("Token Distribution:")
        for min_val, max_val, label in token_ranges:
            count = sum(1 for t in tokens if min_val <= t <= max_val)
            if count > 0:
                percentage = count / len(tokens) * 100
                print(f"  {label:>8}: {count:4d} items ({percentage:5.1f}%)")
        
        # Efficiency analysis
        if len(scores) == len(tokens):
            correct_tokens = [tokens[i] for i, score in enumerate(scores) if score == 1.0]
            incorrect_tokens = [tokens[i] for i, score in enumerate(scores) if score == 0.0]
            
            if correct_tokens and incorrect_tokens:
                avg_correct = sum(correct_tokens) / len(correct_tokens)
                avg_incorrect = sum(incorrect_tokens) / len(incorrect_tokens)
                print(f"\nEfficiency Analysis:")
                print(f"  Avg tokens (correct): {avg_correct:.2f}")
                print(f"  Avg tokens (incorrect): {avg_incorrect:.2f}")
                print(f"  Efficiency ratio: {avg_correct/avg_incorrect:.2f}")
    else:
        print(f"\nNo valid Token statistics data")

if __name__ == "__main__":
    args = parse_args()
    
    try:
        stats = evaluate_responses_inplace(args.response_file)
        print_detailed_statistics(stats)
        
    except Exception as e:
        print(f"Error: {e}")
        exit(1)