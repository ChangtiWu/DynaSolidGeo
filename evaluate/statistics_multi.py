import json
import argparse
import os
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-r', "--response_dec_files", type=str, nargs='+', required=True,
        help="Path(s) to the response JSONL file(s). You can pass multiple paths separated by space."
    )
    return parser.parse_args()

def convert_process_dec(process_dec):
    """
    Convert process_dec to float, handle '-1' as 0.75 per requirement.
    Accepts process_dec as None, int, float, or str.
    """
    if process_dec is None:
        return None
    try:
        val = float(process_dec)
        if val == -1:
            return 0.75
        return val
    except Exception:
        # Maybe process_dec is actually string '-1'
        if str(process_dec).strip() == "-1":
            return 0.75
        return None

def load_all_lines(response_files):
    """Load all lines from a list of files and return as a flat list"""
    all_lines = []
    for file in response_files:
        if not os.path.exists(file):
            print(f"Warning: Response file {file} does not exist and will be skipped.")
            continue
        with open(file, "r", encoding="utf-8") as fin:
            file_lines = fin.readlines()
        all_lines.extend(file_lines)
    return all_lines

def analyze_responses(response_files):
    """
    Analyze responses and compute statistics for a list of JSONL files
    Args:
        response_files: List of path strings to JSONL files containing model responses
    """
    lines = load_all_lines(response_files)
    if not lines:
        raise FileNotFoundError(f"No valid input files or files are empty: {response_files}")
    
    print(f"Analyzing files: {response_files}")
    print("-" * 70)

    # Statistics variables
    total_items = 0
    correct_items = 0
    error_items = 0
    scores = []
    tokens = []  # Token statistics
    types = []   # Type statistics
    levels = []  # Level statistics

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
    print(f"Analysis Results:")
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

def analyze_by_category(response_files):
    """
    Analyze statistics by type and level categories for a list of files
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

    lines = load_all_lines(response_files)
    if not lines:
        print("No detailed data available for category analysis")
        return

    detailed_data = []

    for line in lines:
        if line.strip():
            try:
                item = json.loads(line.strip())
                expected_score = item.get("expected_score", None)
                solution_dec = item.get("solution_dec", None)
                process_dec = item.get("process_dec", None)
                score = expected_score if expected_score is not None else solution_dec

                # Convert process_dec - if -1, treat as 0.75
                process_dec_converted = convert_process_dec(process_dec)

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
                        "token": token_val,
                        "process_dec": process_dec_converted
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
    process_type_stats = {}
    for data in detailed_data:
        if data["type"] != "N/A" and data["token"] != "N/A":
            t = data["type"]
            if t not in type_stats:
                type_stats[t] = {"scores": [], "tokens": []}
            type_stats[t]["scores"].append(data["score"])
            type_stats[t]["tokens"].append(data["token"])
        # For process_dec statistics
        if data["type"] != "N/A" and data["process_dec"] is not None:
            t = data["type"]
            if t not in process_type_stats:
                process_type_stats[t] = {"process_scores": [], "solution_scores": [], "joint_correct": 0, "total": 0}
            process_score = data["process_dec"]
            process_type_stats[t]["total"] += 1
            if process_score is not None:
                process_type_stats[t]["process_scores"].append(process_score)
                process_type_stats[t]["solution_scores"].append(data["score"])
                # solution=1 and process>=0.75
                if data["score"] == 1.0 and process_score >= 0.75:
                    process_type_stats[t]["joint_correct"] += 1

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
        print(f"  Items: {correct:3d}/{len(scores):3d} | Accuracy: {accuracy*100:5.2f}%")
        print(f"  Tokens - All: {avg_all:7.1f} | Correct: {avg_correct:7.1f} | Incorrect: {avg_incorrect:7.1f}")
        # Process_dec statistics by type
        if t in process_type_stats and process_type_stats[t]["process_scores"]:
            avg_process = sum(process_type_stats[t]["process_scores"]) / len(process_type_stats[t]["process_scores"])
            joint_total = len(process_type_stats[t]["process_scores"])
            joint_correct = process_type_stats[t]["joint_correct"]
            joint_ratio = joint_correct / joint_total if joint_total > 0 else 0.0
            print(f"  Avg process_dec score: {avg_process:.4f}")
            print(f"  综合正确率(solution=1 & process>=0.75): {joint_correct}/{joint_total} ({joint_ratio*100:.2f}%)")

    # Analysis by Level
    print("\n📈 Analysis by Difficulty Level:")
    print("-" * 70)
    level_stats = {}
    process_level_stats = {}
    for data in detailed_data:
        if data["level"] != "N/A" and data["token"] != "N/A":
            l = data["level"]
            if l not in level_stats:
                level_stats[l] = {"scores": [], "tokens": []}
            level_stats[l]["scores"].append(data["score"])
            level_stats[l]["tokens"].append(data["token"])
        # For process_dec statistics
        if data["level"] != "N/A" and data["process_dec"] is not None:
            l = data["level"]
            if l not in process_level_stats:
                process_level_stats[l] = {"process_scores": [], "solution_scores": [], "joint_correct": 0, "total": 0}
            process_score = data["process_dec"]
            process_level_stats[l]["total"] += 1
            if process_score is not None:
                process_level_stats[l]["process_scores"].append(process_score)
                process_level_stats[l]["solution_scores"].append(data["score"])
                if data["score"] == 1.0 and process_score >= 0.75:
                    process_level_stats[l]["joint_correct"] += 1

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
        print(f"  Items: {correct:3d}/{len(scores):3d} | Accuracy: {accuracy*100:5.2f}%")
        print(f"  Tokens - All: {avg_all:7.1f} | Correct: {avg_correct:7.1f} | Incorrect: {avg_incorrect:7.1f}")
        # Process_dec statistics by level
        if l in process_level_stats and process_level_stats[l]["process_scores"]:
            avg_process = sum(process_level_stats[l]["process_scores"]) / len(process_level_stats[l]["process_scores"])
            joint_total = len(process_level_stats[l]["process_scores"])
            joint_correct = process_level_stats[l]["joint_correct"]
            joint_ratio = joint_correct / joint_total if joint_total > 0 else 0.0
            print(f"  Avg process_dec score: {avg_process:.4f}")
            print(f"  综合正确率(solution=1 & process>=0.75): {joint_correct}/{joint_total} ({joint_ratio*100:.2f}%)")

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

def analyze_process_dec(response_files):
    """
    统计process_dec字段（评分），不仅统计不同类别的平均分，而且给出solution=1&&process>=0.75的比率（综合正确率）
    并输出总体的过程得分
    支持多个文件的合并统计
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
    # Gather data
    process_type_stats = {}
    process_level_stats = {}
    total_joint = 0
    total_joint_correct = 0
    all_process_scores = []

    lines = load_all_lines(response_files)
    if not lines:
        print("\nNo process_dec statistics available.")
        return

    for line in lines:
        if not line.strip():
            continue
        try:
            item = json.loads(line.strip())
        except Exception:
            continue
        t = item.get("type", None)
        l = item.get("level", None)
        solution = item.get("expected_score", None)
        if solution is None:
            solution = item.get("solution_dec", None)
        process = item.get("process_dec", None)
        process_score = convert_process_dec(process)
        # By type
        if t is not None and process_score is not None:
            if t not in process_type_stats:
                process_type_stats[t] = {"process_scores": [], "joint_correct": 0, "total": 0}
            process_type_stats[t]["process_scores"].append(process_score)
            process_type_stats[t]["total"] += 1
            if solution == 1.0 and process_score >= 0.75:
                process_type_stats[t]["joint_correct"] += 1
        # By level
        if l is not None and process_score is not None:
            if l not in process_level_stats:
                process_level_stats[l] = {"process_scores": [], "joint_correct": 0, "total": 0}
            process_level_stats[l]["process_scores"].append(process_score)
            process_level_stats[l]["total"] += 1
            if solution == 1.0 and process_score >= 0.75:
                process_level_stats[l]["joint_correct"] += 1
        # Overall
        if process_score is not None:
            total_joint += 1
            all_process_scores.append(process_score)
            if solution == 1.0 and process_score >= 0.75:
                total_joint_correct += 1
    if not process_type_stats and not process_level_stats:
        print("\nNo process_dec statistics available.")
        return
    print("\n" + "=" * 70)
    print("process_dec 字段统计（评分）及综合正确率")
    print("=" * 70)
    # By type
    print("\n📊 按类别统计 process_dec 平均分及综合正确率:")
    print("-" * 70)
    for t in sorted(process_type_stats.keys()):
        avg_process = sum(process_type_stats[t]["process_scores"]) / len(process_type_stats[t]["process_scores"])
        joint_correct = process_type_stats[t]["joint_correct"]
        total = process_type_stats[t]["total"]
        joint_ratio = joint_correct / total if total > 0 else 0.0
        print(f"Type {t}: {type_names.get(t, 'Unknown')}")
        print(f"  Avg process_dec score: {avg_process:.4f}")
        print(f"  综合正确率(solution=1 & process>=0.75): {joint_correct}/{total} ({joint_ratio*100:.2f}%)")
    # By level
    print("\n📈 按难度统计 process_dec 平均分及综合正确率:")
    print("-" * 70)
    for l in sorted(process_level_stats.keys()):
        avg_process = sum(process_level_stats[l]["process_scores"]) / len(process_level_stats[l]["process_scores"])
        joint_correct = process_level_stats[l]["joint_correct"]
        total = process_level_stats[l]["total"]
        joint_ratio = joint_correct / total if total > 0 else 0.0
        print(f"Level {l}: {level_names.get(l, 'Unknown')}")
        print(f"  Avg process_dec score: {avg_process:.4f}")
        print(f"  综合正确率(solution=1 & process>=0.75): {joint_correct}/{total} ({joint_ratio*100:.2f}%)")
    # Overall
    print("\n🔢 综合正确率（所有有 process_dec 的样本）:")
    joint_ratio = total_joint_correct / total_joint if total_joint > 0 else 0.0
    print(f"  综合正确率(solution=1 & process>=0.75): {total_joint_correct}/{total_joint} ({joint_ratio*100:.2f}%)")
    # 输出总体的过程得分
    if all_process_scores:
        avg_overall_process = sum(all_process_scores) / len(all_process_scores)
        print(f"\n🌟 总体 process_dec 平均分: {avg_overall_process:.3f}")
    else:
        print(f"\n🌟 总体 process_dec 平均分: 无数据")

if __name__ == "__main__":
    args = parse_args()
    try:
        stats = analyze_responses(args.response_dec_files)
        print_detailed_statistics(stats)
        analyze_by_category(args.response_dec_files)
        analyze_process_dec(args.response_dec_files)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)