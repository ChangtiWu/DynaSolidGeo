import json
import argparse
import os
import tempfile
import shutil
from tqdm import tqdm

from geo_evalute import compute_score

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', "--response_file", type=str, required=True, help="Path to the response JSONL file.")
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
    types = []   # Type statistics
    levels = []  # Level statistics
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
            item_type = item.get("type", "N/A")
            item_level = item.get("level", "N/A")
            
            # Collect token statistics (skip N/A)
            if output_token != "N/A" and output_token is not None:
                try:
                    token_count = int(output_token) if isinstance(output_token, str) else output_token
                    tokens.append(token_count)
                except (ValueError, TypeError):
                    pass  # Skip tokens that cannot be converted to numbers
            
            # Collect type and level statistics
            if item_type != "N/A" and item_type is not None:
                types.append(item_type)
            if item_level != "N/A" and item_level is not None:
                levels.append(item_level)
            
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
    print(f"Evaluation Results: {os.getenv('MODEL_NAME', 'UNKNOWN')}")
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
        "types": types,
        "levels": levels,
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
    
    # Token detailed statistics
    if tokens:
        print(f"\n" + "=" * 60)
        print("Token Usage Detailed Statistics:")
        print("=" * 60)
        
        # Token distribution ranges
        token_ranges = [
            (0, 2000, "    0- 2000"),
            (2001, 5000, " 2000- 5000"),
            (5001, 10000, " 5000-10000"),
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

def analyze_by_category(stats):
    """
    Analyze statistics by type and level categories
    """
    # Type mapping
    type_names = {
        1: "Positional Relationship Determination (PD)",
        2: "Angle Calculation (AN)", 
        3: "Length and Distance Calculation (LC)",
        4: "Area Calculation (AR)",
        5: "Volume Calculation (VC)",
        6: "Counting Problems (CP)",
        7: "Dynamic or Moving-Point Problems (DM)",
        8: "Folding and Unfolding Problems (FP)"
    }
    
    # Level mapping
    level_names = {
        1: "Easy",
        2: "Medium", 
        3: "Hard"
    }
    
    # Read the file again to get detailed statistics with type/level info
    response_file = parse_args().response_file
    detailed_data = []
    
    with open(response_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    item = json.loads(line.strip())
                    if "expected_score" in item:
                        token_val = item.get("output_token", "N/A")
                        if token_val != "N/A":
                            try:
                                token_val = int(token_val) if isinstance(token_val, str) else token_val
                            except (ValueError, TypeError):
                                token_val = "N/A"
                        
                        detailed_data.append({
                            "id": item.get("id", "UNKNOWN"),
                            "type": item.get("type", "N/A"),
                            "level": item.get("level", "N/A"),
                            "score": item.get("expected_score", 0.0),
                            "token": token_val
                        })
                except json.JSONDecodeError:
                    continue
    
    if not detailed_data:
        print("No detailed data available for category analysis")
        return
    
    print("\n" + "=" * 80)
    print("CATEGORY ANALYSIS")
    print("=" * 80)
    
    # Analysis by Type
    print("\n📊 Analysis by Problem Type:")
    print("-" * 60)
    type_stats = {}
    for data in detailed_data:
        if data["type"] != "N/A":
            t = data["type"]
            if t not in type_stats:
                type_stats[t] = {"scores": [], "tokens": []}
            type_stats[t]["scores"].append(data["score"])
            if data["token"] != "N/A":
                type_stats[t]["tokens"].append(data["token"])
    
    for t in sorted(type_stats.keys()):
        scores = type_stats[t]["scores"]
        tokens = type_stats[t]["tokens"]
        correct = sum(1 for s in scores if s == 1.0)
        accuracy = correct / len(scores) if scores else 0.0
        avg_tokens = sum(tokens) / len(tokens) if tokens else 0.0
        
        print(f"Type {t}: {type_names.get(t, 'Unknown')}")
        print(f"  Items: {len(scores):3d} | Accuracy: {accuracy:.3f} ({accuracy*100:5.1f}%) | Avg Tokens: {avg_tokens:6.1f}")
    
    # Analysis by Level
    print("\n📈 Analysis by Difficulty Level:")
    print("-" * 60)
    level_stats = {}
    for data in detailed_data:
        if data["level"] != "N/A":
            l = data["level"]
            if l not in level_stats:
                level_stats[l] = {"scores": [], "tokens": []}
            level_stats[l]["scores"].append(data["score"])
            if data["token"] != "N/A":
                level_stats[l]["tokens"].append(data["token"])
    
    for l in sorted(level_stats.keys()):
        scores = level_stats[l]["scores"]
        tokens = level_stats[l]["tokens"]
        correct = sum(1 for s in scores if s == 1.0)
        accuracy = correct / len(scores) if scores else 0.0
        avg_tokens = sum(tokens) / len(tokens) if tokens else 0.0
        
        print(f"Level {l}: {level_names.get(l, 'Unknown')}")
        print(f"  Items: {len(scores):3d} | Accuracy: {accuracy:.3f} ({accuracy*100:5.1f}%) | Avg Tokens: {avg_tokens:6.1f}")
    
    # Cross analysis: Type vs Level
    print("\n🔍 Cross Analysis: Type vs Level Accuracy Matrix:")
    print("-" * 80)
    print("Type\\Level", end="")
    for l in sorted(level_stats.keys()):
        print(f"{level_names.get(l, f'L{l}'):>12}", end="")
    print()
    print("-" * 80)
    
    for t in sorted(type_stats.keys()):
        print(f"Type {t:2d}   ", end="")
        for l in sorted(level_stats.keys()):
            # Find items with this type and level
            items = [d for d in detailed_data if d["type"] == t and d["level"] == l and d["score"] is not None]
            if items:
                correct = sum(1 for item in items if item["score"] == 1.0)
                accuracy = correct / len(items)
                print(f"{accuracy:8.3f}({len(items):2d})", end="")
            else:
                print(f"{'':>12}", end="")
        print()

if __name__ == "__main__":
    args = parse_args()
    
    try:
        stats = evaluate_responses_inplace(args.response_file)
        print_detailed_statistics(stats)
        analyze_by_category(stats)
        
    except Exception as e:
        print(f"Error: {e}")
        exit(1)