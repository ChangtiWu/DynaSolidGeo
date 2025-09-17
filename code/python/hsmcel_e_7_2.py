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
point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
def calculate(len_a: float, len_b: float, len_c: float) -> float:
    """计算 cos(arg_theta) 的值（公式：cos(arg_theta) = |len_b² - len_c²| / len_a²）"""
    numerator = abs(len_b ** 2 - len_c ** 2)
    denominator = len_a ** 2
    return numerator / denominator


len_a = 2.0
len_b = 3.0
len_c = 2.0

# result = calculate(len_a, len_b, len_c)
# print(f"cos_arg_theta = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_7_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在四面体 ${point_A}{point_B}{point_C}{point_D}$ 中给定 ${point_A}{point_B} = {point_C}{point_D} = {len_a}$，${point_B}{point_C} = {point_A}{point_D} = {len_b}$，${point_C}{point_A} = {point_B}{point_D} = {len_c}$，${len_a},{len_b},{len_c}>0$。设异面直线 ${point_A}{point_B}$ 与 ${point_C}{point_D}$ 所成角为 $arg_theta$。求 $\\cosarg_theta$。",
    "en_problem": f"In tetrahedron ${point_A}{point_B}{point_C}{point_D}$, given ${point_A}{point_B} = {point_C}{point_D} = {len_a}$, ${point_B}{point_C} = {point_A}{point_D} = {len_b}$, ${point_C}{point_A} = {point_B}{point_D} = {len_c}$, where ${len_a},{len_b},{len_c}>0$. Let the angle between skew lines ${point_A}{point_B}$ and ${point_C}{point_D}$ be $arg_theta$. Find $\\cos arg_theta$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_7_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
