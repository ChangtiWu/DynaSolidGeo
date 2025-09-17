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
point_P, point_A, point_B, point_C, point_D, point_M = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_a, len_b):
    """计算sin(theta)的值（公式：2*len_a*√(4len_b² - len_a²) / √[(8len_b² - len_a²)(3len_a² + len_b²)]）"""
    numerator_part = 2 * len_a * math.sqrt(4 * (len_b ** 2) - len_a ** 2)
    denominator_part = math.sqrt((8 * (len_b ** 2) - len_a ** 2) * (3 * (len_a ** 2) + len_b ** 2))
    return numerator_part / denominator_part


# 测试示例
len_a = 4.0
len_b = math.sqrt(6)

# print(calculate(len_a, len_b))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_24_3",
    "type": 2,
    "level": 2,
    "cn_problem": f"在四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}中，底面{point_A}{point_B}{point_C}{point_D}为正方形，边长为{len_a}，平面{point_P}{point_A}{point_D}⊥平面{point_A}{point_B}{point_C}{point_D}，{point_P}{point_A}={point_P}{point_D}={len_b}。点{point_M}为线段{point_P}{point_B}的中点，求直线{point_M}{point_C}与平面{point_B}{point_D}{point_P}所成角的正弦值。",
    "en_problem": f"In pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, the base {point_A}{point_B}{point_C}{point_D} is a square with side length {len_a}, plane {point_P}{point_A}{point_D}⊥plane {point_A}{point_B}{point_C}{point_D}, and {point_P}{point_A}={point_P}{point_D}={len_b}. Point {point_M} is the midpoint of segment {point_P}{point_B}. Find the sine of the angle between line {point_M}{point_C} and plane {point_B}{point_D}{point_P}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_24_3({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}')"}, ensure_ascii=False) + "\n")
