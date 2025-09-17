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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_G, point_E, point_D, point_F = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math


def calculate(len_a):
    """计算区间[len_d_min, len_d_max)的左右端点（左闭右开）"""
    len_d_min = (len_a * math.sqrt(5)) / 5

    return len_d_min


# 测试示例
len_a = 1.0

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_10_1_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"在直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，$\\\\angle {point_B}{point_A}{point_C} = \\\\frac{{\\\\pi}}{{2}}$，${point_A}{point_B} = {point_A}{point_C} = {point_A}{point_A1} = {len_a}$（${len_a} > 0$）。已知 {point_G} 与 {point_E} 分别为 ${point_A1}{point_B1}$ 和 ${point_C}{point_C1}$ 的中点，{point_D} 与 {point_F} 分别为线段 ${point_A}{point_C}$ 和 ${point_A}{point_B}$ 上的动点（不包括端点），若 ${point_G}{point_D} \\\\perp {point_E}{point_F}$，求线段 ${point_D}{point_F}$ 长度的最小值。",
    "en_problem": f"In a right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} where $\\\\angle {point_B}{point_A}{point_C} = \\\\frac{{\\\\pi}}{{2}}$ and ${point_A}{point_B} = {point_A}{point_C} = {point_A}{point_A1} = {len_a}$ (${len_a} > 0$), let {point_G} and {point_E} be midpoints of ${point_A1}{point_B1}$ and ${point_C}{point_C1}$ respectively. If {point_D} and {point_F} are moving points on segments ${point_A}{point_C}$ and ${point_A}{point_B}$ respectively (excluding endpoints), and ${point_G}{point_D} \\\\perp {point_E}{point_F}$, find the minimum of segment ${point_D}{point_F}$ length.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_10_1_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_G}', '{point_E}', '{point_D}', '{point_F}')"}, ensure_ascii=False) + "\n")
