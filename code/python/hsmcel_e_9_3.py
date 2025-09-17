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
point_V, point_A, point_B, point_C, point_O, point_M, point_E, point_F, point_G, point_H = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
def calculate(len_a, len_b):
    """计算四边形EFGH的面积"""
    numerator = 2 * len_a * (len_b ** 2) * (3 * len_a + len_b)
    denominator = 9 * (len_a + len_b) ** 2
    return numerator / denominator


# 测试示例
len_a = 2
len_b = 3

# print(calculate(len_a, len_b))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_9_3",
    "type": 4,
    "level": 3,
    "cn_problem": f"在正三棱锥 ${point_V}$-${point_A}{point_B}{point_C}$ 中，底面 $\\triangle {point_A}{point_B}{point_C}$ 为边长为 ${len_a}>0$ 的正三角形；三条侧棱等长：$|{point_V}{point_A}|=|{point_V}{point_B}|=|{point_V}{point_C}|={len_b}>0$。设 ${point_O}$ 为底面 $\\triangle {point_A}{point_B}{point_C}$ 的中心，${point_V}{point_O}$ 为棱锥高。在高 ${point_V}{point_O}$ 上取点 ${point_M}$，使 $\\frac{{{point_V}{point_M}}}{{{point_M}{point_O}}}=\\frac{{len_b}}{{len_a}}$。过 ${point_M}$ 作平面 $\\pi$，要求 $\\pi \\parallel {point_V}{point_A}$，$\\pi \\parallel {point_B}{point_C}$。记 $\\pi$ 与棱锥所截得的截面为矩形 ${point_E}{point_F}{point_G}{point_H}$。求 $area_S_{{{point_E}{point_F}{point_G}{point_H}}}$。",
    "en_problem": f"In a regular triangular pyramid ${point_V}$-${point_A}{point_B}{point_C}$, the base $\\triangle {point_A}{point_B}{point_C}$ is an equilateral triangle with side length ${len_a}>0$; the three lateral edges are equal in length: $|{point_V}{point_A}|=|{point_V}{point_B}|=|{point_V}{point_C}|={len_b}>0$. Let ${point_O}$ be the center of the base $\\triangle {point_A}{point_B}{point_C}$, and ${point_V}{point_O}$ be the height of the pyramid. On the height ${point_V}{point_O}$, take point ${point_M}$ such that $\\frac{{{point_V}{point_M}}}{{{point_M}{point_O}}}=\\frac{{len_b}}{{len_a}}$. Through ${point_M}$, construct a plane $\\pi$ such that $\\pi \\parallel {point_V}{point_A}$ and $\\pi \\parallel {point_B}{point_C}$. Let the cross-section formed by the intersection of $\\pi$ and the pyramid be rectangle ${point_E}{point_F}{point_G}{point_H}$. Find $area_S_{{{point_E}{point_F}{point_G}{point_H}}}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_9_3({mode}, {azimuth}, {elevation}, '{point_V}', '{point_A}', '{point_B}', '{point_C}', '{point_O}', '{point_M}', '{point_E}', '{point_F}', '{point_G}', '{point_H}')"}, ensure_ascii=False) + "\n")
