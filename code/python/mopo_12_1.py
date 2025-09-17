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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math


def calculate(len_a, len_h):
    """计算len_L关于len_a和len_h的表达式"""
    numerator = 4 * len_a
    denominator = len_h
    sqrt_term = math.sqrt(len_h ** 2 + len_a ** 2)
    return (numerator / denominator) * sqrt_term


# 测试示例
len_a = 4.0
len_h = 8.0

# print(calculate(len_a, len_h))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_12_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"在正四棱柱 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 中，底面正方形边长为 ${len_a}$，侧棱长为 ${len_h}$。点 {point_M} 是该正四棱柱表面上的动点，满足 ${point_D}{point_M} \\\\perp {point_B}{point_D1}$，求点 {point_M} 的运动轨迹长度。",
    "en_problem": f"In a right square prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} where the base square has side length ${len_a}$ and lateral edge length ${len_h}$, point {point_M} is a moving point on the surface of the prism satisfying ${point_D}{point_M} \\\\perp {point_B}{point_D1}$. Find the trajectory length of point {point_M}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_12_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_M}')"}, ensure_ascii=False) + "\n")
