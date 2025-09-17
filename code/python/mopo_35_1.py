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
point_A, point_A1, point_B1, point_C1, point_P, point_M, point_N = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_a, len_b, len_h):
    """计算f_min关于len_a、len_b、len_h的表达式（结果为len_b乘以√(len_a²+len_h²)）"""
    return len_b * math.sqrt(len_a ** 2 + len_h ** 2)


# 测试示例
len_a = 2.0
len_b = 1.0
len_h = 1.0

# print(calculate(len_a, len_b, len_h))

# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_35_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"在三棱锥 {point_A}-{point_A1}{point_B1}{point_C1} 中，${point_A}{point_A1} \\\\perp$ 平面 {point_A1}{point_B1}{point_C1}，$\\\\angle {point_A1}{point_B1}{point_C1} = 90°$。设 ${point_A}{point_A1} = {len_h}$，${point_A1}{point_B1} = {len_a}$，${point_B1}{point_C1} = {len_b}$（其中 ${len_a}, {len_b}, {len_h} > 0$）。{point_P} 为线段 ${point_A}{point_B1}$ 的中点，{point_M}、{point_N} 分别为线段 ${point_A}{point_C1}$ 和 ${point_B1}{point_C1}$ 上的任意一点，求 $\\\\sqrt{{{len_a}^2+{len_h}^2}} \\\\cdot {point_P}{point_M} + {point_M}{point_N}$ 的最小值。",
    "en_problem": f"In tetrahedron {point_A}-{point_A1}{point_B1}{point_C1}, ${point_A}{point_A1} \\\\perp$ plane {point_A1}{point_B1}{point_C1}, and $\\\\angle {point_A1}{point_B1}{point_C1} = 90°$. Let ${point_A}{point_A1} = {len_h}$, ${point_A1}{point_B1} = {len_a}$, ${point_B1}{point_C1} = {len_b}$ (where ${len_a}, {len_b}, {len_h} > 0$). {point_P} is the midpoint of segment ${point_A}{point_B1}$, and {point_M}, {point_N} are arbitrary points on segments ${point_A}{point_C1}$ and ${point_B1}{point_C1}$ respectively. Find the minimum value of $\\\\sqrt{{{len_a}^2+{len_h}^2}} \\\\cdot {point_P}{point_M} + {point_M}{point_N}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_35_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_P}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
