import json
import os
# Set random seed
import random
import argparse
import string
import math

parser = argparse.ArgumentParser()
parser.add_argument('--seed', type=int, default=0, help='Random seed (default: 0)')
parser.add_argument('--mode', type=int, default=0, choices=[0, 1], help='Mode (default: 0)')
args, unknown = parser.parse_known_args()
random.seed(args.seed)

# Scaling factor
len_scaling_factor = round(random.uniform(0.1, 100.0), 1)

# Generate random point names
point_A = random.sample(string.ascii_uppercase, 1)[0]

# Add result calculation code
def calculate(len_a: float, len_b: float, len_c: float) -> float:
    """计算体积 volume_O 的表达式值（volume_O = (len_a·len_b·len_c)/6）"""
    return (len_a * len_b * len_c) / 6


len_a = 5.0
len_b = 4.0
len_c = 3.0


# result = calculate(len_a, len_b, len_c)
# print(f"volume_O = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_15_amc10B_17",
    "type": 5,
    "level": 1,
    "cn_problem": f"设有一长、宽、高分别为 {len_a},{len_b},{len_c}>0 的矩形平行六面体（直角棱柱）。取该棱柱 6 个面的中心（记为 {point_A}_1, {point_A}_2, {point_A}_3, {point_A}_4, {point_A}_5, {point_A}_6），将它们两两连线，得到一个凸八面体。求该八面体的体积。",
    "en_problem": f"Consider a rectangular parallelepiped (right prism) with length, width, and height {len_a},{len_b},{len_c}>0 respectively. Take the centers of the 6 faces of this prism (denoted as {point_A}_1, {point_A}_2, {point_A}_3, {point_A}_4, {point_A}_5, {point_A}_6) and connect them pairwise to form a convex octahedron. Find the volume of this octahedron.",
    "solution": f"{result}",
    "image": f"images/{os.path.splitext(os.path.basename(__file__))[0]}.png"
}

# Save to jsonl
jsonl_path = os.path.join(os.path.dirname(__file__), "../../data/problem.jsonl")
os.makedirs(os.path.dirname(jsonl_path), exist_ok=True)
with open(jsonl_path, "a", encoding="utf-8") as f:
    f.write(json.dumps(json_data, ensure_ascii=False) + "\n")
    
# ─── 2. save MATLAB command JSONL ─────────────────────────────── 
mode = args.mode
azimuth = (-150 + random.randint(0, 360)) % 360
elevation = (25 + random.randint(0, 360)) % 360

matlab_cmd_jsonl_path = os.path.join(os.path.dirname(__file__), "../../data/matlab_cmd.jsonl")
os.makedirs(os.path.dirname(matlab_cmd_jsonl_path), exist_ok=True)
with open(matlab_cmd_jsonl_path, "a", encoding="utf-8") as f:
    f.write(json.dumps({json_data["id"]: f"aops_15_amc10B_17({mode}, {azimuth}, {elevation}, '{point_A}')"}, ensure_ascii=False) + "\n")
