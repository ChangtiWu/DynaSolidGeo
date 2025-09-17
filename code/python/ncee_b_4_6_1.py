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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_E, point_F = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
def calculate(len_a):
    """
    计算体积 V_{point_F-point_E point_B point_C}

    参数:
        len_a (float): 长度参数 a

    返回:
        float: 体积计算结果

    公式:
        V = len_a³ / 24
    """
    return (len_a ** 3) / 24

# 当边长为 2 时的体积计算
len_a = 2.0
# volume = calculate(len_a)
#
# print(f"体积 V = {volume:.6f}")

# Generate random lengths

len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_6_1",
    "type": 5,
    "level": 1,
    "cn_problem": f"在直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，侧面 {point_A}{point_A1}{point_B1}{point_B} 为正方形，即 {point_A}{point_B}={point_A}{point_A1}={point_B}{point_B1}={point_A}{point_B1}={len_a}，且 {point_A}{point_A1}⊥{point_A}{point_B}。底面满足 {point_A}{point_B}={point_B}{point_C}={len_a}（{len_a}>0）。设 {point_E}、{point_F} 分别是线段 {point_A}{point_C} 与 {point_C1}{point_C} 的中点，且 {point_B}{point_F}⊥{point_A1}{point_B1}。求三棱锥 {point_F}-{point_E}{point_B}{point_C} 的体积。",
    "en_problem": f"In the right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, the lateral face {point_A}{point_A1}{point_B1}{point_B} is a square, i.e., {point_A}{point_B}={point_A}{point_A1}={point_B}{point_B1}={point_A}{point_B1}={len_a} with {point_A}{point_A1}⊥{point_A}{point_B}. The base satisfies {point_A}{point_B}={point_B}{point_C}={len_a} (where {len_a}>0). Let {point_E} and {point_F} be the midpoints of segments {point_A}{point_C} and {point_C1}{point_C} respectively, with {point_B}{point_F}⊥{point_A1}{point_B1}. Find the volume of triangular pyramid {point_F}-{point_E}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_6_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
