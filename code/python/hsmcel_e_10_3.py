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
point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_a, len_b, len_c):
    """计算共体积V的表达式"""
    numerator = math.sqrt(3) * (len_b ** 3)
    denominator = 12 * (len_a + len_b) * (len_b + len_c)
    return numerator / denominator


# 测试示例
len_a = 1
len_b = 2
len_c = 3

# print(calculate(len_a, len_b, len_c))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_10_3",
    "type": 5,
    "level": 3,
    "cn_problem": f"设底面 $\\triangle {point_A}{point_B}{point_C}$ 为边长 $1$ 的正三角形。过三个顶点向底面所作的高分别取点 ${point_D} \\in {point_A} \\perp {point_A}{point_B}{point_C}$，${point_E} \\in {point_B} \\perp {point_A}{point_B}{point_C}$，${point_F} \\in {point_C} \\perp {point_A}{point_B}{point_C}$，使 $|{point_A}{point_D}| = {len_a}$，$|{point_B}{point_E}| = {len_b}$，$|{point_C}{point_F}| = {len_c}$（${len_a}, {len_b}, {len_c} > 0$）。求四面体 ${point_E}{point_A}{point_B}{point_C}$ 与四面体 ${point_B}{point_D}{point_E}{point_F}$ 的公共部分体积。",
    "en_problem": f"Let the base $\\triangle {point_A}{point_B}{point_C}$ be an equilateral triangle with side length $1$. Through the three vertices, construct perpendiculars to the base and take points ${point_D} \\in {point_A} \\perp {point_A}{point_B}{point_C}$, ${point_E} \\in {point_B} \\perp {point_A}{point_B}{point_C}$, ${point_F} \\in {point_C} \\perp {point_A}{point_B}{point_C}$ such that $|{point_A}{point_D}| = {len_a}$, $|{point_B}{point_E}| = {len_b}$, $|{point_C}{point_F}| = {len_c}$ (${len_a}, {len_b}, {len_c} > 0$). Find the volume of the common part of tetrahedron ${point_E}{point_A}{point_B}{point_C}$ and tetrahedron ${point_B}{point_D}{point_E}{point_F}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_10_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
