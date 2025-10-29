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
point_P, point_A, point_B, point_C, point_D, point_E, point_N, point_M = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a, len_b):
    """计算sin(theta)的值（公式：len_b*√5 / √(4len_a² + 5len_b²)）"""
    numerator = len_b * math.sqrt(5)
    denominator = math.sqrt(4 * (len_a ** 2) + 5 * (len_b ** 2))
    return numerator / denominator


# 测试示例
arg_beta = math.pi / 2
len_a = 4.0
len_b = 2.0

# print(calculate(len_a, len_b))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_8_5_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在三棱锥{point_P}-{point_A}{point_B}{point_C}中，{point_P}{point_A}⊥底面{point_A}{point_B}{point_C}，∠{point_B}{point_A}{point_C}={arg_beta}。点{point_D}、{point_E}、{point_N}分别为棱{point_P}{point_A}、{point_P}{point_C}、{point_B}{point_C}的中点，{point_M}是线段{point_A}{point_D}的中点，{point_P}{point_A}={point_A}{point_C}={len_a}，{point_A}{point_B}={len_b}。求二面角{point_C}-{point_E}{point_M}-{point_N}的正弦值。",
    "en_problem": f"In triangular pyramid {point_P}-{point_A}{point_B}{point_C}, {point_P}{point_A}⊥base {point_A}{point_B}{point_C}, ∠{point_B}{point_A}{point_C}={arg_beta}. Points {point_D}, {point_E}, {point_N} are midpoints of edges {point_P}{point_A}, {point_P}{point_C}, {point_B}{point_C} respectively, {point_M} is the midpoint of segment {point_A}{point_D}, {point_P}{point_A}={point_A}{point_C}={len_a}, {point_A}{point_B}={len_b}. Find the sine value of dihedral angle {point_C}-{point_E}{point_M}-{point_N}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_8_5_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_N}', '{point_M}')"}, ensure_ascii=False) + "\n")
