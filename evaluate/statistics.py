import json
import argparse
import os
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', "--response_dec_file", type=str, required=True, help="Path to the response JSONL file.")
    return parser.parse_args()

def analyze_responses(response_file):
    """
    Analyze responses and compute statistics without modifying the file
    
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
    
    print(f"Analyzing file: {response_file}")
    print("-" * 70)
    
    # Read all data and process
    with open(response_file, "r", encoding="utf-8") as fin:
        lines = fin.readlines()
    
    for line in tqdm(lines, desc="Analyzing"):
        if not line.strip():
            continue
            
        try:
            item = json.loads(line.strip())
            
            # Get required fields
            item_id = item.get("id", "UNKNOWN")
            output_token = item.get("output_token", "N/A")
            item_type = item.get("type", "N/A")
            item_level = item.get("level", "N/A")
            expected_score = item.get("expected_score", None)
            solution_dec = item.get("solution_dec", None)
            process_dec = item.get("process_dec", None)
            
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
            
            # Use expected_score if available, otherwise use solution_dec
            score = expected_score if expected_score is not None else solution_dec
            
            if score is not None:
                scores.append(score)
                if score == 1.0:
                    correct_items += 1
            else:
                error_items += 1
            
            total_items += 1
            
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON line: {e}")
            error_items += 1
            continue
    
    # Calculate statistics
    if scores:
        accuracy = correct_items / len(scores)
    else:
        accuracy = 0.0
    
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
    print("\n" + "=" * 70)
    print(f"Analysis Results: {os.getenv('MODEL_NAME', 'UNKNOWN')}")
    print("=" * 70)
    print(f"Total items: {total_items}, Successfully analyzed: {len(scores)}, Analysis errors: {error_items}")
    print(f"Correct answers: {correct_items} ({accuracy*100:.2f}%)")
    
    print("\n" + "=" * 70)
    print("Token Usage Statistics:")
    print("=" * 70)
    print(f"Valid token records: {len(tokens)} (Total tokens: {total_tokens:,})")
    
    # Separate statistics for all, correct, and incorrect items
    if len(scores) == len(tokens):
        correct_tokens = [tokens[i] for i, score in enumerate(scores) if score == 1.0]
        incorrect_tokens = [tokens[i] for i, score in enumerate(scores) if score == 0.0]
        
        print(f"\n{'Category':<12} {'Count':<8} {'Avg':<10} {'Min':<8} {'Max':<8} {'Median':<8}")
        print("-" * 70)
        
        # All items
        print(f"{'All Items':<12} {len(tokens):<8} {average_tokens:<10.2f} {min_tokens:<8} {max_tokens:<8} {median_tokens:<8}")
        
        # Correct items
        if correct_tokens:
            avg_correct = sum(correct_tokens) / len(correct_tokens)
            min_correct = min(correct_tokens)
            max_correct = max(correct_tokens)
            median_correct = sorted(correct_tokens)[len(correct_tokens)//2]
            print(f"{'Correct':<12} {len(correct_tokens):<8} {avg_correct:<10.2f} {min_correct:<8} {max_correct:<8} {median_correct:<8}")
        else:
            print(f"{'Correct':<12} {0:<8} {0.0:<10.2f} {0:<8} {0:<8} {0:<8}")
        
        # Incorrect items
        if incorrect_tokens:
            avg_incorrect = sum(incorrect_tokens) / len(incorrect_tokens)
            min_incorrect = min(incorrect_tokens)
            max_incorrect = max(incorrect_tokens)
            median_incorrect = sorted(incorrect_tokens)[len(incorrect_tokens)//2]
            print(f"{'Incorrect':<12} {len(incorrect_tokens):<8} {avg_incorrect:<10.2f} {min_incorrect:<8} {max_incorrect:<8} {median_incorrect:<8}")
        else:
            print(f"{'Incorrect':<12} {0:<8} {0.0:<10.2f} {0:<8} {0:<8} {0:<8}")
    else:
        print(f"Average tokens: {average_tokens:.2f}", end="")
        print(f" (Min: {min_tokens:.2f}, Max: {max_tokens:.2f}, Median: {median_tokens:.2f})")

    return {
        "total_items": total_items,
        "analyzed_items": len(scores),
        "error_items": error_items,
        "correct_items": correct_items,
        "accuracy": accuracy,
        "average_score": sum(scores) / len(scores) if scores else 0.0,
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
        
        print("\nToken Distribution:")
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

def analyze_by_category(response_file):
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
    
    # Read the file to get detailed statistics with type/level info
    detailed_data = []
    
    with open(response_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    item = json.loads(line.strip())
                    expected_score = item.get("expected_score", None)
                    solution_dec = item.get("solution_dec", None)
                    score = expected_score if expected_score is not None else solution_dec
                    
                    if score is not None:
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
                            "score": score,
                            "token": token_val
                        })
                except json.JSONDecodeError:
                    continue
    
    if not detailed_data:
        print("No detailed data available for category analysis")
        return
    
    print("\n" + "=" * 70)
    print("CATEGORY ANALYSIS")
    print("=" * 70)
    
    # Analysis by Type
    print("\n📊 Analysis by Problem Type:")
    print("-" * 70)
    type_stats = {}
    for data in detailed_data:
        if data["type"] != "N/A" and data["token"] != "N/A":
            t = data["type"]
            if t not in type_stats:
                type_stats[t] = {"scores": [], "tokens": []}
            type_stats[t]["scores"].append(data["score"])
            type_stats[t]["tokens"].append(data["token"])
    
    for t in sorted(type_stats.keys()):
        scores = type_stats[t]["scores"]
        tokens = type_stats[t]["tokens"]
        correct = sum(1 for s in scores if s == 1.0)
        accuracy = correct / len(scores) if scores else 0.0
        
        # Calculate token statistics for correct, incorrect, and all items
        correct_tokens = [tokens[i] for i, score in enumerate(scores) if score == 1.0]
        incorrect_tokens = [tokens[i] for i, score in enumerate(scores) if score == 0.0]
        
        avg_all = sum(tokens) / len(tokens) if tokens else 0.0
        avg_correct = sum(correct_tokens) / len(correct_tokens) if correct_tokens else 0.0
        avg_incorrect = sum(incorrect_tokens) / len(incorrect_tokens) if incorrect_tokens else 0.0
        
        print(f"Type {t}: {type_names.get(t, 'Unknown')}")
        print(f"  Items: {len(scores):3d} | Accuracy: {accuracy*100:5.1f}%")
        print(f"  Tokens - All: {avg_all:7.1f} | Correct: {avg_correct:7.1f} | Incorrect: {avg_incorrect:7.1f}")
    
    # Analysis by Level
    print("\n📈 Analysis by Difficulty Level:")
    print("-" * 70)
    level_stats = {}
    for data in detailed_data:
        if data["level"] != "N/A" and data["token"] != "N/A":
            l = data["level"]
            if l not in level_stats:
                level_stats[l] = {"scores": [], "tokens": []}
            level_stats[l]["scores"].append(data["score"])
            level_stats[l]["tokens"].append(data["token"])
    
    for l in sorted(level_stats.keys()):
        scores = level_stats[l]["scores"]
        tokens = level_stats[l]["tokens"]
        correct = sum(1 for s in scores if s == 1.0)
        accuracy = correct / len(scores) if scores else 0.0
        
        # Calculate token statistics for correct, incorrect, and all items
        correct_tokens = [tokens[i] for i, score in enumerate(scores) if score == 1.0]
        incorrect_tokens = [tokens[i] for i, score in enumerate(scores) if score == 0.0]
        
        avg_all = sum(tokens) / len(tokens) if tokens else 0.0
        avg_correct = sum(correct_tokens) / len(correct_tokens) if correct_tokens else 0.0
        avg_incorrect = sum(incorrect_tokens) / len(incorrect_tokens) if incorrect_tokens else 0.0
        
        print(f"Level {l}: {level_names.get(l, 'Unknown')}")
        print(f"  Items: {len(scores):3d} | Accuracy: {accuracy*100:5.1f}%")
        print(f"  Tokens - All: {avg_all:7.1f} | Correct: {avg_correct:7.1f} | Incorrect: {avg_incorrect:7.1f}")
    
    # Cross analysis: Type vs Level
    print("\n🔍 Cross Analysis: Type vs Level Accuracy Matrix:")
    print("-" * 70)
    print("Type\\Level", end="")
    for l in sorted(level_stats.keys()):
        print(f"{level_names.get(l, f'L{l}'):>12}", end="   ")
    print()
    print("-" * 70)
    
    for t in sorted(type_stats.keys()):
        print(f"Type {t:2d}   ", end="")
        for l in sorted(level_stats.keys()):
            # Find items with this type and level (only those with valid tokens)
            items = [d for d in detailed_data if d["type"] == t and d["level"] == l and d["score"] is not None and d["token"] != "N/A"]
            if items:
                correct = sum(1 for item in items if item["score"] == 1.0)
                accuracy = correct / len(items)
                print(f"  {accuracy:8.3f} ({len(items):2d})", end="")
            else:
                print(f"{'':>12}", end="")
        print()

if __name__ == "__main__":
    args = parse_args()
    
    try:
        stats = analyze_responses(args.response_dec_file)
        print_detailed_statistics(stats)
        analyze_by_category(args.response_dec_file)
        
    except Exception as e:
        print(f"Error: {e}")
        exit(1)