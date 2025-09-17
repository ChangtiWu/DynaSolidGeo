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
point_A, point_B, point_C, point_D, point_E = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate():
    """计算满足cos(theta) = √7/7的角度theta（弧度制）"""
    return math.sqrt(7) / 7


# 测试示例
len_a = 2.0
arg_alpha = math.pi / 2

# print(calculate())

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_27_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"四面体{point_A}{point_B}{point_C}{point_D}中，△{point_A}{point_B}{point_C}是正三角形，边长为{len_a}，△{point_A}{point_C}{point_D}是等腰直角三角形，∠{point_A}{point_D}{point_C}={arg_alpha}，∠{point_A}{point_B}{point_D}=∠{point_C}{point_B}{point_D}，{point_A}{point_B}={point_B}{point_D}。过{point_A}{point_C}的平面交{point_B}{point_D}于点{point_E}，若平面{point_A}{point_E}{point_C}把四面体{point_A}{point_B}{point_C}{point_D}分成体积相等的两部分，求二面角{point_D}-{point_A}{point_E}-{point_C}的余弦值。",
    "en_problem": f"In tetrahedron {point_A}{point_B}{point_C}{point_D}, △{point_A}{point_B}{point_C} is an equilateral triangle with side length {len_a}, △{point_A}{point_C}{point_D} is an isosceles right triangle with ∠{point_A}{point_D}{point_C}={arg_alpha}, ∠{point_A}{point_B}{point_D}=∠{point_C}{point_B}{point_D}, and {point_A}{point_B}={point_B}{point_D}. A plane through {point_A}{point_C} intersects {point_B}{point_D} at point {point_E}, and plane {point_A}{point_E}{point_C} divides tetrahedron {point_A}{point_B}{point_C}{point_D} into two parts of equal volume. Find the cosine of dihedral angle {point_D}-{point_A}{point_E}-{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_27_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
