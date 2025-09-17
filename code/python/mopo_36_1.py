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
point_A, point_B, point_C, point_D, point_E, point_A_prime, point_P = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_a, len_b):
    """计算len_L关于len_a和len_b的表达式（结果为2*len_b*π/9）"""
    return (2 * len_b * math.pi) / 9


# 测试示例
len_a = 8.0
len_b = 6.0

# print(calculate(len_a, len_b))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)


# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_36_1",
    "type": 8,
    "level": 2,
    "cn_problem": f"在平行四边形 {point_A}{point_B}{point_C}{point_D} 中，{point_E} 为 ${point_A}{point_B}$ 中点，${point_D}{point_E} \\\\perp {point_A}{point_B}$，设 ${point_D}{point_C} = {len_a}$（故 ${point_B}{point_E} = \\\\frac{{len_a}}{2}$），${point_D}{point_E} = {len_b}$。沿 ${point_D}{point_E}$ 将 $\\\\triangle {point_A}{point_D}{point_E}$ 折起至 $\\\\triangle {point_A_prime}{point_D}{point_E}$，使平面 {point_A_prime}{point_D}{point_E} $\\\\perp$ 平面 {point_B}{point_C}{point_D}{point_E}。点 {point_P} 为 $\\\\triangle {point_A_prime}{point_D}{point_E}$ 内的动点，满足 $\\\\angle {point_E}{point_P}{point_B} = \\\\angle {point_D}{point_P}{point_C}$，求点 {point_P} 的轨迹长度。",
    "en_problem": f"In parallelogram {point_A}{point_B}{point_C}{point_D}, {point_E} is the midpoint of ${point_A}{point_B}$, ${point_D}{point_E} \\\\perp {point_A}{point_B}$, let ${point_D}{point_C} = {len_a}$ (so ${point_B}{point_E} = \\\\frac{{len_a}}{2}$), ${point_D}{point_E} = {len_b}$. Fold $\\\\triangle {point_A}{point_D}{point_E}$ along ${point_D}{point_E}$ to $\\\\triangle {point_A_prime}{point_D}{point_E}$ such that plane {point_A_prime}{point_D}{point_E} $\\\\perp$ plane {point_B}{point_C}{point_D}{point_E}. Point {point_P} is a moving point inside $\\\\triangle {point_A_prime}{point_D}{point_E}$ satisfying $\\\\angle {point_E}{point_P}{point_B} = \\\\angle {point_D}{point_P}{point_C}$. Find the length of the trajectory of point {point_P}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_36_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_A_prime}', '{point_P}')"}, ensure_ascii=False) + "\n")
