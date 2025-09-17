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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_F, point_M = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math


def calculate(val_k: float) -> float:
    """计算 λ 的值（根据公式 λ=1 - val_k/√(5(1-val_k²))）"""
    denominator = math.sqrt(5 * (1 - val_k ** 2))
    return 1 - val_k / denominator


len_a = 2.0
val_k = math.sqrt(5) / 3

# result = calculate(val_k)
# print(f"λ = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
val_k = round(random.uniform(0.1, 0.9), 1) # cosine


# Calculate the result
result = calculate(val_k)

# Define LaTeX expressions separately to avoid backslashes in f-strings
lambda_frac = f"\\lambda=\\dfrac{{{point_A1}{point_M}}}{{{point_A1}{point_B1}}}"

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_8_4_2",
    "type": 3,
    "level": 2,
    "cn_problem": f"在正方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 中，棱长为 {len_a}（{len_a}>0）。设 {point_E} 为棱 {point_A1}{point_D1} 的中点；设直线 {point_B}{point_C1} 与平面 {point_C}{point_D}{point_E} 交于点 {point_F}；再取点 {point_M} 为棱 {point_A1}{point_B1} 上的动点，记 \\({lambda_frac}\\in[0,1]\\)。已知二面角 {point_M}-{point_F}{point_C}-{point_E} 的平面角余弦为给定常数 {val_k}（0<{val_k}<1）。求 \\(\\lambda\\)。",
    "en_problem": f"In the cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} with edge length {len_a} ({len_a}>0), let {point_E} be the midpoint of edge {point_A1}{point_D1}. Line {point_B}{point_C1} meets plane {point_C}{point_D}{point_E} at {point_F}. A moving point {point_M} lies on edge {point_A1}{point_B1}, and we denote \\({lambda_frac}\\in[0,1]\\). The cosine of the dihedral angle formed by {point_M}-{point_F}{point_C}-{point_E} is a given constant {val_k} with 0<{val_k}<1. Find \\(\\lambda\\).",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_8_4_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_F}', '{point_M}')"}, ensure_ascii=False) + "\n")
