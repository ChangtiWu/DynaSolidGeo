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
point_A, point_B, point_C, point_C1, point_D, point_A1, point_E, point_M, point_B1, point_N, point_P = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math


def calculate(len_h, len_e, len_a, len_d):
    """
    计算正弦值 sinθ，基于给定的公式：
    sinθ = √[(len_h - len_e)² + len_a²] / √[(len_d - len_e)² + (len_h - len_e)² + len_a²]

    参数:
    len_h (float): 长度参数（代表实际长度）
    len_e (float): 长度参数（代表实际长度）
    len_a (float): 长度参数（代表实际长度）
    len_d (float): 长度参数（代表实际长度）

    返回:
    float: 计算得到的 sinθ 值
    """
    # 计算分子中的平方项：(len_h - len_e)² + len_a²
    numerator_sq = (len_h - len_e) ** 2 + len_a ** 2
    # 计算分子的平方根
    numerator = math.sqrt(numerator_sq)

    # 计算分母中的平方项：(len_d - len_e)² + (len_h - len_e)² + len_a²
    denominator_sq = (len_d - len_e) ** 2 + numerator_sq  # 复用 numerator_sq 简化计算
    # 计算分母的平方根
    denominator = math.sqrt(denominator_sq)

    # 计算 sinθ
    sin_theta = numerator / denominator
    return sin_theta

len_h = 3.0
len_e = 2.0
len_a = 2.0
len_d = 1.0

# result1 = calculate(len_h, len_e, len_a, len_d)
# print(f"当 len_h={len_h}, len_e={len_e}, len_a={len_a}, len_d={len_d} 时，sinθ≈{result1:.4f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)
len_d = round(len_scaling_factor * float(len_d), 2)
len_e = round(len_scaling_factor * float(len_e), 2)

# Calculate the result
result = calculate(len_h, len_e, len_a, len_d)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_10_2",
    "type": 2,
    "level": 3,
    "cn_problem": f"参数化设置：\n- 设底面直角等腰三角形 {point_A}{point_B}{point_C} 满足 {point_A}{point_C} = {point_B}{point_C} = {len_a} (>0)，且 {point_A}{point_C} ⟂ {point_B}{point_C}；\n- 设侧棱 {point_C}{point_C1} ⟂ 底面，长度 {len_h} (>0)；\n- 点 {point_D} 在 {point_A}{point_A1} 上，取 {point_A}{point_D} = {len_d}\\,(0 < {len_d} < {len_h})；\n- 点 {point_E} 在 {point_C}{point_C1} 上，取 {point_C}{point_E} = {len_e}\\,(0 < {len_e} < {len_h})；\n- 点 {point_M} 为 {point_A1}{point_B1} 的中点。\n设 θ 为直线 {point_A}{point_N} (此处 {point_N} 为 {point_P}{point_C} 的中点) 与平面 {point_P}{point_D}{point_M} 所成的锐角，其中 {point_P} = {point_A1}，{point_N} = \\operatorname{{mid}}({point_P},{point_C})。求 sin θ 。",
    "en_problem": f"Parameterised version:\n- Let the base right‑isosceles triangle {point_A}{point_B}{point_C} satisfy {point_A}{point_C} = {point_B}{point_C} = {len_a} (>0) with {point_A}{point_C} ⟂ {point_B}{point_C};\n- The lateral edge {point_C}{point_C1} is perpendicular to the base and has length {len_h} (>0);\n- Point {point_D} lies on {point_A}{point_A1} with {point_A}{point_D} = {len_d}\\,(0 < {len_d} < {len_h});\n- Point {point_E} lies on {point_C}{point_C1} with {point_C}{point_E} = {len_e}\\,(0 < {len_e} < {len_h});\n- Point {point_M} is the midpoint of {point_A1}{point_B1}.\nLet θ denote the acute angle between line {point_A}{point_N} (where {point_N} is the midpoint of {point_P}{point_C} with {point_P} = {point_A1}) and plane {point_P}{point_D}{point_M}. Derive sin θ .",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_10_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_C1}', '{point_D}', '{point_A1}', '{point_E}', '{point_M}', '{point_B1}', '{point_N}', '{point_P}')"}, ensure_ascii=False) + "\n")
