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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_P, point_Q = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math


def calculate(len_S, len_s, len_h, param_k):
    """计算体积V的表达式：V = (len_S²·len_h)/(6·param_k) · √[1 - param_k² - (param_k²·len_h²)/(len_S - len_s)²]（需满足0<param_k<1且len_h<(len_S-len_s)/param_k·√(1-param_k²)）"""
    # 计算分母部分
    denominator = 6 * param_k
    # 计算根号内的分子部分：1 - param_k²
    sqrt_numerator_part = 1 - param_k ** 2
    # 计算根号内的分数部分：(param_k²·len_h²)/(len_S - len_s)²
    sqrt_fraction = (param_k ** 2 * len_h ** 2) / ((len_S - len_s) ** 2)
    # 根号内整体值
    sqrt_inner = sqrt_numerator_part - sqrt_fraction
    # 计算根号项
    sqrt_term = math.sqrt(sqrt_inner)
    # 计算最终体积
    return (len_S ** 2 * len_h / denominator) * sqrt_term


# 测试示例
len_S = 6
len_s = 3
len_h = 6.0
param_k = 3 / 7

# print(calculate(len_S, len_s, len_h, param_k))

# Generate random lengths
len_S = round(len_scaling_factor * float(len_S), 2)
len_s = round(len_scaling_factor * float(len_s), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_S, len_s, len_h, param_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_26_2",
    "type": 5,
    "level": 3,
    "cn_problem": f"如图，已知四棱台 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}，下底 {point_A}{point_B}{point_C}{point_D} 为边长 {len_S}>0 的正方形，上底 {point_A1}{point_B1}{point_C1}{point_D1} 为边长 {len_s}（0<{len_s}<{len_S}）的正方形，侧棱皆垂直于下底，且 {point_A}{point_A1}={point_B}{point_B1}=...={len_h}>0。点 {point_P} 在侧棱 {point_D}{point_D1} 上，点 {point_Q} 在下底棱 {point_B}{point_C} 上；规定 {point_P}{point_Q}∥平面 {point_A}{point_B}{point_B1}{point_A1}，并记 cos(∠二面角({point_P}{point_Q}{point_D},{point_A}{point_D}{point_Q}))={param_k}（0<{param_k}<1）。令四面体 {point_A}{point_D}{point_P}{point_Q} 的体积为volume_V。求 volume_V。",
    "en_problem": f"As shown, given a quadrilateral frustum {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, where the lower base {point_A}{point_B}{point_C}{point_D} is a square with side length {len_S}>0, the upper base {point_A1}{point_B1}{point_C1}{point_D1} is a square with side length {len_s} (0<{len_s}<{len_S}), all lateral edges are perpendicular to the lower base, and {point_A}{point_A1}={point_B}{point_B1}=...={len_h}>0. Point {point_P} is on lateral edge {point_D}{point_D1}, point {point_Q} is on base edge {point_B}{point_C}; given that {point_P}{point_Q}∥plane {point_A}{point_B}{point_B1}{point_A1}, and cos(∠dihedral({point_P}{point_Q}{point_D},{point_A}{point_D}{point_Q}))={param_k} (0<{param_k}<1). Let volume_V be the volume of tetrahedron {point_A}{point_D}{point_P}{point_Q}. Find volume_V.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_26_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_P}', '{point_Q}')"}, ensure_ascii=False) + "\n")
