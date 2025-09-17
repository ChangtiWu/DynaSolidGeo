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
point_A, point_B, point_C, point_D, point_M, point_N = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
def calculate(len_a, len_b):
    """计算表达式 [2*(2len_a² - len_b²)] / (4len_a² - len_b²) 的值"""
    numerator = 2 * (2 * len_a ** 2 - len_b ** 2)
    denominator = 4 * len_a ** 2 - len_b ** 2
    return numerator / denominator


# 测试示例
len_a = 3.0
len_b = 2.0

# print(calculate(len_a, len_b))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_s2_1_6_1",
    "type": 2,
    "level": 1,
    "cn_problem": f"三棱锥{point_A}-{point_B}{point_C}{point_D}中，{point_A}{point_B}={point_A}{point_C}={point_B}{point_D}={point_C}{point_D}={len_a}，{point_A}{point_D}={point_B}{point_C}={len_b}，点{point_M}、{point_N}分别是{point_A}{point_D}、{point_B}{point_C}的中点，求异面直线{point_A}{point_N}与{point_C}{point_M}所成角的余弦值。",
    "en_problem": f"In triangular pyramid {point_A}-{point_B}{point_C}{point_D}, {point_A}{point_B}={point_A}{point_C}={point_B}{point_D}={point_C}{point_D}={len_a}, {point_A}{point_D}={point_B}{point_C}={len_b}, points {point_M} and {point_N} are the midpoints of {point_A}{point_D} and {point_B}{point_C} respectively. Find the cosine of the angle between skew lines {point_A}{point_N} and {point_C}{point_M}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_s2_1_6_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
