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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_M, point_N = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math


def calculate(len_a, len_h, ang_theta):
    """
    计算距离 d 的表达式

    参数:
    len_a (float): 长度参数 a
    len_h (float): 高度参数 h
    ang_theta (float): 角度 theta（弧度）

    返回:
    float: 计算结果 d
    """
    # 计算分子: len_a * len_h * sin(ang_theta)
    numerator = len_a * len_h * math.sin(ang_theta)

    # 计算分母中的各项
    sin_sq = math.sin(ang_theta) ** 2  # sin²(ang_theta)
    cos_term = math.cos(ang_theta)  # cos(ang_theta)

    # 分母: sqrt(len_a² * sin²(ang_theta) + len_h² * (5 - 4*cos(ang_theta)))
    denominator = math.sqrt(
        (len_a ** 2) * sin_sq +
        (len_h ** 2) * (5 - 4 * cos_term)
    )

    # 返回分子除以分母的结果
    return numerator / denominator

len_a = 2.0
len_h = 4.0
ang_theta = math.pi / 3  # 60度，约1.0472弧度

#
# d = calculate(len_a, len_h, ang_theta)
# print(f"计算结果 d = {d:.6f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h, ang_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_3_6_2",
    "type": 3,
    "level": 2,
    "cn_problem": f"直四棱柱 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 的底面 {point_A}{point_B}{point_C}{point_D} 为菱形，满足\n{point_A}{point_B} = {point_A}{point_D} = {len_a}，∠{point_A}{point_B}{point_D} = {ang_theta}，侧棱 {point_A}{point_A1} = {len_h}，且 {point_A}{point_A1} ⟂ 底面。\n设 {point_E} 为 {point_B}{point_C} 的中点，{point_M} 为 {point_B}{point_B1} 的中点，{point_N} 为 {point_A1}{point_D} 的中点。\n求点 {point_C} 到平面 {point_C1}{point_D}{point_E} 的距离。",
    "en_problem": f"In the right prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, the base {point_A}{point_B}{point_C}{point_D} is a rhombus with {point_A}{point_B} = {point_A}{point_D} = {len_a} and ∠{point_B}{point_A}{point_D} = {ang_theta} (0 < {ang_theta} < π). The lateral edge {point_A}{point_A1} is perpendicular to the base and has length {len_h}.\nLet {point_E} be the midpoint of {point_B}{point_C}, {point_M} the midpoint of {point_B}{point_B1}, and {point_N} the midpoint of {point_A1}{point_D}.\nFind the distance from {point_C} to the plane {point_C1}{point_D}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_3_6_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
