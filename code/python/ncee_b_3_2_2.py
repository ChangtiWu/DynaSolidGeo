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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_N, point_M = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math

def calculate(len_a, len_b, len_c):
    """
    计算余弦值 cos(theta) 的表达式

    参数:
    len_a (float): 长度参数 a
    len_b (float): 长度参数 b
    len_c (float): 长度参数 c

    返回:
    float: cos(theta) 的计算结果
    """
    # 计算分子: len_a² * len_c
    numerator = len_a ** 2 * len_c

    # 计算分母中的第一部分: [len_b² + (len_a - len_b)²]
    part1 = len_b ** 2 + (len_a - len_b) ** 2

    # 计算分母中的内嵌表达式: len_b² + (len_a + len_b)²
    inner_expr = len_b ** 2 + (len_a + len_b) ** 2

    # 计算分母中的第二部分: [4·len_b⁴ + len_c²·inner_expr]
    part2 = 4 * len_b ** 4 + len_c ** 2 * inner_expr

    # 计算整个分母: sqrt(part1 * part2)
    denominator = math.sqrt(part1 * part2)

    # 返回分子除以分母的结果
    return numerator / denominator

# 示例调用
len_a = 2.0
len_b = 1.0
len_c = 2.0

# cos_theta = calculate(len_a, len_b, len_c)
# print(f"cos(theta) = {cos_theta:.6f}")
#
# # 验证结果范围 (余弦值应在 -1 到 1 之间)
# if abs(cos_theta) > 1:
#     print("注意：计算结果超出余弦值定义域 [-1, 1]")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_3_2_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"如图，在四棱柱 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 中，底面 {point_A}{point_B}{point_C}{point_D} 为梯形，满足 {point_A}{point_B}∥{point_C}{point_D}，{point_A}{point_D} ⟂ {point_A}{point_B}，且 {point_A}{point_A1} ⟂ 平面 {point_A}{point_B}{point_C}{point_D}。\n已知 {point_A}{point_B} = {len_a}，{point_A}{point_D} = {point_C}{point_D} = {len_b}，{point_A}{point_A1} = {len_c}（{len_a},{len_b},{len_c} > 0）。\n设 {point_N} 为 {point_B}{point_C1} 的中点，{point_M} 为 {point_D}{point_D1} 的中点。\n设两平面\n\\[\\Pi_1 = {point_C}{point_B1}{point_M}, \\qquad \\Pi_2 = {point_B}{point_B1}{point_C}\\]\n所成锐二面角为 θ，求 \\(\\cos\\theta\\)。",
    "en_problem": f"In the prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, the base {point_A}{point_B}{point_C}{point_D} is a trapezoid with {point_A}{point_B} ∥ {point_C}{point_D}, {point_A}{point_D} ⟂ {point_A}{point_B}, and {point_A}{point_A1} ⟂ plane {point_A}{point_B}{point_C}{point_D}.\nGiven {point_A}{point_B} = {len_a}, {point_A}{point_D} = {point_C}{point_D} = {len_b}, {point_A}{point_A1} = {len_c} (all positive).\nLet {point_N} be the midpoint of {point_B}{point_C1} and {point_M} the midpoint of {point_D}{point_D1}.\nLet \\(\\Pi_1 = {point_C}{point_B1}{point_M}\\) and \\(\\Pi_2 = {point_B}{point_B1}{point_C}\\). Find \\(\\cos\\theta\\), where θ is the acute dihedral angle between the two planes.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_3_2_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_N}', '{point_M}')"}, ensure_ascii=False) + "\n")
