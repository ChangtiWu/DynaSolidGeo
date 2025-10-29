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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_F = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math


def calculate(len_s: float, len_p: float, len_q: float) -> float:
    """计算长度 len_d 的表达式值（公式：len_d = [len_s·|len_p(1-len_q)-1|] / √(len_q² + (1-len_p)²(1+len_q²))）"""
    numerator = len_s * abs(len_p * (1 - len_q) - 1)
    denominator = math.sqrt(len_q ** 2 + (1 - len_p) ** 2 * (1 + len_q ** 2))
    return numerator / denominator


len_s = 1.0
len_p = 0.5
len_q = 0.5

# result = calculate(len_s, len_p, len_q)
# print(f"len_d = {result:.6f}")

# Generate random lengths
len_s = round(len_scaling_factor * float(len_s), 2)
len_p = round(len_scaling_factor * float(len_p), 2)
len_q = round(len_scaling_factor * float(len_q), 2)

# Calculate the result
result = calculate(len_s, len_p, len_q)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_5_4",
    "type": 3,
    "level": 2,
    "cn_problem": f"在正方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 中，设棱长为 ${len_s}>0$。令 {point_E} $\\in$ {point_A}{point_B}，$\\frac{{ {point_A}{point_E} }}{{ {point_E}{point_B} }}={len_p}:(1-{len_p})$，$0<{len_p}<1$，{point_F} $\\in$ {point_B}{point_C}，$\\frac{{ {point_B}{point_F} }}{{ {point_F}{point_C} }}={len_q}:(1-{len_q})$，$0<{len_q}<1$。求点 {point_D} 到平面 $\\pi={point_B1}{point_E}{point_F}$ 的距离。",
    "en_problem": f"In a cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} with edge length ${len_s}>0$, let {point_E} $\\in$ {point_A}{point_B} with $\\frac{{ {point_A}{point_E} }}{{ {point_E}{point_B} }}={len_p}:(1-{len_p})$, $0<{len_p}<1$, and {point_F} $\\in$ {point_B}{point_C} with $\\frac{{ {point_B}{point_F} }}{{ {point_F}{point_C} }}={len_q}:(1-{len_q})$, $0<{len_q}<1$. Find the distance from point {point_D} to plane $\\pi={point_B1}{point_E}{point_F}$.",
    "solution": f"{result}",
    "image": f"images/{os.path.splitext(os.path.basename(__file__))[0]}.png"
}

# video mode
if args.mode == 1:
    json_data["image"] = f"videos/{os.path.splitext(os.path.basename(__file__))[0]}.mp4"



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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_5_4({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
