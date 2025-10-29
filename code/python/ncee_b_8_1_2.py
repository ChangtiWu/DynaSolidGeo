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
point_P, point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(param_lambda: float, len_k: float) -> float:
    """计算 AD 的长度（AD = λ·len_k）"""
    return param_lambda * len_k


param_lambda = math.sqrt(3)
len_k = 1.0
param_s = math.sqrt(42) / 7


# result = calculate(param_lambda, len_k)
# print(f"AD = {result:.6f}")

# Generate random lengths

len_k = round(len_scaling_factor * float(len_k), 2)

# Calculate the result
result = calculate(param_lambda, len_k)

# Define LaTeX expressions separately to avoid backslashes in f-strings
triangle_symbol = "\\triangle"
sqrt_lambda_plus_1 = f"\\sqrt{{{param_lambda}^2+1}}"

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_8_1_2",
    "type": 3,
    "level": 2,
    "cn_problem": f"在四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 中，{point_P}{point_A}⊥平面 {point_A}{point_B}{point_C}{point_D}，${triangle_symbol} {point_A}{point_B}{point_C}$ 直角于 {point_B}，且 {point_A}{point_B} = {param_lambda}*{len_k}，{point_B}{point_C} = {len_k}，{point_A}{point_C} = {sqrt_lambda_plus_1}*{len_k}，{point_P}{point_A} = {sqrt_lambda_plus_1}*{len_k}（其中 {param_lambda}>0，{len_k}>0）。设 {point_A}{point_D}⊥{point_D}{point_C}，并记 sin(二面角 {point_A}-{point_C}{point_P}-{point_D}) = {param_s}（0<{param_s}<1）。求边长 {point_A}{point_D}。",
    "en_problem": f"In quadrilateral pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, {point_P}{point_A}⊥plane {point_A}{point_B}{point_C}{point_D}, ${triangle_symbol} {point_A}{point_B}{point_C}$ has right angle at {point_B}, with {point_A}{point_B} = {param_lambda}*{len_k}, {point_B}{point_C} = {len_k}, {point_A}{point_C} = {sqrt_lambda_plus_1}*{len_k}, {point_P}{point_A} = {sqrt_lambda_plus_1}*{len_k} (where {param_lambda}>0, {len_k}>0). Let {point_A}{point_D}⊥{point_D}{point_C}, and denote sin(dihedral angle {point_A}-{point_C}{point_P}-{point_D}) = {param_s} (0<{param_s}<1). Find the edge length {point_A}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_8_1_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
