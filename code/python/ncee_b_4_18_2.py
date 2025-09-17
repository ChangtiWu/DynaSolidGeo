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
point_A, point_B, point_C, point_D, point_O, point_E, point_F, point_D_prime = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_h, len_d1, len_s, param_p):
    """
    计算给定参数对应的体积V。

    参数:
        len_h (float): 高度参数（如棱锥的高）。
        len_d1 (float): 长度参数（如底面某边长）。
        len_s (float): 基准长度参数（如底面正方形的半对角线长度）。
        param_p (float): 比例参数（影响体积的非线性项）。

    返回:
        float: 计算得到的体积V。
    """
    # 计算根号内的部分：√(4len_s² - len_d1²)
    sqrt_term = math.sqrt(4 * (len_s ** 2) - (len_d1 ** 2))

    # 计算分子部分：len_h * len_d1 * sqrt_term
    numerator = len_h * len_d1 * sqrt_term

    # 计算分母部分：12
    denominator = 12

    # 计算括号内的多项式部分
    ratio = param_p / len_s
    poly_term = 1 + 2 * ratio - (ratio ** 2)

    # 计算最终体积V
    V = (numerator / denominator) * poly_term

    return V


len_h = 2 * math.sqrt(2)
len_d1 = 6.0
len_d2 = 8.0
len_s = 5.0
param_p = 5/4

# V = calculate(len_h, len_d1, len_s, param_p)
# print(f"体积 V = {V:.4f}")
# Generate random lengths
len_s = round(len_scaling_factor * float(len_s), 2)
len_d1 = round(len_scaling_factor * float(len_d1), 2)
len_d2 = round(len_scaling_factor * float(len_d2), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_h, len_d1, len_s, param_p)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_18_2",
    "type": 5,
    "level": 3,
    "cn_problem": f"设菱形 {point_A}{point_B}{point_C}{point_D} 的边长为 {len_s}（{len_s}>0），对角线 {point_A}{point_C}、{point_B}{point_D} 交于点 {point_O}。在边 {point_A}{point_D} 上取点 {point_E}，在边 {point_C}{point_D} 上取点 {point_F}，使 {point_A}{point_E}={point_C}{point_F}={param_p}（0<{param_p}<{len_s}）。记 λ=\\frac{{{param_p}}}{{{len_s}}}∈(0,1)。设 |{point_A}{point_C}|={len_d1}（0<{len_d1}<2*{len_s}），|{point_B}{point_D}|={len_d2}=\\sqrt{{4*{len_s}^2-{len_d1}^2}}。现把 \\triangle {point_D}{point_E}{point_F} 沿 {point_E}{point_F} 折起到空间位置 \\triangle {point_D_prime}{point_E}{point_F}，满足 {point_O}{point_D_prime}={len_h}（{len_h}>0）。求五棱锥 {point_D_prime}-{point_A}{point_B}{point_C}{point_F}{point_E} 的体积 V。",
    "en_problem": f"Given rhombus {point_A}{point_B}{point_C}{point_D} with side length {len_s} ({len_s}>0), where diagonals {point_A}{point_C} and {point_B}{point_D} intersect at point {point_O}. Take point {point_E} on side {point_A}{point_D} and point {point_F} on side {point_C}{point_D} such that {point_A}{point_E}={point_C}{point_F}={param_p} (0<{param_p}<{len_s}). Let λ=\\frac{{{param_p}}}{{{len_s}}}∈(0,1). Set |{point_A}{point_C}|={len_d1} (0<{len_d1}<2*{len_s}) and |{point_B}{point_D}|={len_d2}=\\sqrt{{4*{len_s}^2-{len_d1}^2}}. Now fold triangle \\triangle {point_D}{point_E}{point_F} along {point_E}{point_F} to spatial position \\triangle {point_D_prime}{point_E}{point_F}, satisfying {point_O}{point_D_prime}={len_h} ({len_h}>0). Find the volume V of pentagonal pyramid {point_D_prime}-{point_A}{point_B}{point_C}{point_F}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_18_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}', '{point_E}', '{point_F}', '{point_D_prime}')"}, ensure_ascii=False) + "\n")
