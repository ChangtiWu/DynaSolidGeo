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
point_P, point_A, point_B, point_C, point_D, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate() -> float:
    """计算 cosθ 的值（固定为 √3/6）"""
    return math.sqrt(3) / 6


len_t = 1.0
# result = calculate()
# print(f"cosθ = {result:.6f}")

# Generate random lengths
len_t = round(len_scaling_factor * float(len_t), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_36_2",
    "type": 2,
    "level": 1,
    "cn_problem": f"在三棱锥 {point_P}-{point_A}{point_B}{point_C} 中，{point_P}{point_C}⊥平面 {point_A}{point_B}{point_C}，∠{point_A}{point_C}{point_B} = 90°，{point_D},{point_E} 分别为线段 {point_A}{point_B},{point_B}{point_C} 上的点。设 {point_P}{point_C} = 3*{len_t}，{point_C}{point_D} = {point_D}{point_E} = √2*{len_t}，{point_C}{point_E} = 2*{len_t}，{point_E}{point_B} = {len_t}（其中 {len_t} > 0），使得 $\\triangle {point_C}{point_D}{point_E}$ 为直角等腰三角形（在 {point_D} 处成直角）。求二面角 {point_A}-{point_P}{point_D}-{point_C} 的余弦值 cos θ。",
    "en_problem": f"In triangular pyramid {point_P}-{point_A}{point_B}{point_C}, {point_P}{point_C}⊥plane {point_A}{point_B}{point_C}, ∠{point_A}{point_C}{point_B} = 90°, and {point_D},{point_E} are points on segments {point_A}{point_B},{point_B}{point_C} respectively. Let {point_P}{point_C} = 3*{len_t}, {point_C}{point_D} = {point_D}{point_E} = √2*{len_t}, {point_C}{point_E} = 2*{len_t}, {point_E}{point_B} = {len_t} (where {len_t} > 0), such that $\\triangle {point_C}{point_D}{point_E}$ forms a right isosceles triangle (with right angle at {point_D}). Find the cosine value of dihedral angle {point_A}-{point_P}{point_D}-{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_36_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
