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
def calculate(len_a, len_b):
    """计算len_d_min关于len_a和len_b的表达式（结果等于len_a）"""
    return len_a


# 测试示例
len_a = 1.0
len_b = 2.0

# print(calculate(len_a, len_b))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_17_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"在长方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 中，棱长 ${point_A}{point_B} = {point_B}{point_C} = {len_a}$，${point_A}{point_A1} = {len_b}$。点 {point_P} 为线段 ${point_A}{point_B1}$ 的中点，{point_M}、{point_N} 分别为体对角线 ${point_A}{point_C1}$ 和棱 ${point_C1}{point_D1}$ 上任意一点，求 ${point_P}{point_M} + \\\\frac{{1}}{{\\\\sqrt{{{len_a}^2 + {len_b}^2}}}} \\\\cdot {point_M}{point_N}$ 的最小值。",
    "en_problem": f"In a rectangular parallelepiped {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} where edge lengths ${point_A}{point_B} = {point_B}{point_C} = {len_a}$ and ${point_A}{point_A1} = {len_b}$, point {point_P} is the midpoint of segment ${point_A}{point_B1}$, and {point_M}, {point_N} are arbitrary points on space diagonal ${point_A}{point_C1}$ and edge ${point_C1}{point_D1}$ respectively. Find the minimum value of ${point_P}{point_M} + \\\\frac{{1}}{{\\\\sqrt{{{len_a}^2 + {len_b}^2}}}} \\\\cdot {point_M}{point_N}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_17_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_P}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
