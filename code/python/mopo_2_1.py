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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_P, point_M, point_N = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math


def calculate(len_a, len_b, len_c):
    """计算函数f(len_a, len_b, len_c) = (len_b² + 2len_c²) / √[(len_b² + len_c²)(len_b² + 4len_c²)]"""
    numerator = len_b ** 2 + 2 * len_c ** 2
    denominator = math.sqrt((len_b ** 2 + len_c ** 2) * (len_b ** 2 + 4 * len_c ** 2))
    return numerator / denominator


# 测试示例
len_a = 3.0
len_b = 2.0
len_c = 2.0

# print(calculate(len_a, len_b, len_c))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_2_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"在长方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 中，设 ${point_A}{point_B} = {len_a}$，${point_B}{point_C} = {len_b}$，${point_C}{point_C1} = {len_c}$。点 {point_P} 在矩形 ${point_B}{point_C}{point_C1}{point_B1}$ 内运动（包括边界），{point_M}、{point_N} 分别为 ${point_B}{point_C}$、${point_C}{point_C1}$ 的中点。若 ${point_A1}{point_P} \\\\parallel$ 平面 ${point_M}{point_A}{point_N}$，当 ${point_A1}{point_P}$ 取得最小值时，求 $\\\\angle {point_B1}{point_B}{point_P}$ 的余弦值。",
    "en_problem": f"In a rectangular parallelepiped {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, let ${point_A}{point_B} = {len_a}$, ${point_B}{point_C} = {len_b}$, ${point_C}{point_C1} = {len_c}$. Point {point_P} moves within rectangle ${point_B}{point_C}{point_C1}{point_B1}$ (including boundary), and {point_M}, {point_N} are midpoints of ${point_B}{point_C}$ and ${point_C}{point_C1}$ respectively. If ${point_A1}{point_P} \\\\parallel$ plane ${point_M}{point_A}{point_N}$, when ${point_A1}{point_P}$ attains its minimum value, find the cosine value of $\\\\angle {point_B1}{point_B}{point_P}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_2_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_P}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
