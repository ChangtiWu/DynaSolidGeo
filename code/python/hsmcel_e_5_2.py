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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_a: float, len_h: float) -> float:
    """计算长度 len_d 的表达式值（公式：len_d = (len_a·len_h)/(2√(len_h² + len_a²))）"""
    numerator = len_a * len_h
    denominator = 2 * math.sqrt(len_h ** 2 + len_a ** 2)
    return numerator / denominator


len_a = 6.0
len_h = 8.0

# result = calculate(len_a, len_h)
# print(f"len_d = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_5_2",
    "type": 3,
    "level": 2,
    "cn_problem": f"在正三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，下底与上底分别为全等的正三角形，设 ${point_A}{point_B}={point_B}{point_C}={point_C}{point_A}={len_a}>0$，${point_A}{point_A1}={point_B}{point_B1}={point_C}{point_C1}={len_h}>0$。取点 {point_D} 为棱 $\\overline{{ {point_A}{point_B} }}$ 的中点。求下底顶点 {point_C} 与中点 {point_D} 的连线 $\\overline{{ {point_C}{point_D} }}$ 与斜棱 $\\overline{{ {point_A1}{point_B} }}$ 这两条异面直线的最短距离。",
    "en_problem": f"In a regular triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, where the lower and upper bases are congruent equilateral triangles, let ${point_A}{point_B}={point_B}{point_C}={point_C}{point_A}={len_a}>0$ and ${point_A}{point_A1}={point_B}{point_B1}={point_C}{point_C1}={len_h}>0$. Let point {point_D} be the midpoint of edge $\\overline{{ {point_A}{point_B} }}$. Find the shortest distance between the two skew lines: the line $\\overline{{ {point_C}{point_D} }}$ connecting base vertex {point_C} with midpoint {point_D}, and the oblique edge $\\overline{{ {point_A1}{point_B} }}$.",
    "solution": f"{result}",
    "image": f"images/{os.path.splitext(os.path.basename(__file__))[0]}.png"
}

# video mode
if args.mode == 1:
    json_data["image"] = f"videos/{os.path.splitext(os.path.basename(__file__))[0]}.mp4"



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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_5_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}')"}, ensure_ascii=False) + "\n")
