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
point_A, point_B, point_C, point_P, point_D = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_a, arg_theta):
    """计算最大体积（公式：$volume\_max = \frac{len\_a^3 \cdot \cos(\frac{arg\_theta}{2}) \cdot \sin^2(\frac{arg\_theta}{2})}{6}$）"""
    theta_half = arg_theta / 2
    cos_term = math.cos(theta_half)
    sin_sq_term = math.sin(theta_half) ** 2
    numerator = (len_a ** 3) * cos_term * sin_sq_term
    return numerator / 6


# 测试示例
len_a = 2.0
arg_theta = math.pi / 3 * 2

# print(calculate(len_a, arg_theta))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_s1_2_28_1",
    "type": 5,
    "level": 2,
    "cn_problem": f"在△{point_A}{point_B}{point_C}中，设{point_A}{point_B}={point_B}{point_C}={len_a}，∠{point_A}{point_B}{point_C}={arg_theta}（0<{arg_theta}<π）。平面{point_A}{point_B}{point_C}外的点{point_P}和线段{point_A}{point_C}上的点{point_D}满足{point_P}{point_D}={point_D}{point_A}，{point_P}{point_B}={point_B}{point_A}={len_a}。求四面体{point_P}{point_B}{point_C}{point_D}的体积的最大值。",
    "en_problem": f"In triangle {point_A}{point_B}{point_C}, let {point_A}{point_B}={point_B}{point_C}={len_a}, and ∠{point_A}{point_B}{point_C}={arg_theta} (0<{arg_theta}<π). Point {point_P} outside plane {point_A}{point_B}{point_C} and point {point_D} on segment {point_A}{point_C} satisfy {point_P}{point_D}={point_D}{point_A} and {point_P}{point_B}={point_B}{point_A}={len_a}. Find the maximum volume of tetrahedron {point_P}{point_B}{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_s1_2_28_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_P}', '{point_D}')"}, ensure_ascii=False) + "\n")
