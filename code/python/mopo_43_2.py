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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_P = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_a, len_b, len_h, arg_theta):
    """计算len_min的值（表达式为√(len_b² + 2len_h² - 2len_h·√(len_b²+len_h²)·cos(arg_theta))）"""
    term1 = len_b ** 2
    term2 = 2 * (len_h ** 2)
    sqrt_inner = math.sqrt(len_b ** 2 + len_h ** 2)
    term3 = 2 * len_h * sqrt_inner * math.cos(arg_theta)
    return math.sqrt(term1 + term2 - term3)


# 测试示例
len_a = math.sqrt(2)
len_b = 2.0
len_h = math.sqrt(2)
arg_theta = math.radians(135)

# print(calculate(len_a, len_b, len_h, arg_theta))

# Generate random lengths
arg_theta = round(len_scaling_factor * float(arg_theta), 2)
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b, len_h, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_43_2",
    "type": 7,
    "level": 2,
    "cn_problem": f"在直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，底面角 $\\\\angle {point_A}{point_C}{point_B} = {arg_theta}$（$90° < {arg_theta} < 180°$，保证 $\\\\cos {arg_theta} < 0$），侧棱 ${point_B}{point_C} = {len_a}$，侧棱高 ${point_C}{point_C1} = {len_h}$。设 ${point_A}{point_C} = {len_b}$，满足垂直条件：${point_A1}{point_C} \\\\perp {point_B1}{point_C}$（推导得 ${len_h}^2 = -{len_a}{len_b} \\\\cos {arg_theta}$）。点 {point_P} 是线段 ${point_B1}{point_C}$ 上的动点，求 ${point_A1}{point_P} + {point_P}{point_C1}$ 的最小值。",
    "en_problem": f"In right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, the base angle $\\\\angle {point_A}{point_C}{point_B} = {arg_theta}$ (where $90° < {arg_theta} < 180°$, ensuring $\\\\cos {arg_theta} < 0$), lateral edge ${point_B}{point_C} = {len_a}$, and lateral height ${point_C}{point_C1} = {len_h}$. Let ${point_A}{point_C} = {len_b}$, satisfying the perpendicular condition: ${point_A1}{point_C} \\\\perp {point_B1}{point_C}$ (which yields ${len_h}^2 = -{len_a}{len_b} \\\\cos {arg_theta}$). Point {point_P} is a moving point on segment ${point_B1}{point_C}$. Find the minimum value of ${point_A1}{point_P} + {point_P}{point_C1}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_43_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_P}')"}, ensure_ascii=False) + "\n")
