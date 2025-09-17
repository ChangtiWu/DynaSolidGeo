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
point_A, point_B, point_C, point_P, point_Q, point_O = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(arg_alpha, arg_beta):
    """计算tan(α+β)和tanα·tanβ的值"""
    tan_sum = math.tan(arg_alpha + arg_beta)
    tan_prod = math.tan(arg_alpha) * math.tan(arg_beta)
    return tan_prod


# 测试示例
len_R = 3.0
len_a = 3 * (3**0.5)
arg_alpha = math.atan(-2)
arg_beta = math.atan(-2)

# print(calculate(arg_alpha, arg_beta))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_R = round(len_scaling_factor * float(len_R), 2)

# Calculate the result
result = calculate(arg_alpha, arg_beta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_8_6",
    "type": 2,
    "level": 3,
    "cn_problem": f"已知底面为正三角形 $\\triangle {point_A}{point_B}{point_C}$，其边长为 ${len_a}=3\\sqrt{3}$。以 ${point_A}{point_B}{point_C}$ 为公共底面，在其两侧分别构造两个正三棱锥 ${point_P}$-${point_A}{point_B}{point_C}$ 和 ${point_Q}$-${point_A}{point_B}{point_C}$，并使这两个三棱锥与同一球面 $({point_O},{len_R})$ 外切；换言之，点 ${point_P},{point_Q},{point_A},{point_B},{point_C}$ 均位于以 {point_O} 为球心、以 ${len_R}=3$ 为半径的球面上。设侧棱 ${point_P}{point_A}$ 与底面 ${point_A}{point_B}{point_C}$ 的夹角为 ${arg_alpha}$，侧棱 ${point_Q}{point_A}$ 与底面的夹角为 ${arg_beta}$。求 $\\tan({arg_alpha})\\cdot\\tan({arg_beta})$ 的值。",
    "en_problem": f"Given an equilateral triangle $\\triangle {point_A}{point_B}{point_C}$ with side length ${len_a}=3\\sqrt{3}$ as the base. Construct two regular triangular pyramids ${point_P}$-${point_A}{point_B}{point_C}$ and ${point_Q}$-${point_A}{point_B}{point_C}$ on opposite sides of the common base ${point_A}{point_B}{point_C}$, such that both pyramids are inscribed in the same sphere $({point_O},{len_R})$. In other words, points ${point_P},{point_Q},{point_A},{point_B},{point_C}$ all lie on the sphere with center {point_O} and radius ${len_R}=3$. Let the angle between lateral edge ${point_P}{point_A}$ and base plane ${point_A}{point_B}{point_C}$ be ${arg_alpha}$, and the angle between lateral edge ${point_Q}{point_A}$ and the base plane be ${arg_beta}$. Find the value of $\\tan({arg_alpha})\\cdot\\tan({arg_beta})$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_8_6({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_P}', '{point_Q}', '{point_O}')"}, ensure_ascii=False) + "\n")
