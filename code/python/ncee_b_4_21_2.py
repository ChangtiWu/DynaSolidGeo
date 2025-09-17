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
point_P, point_A, point_B, point_C, point_D, point_M, point_N = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_a, len_p):
    """计算体积V的表达式：V = (len_p²·√(4len_a² - len_p²)) / 24（要求len_p < 2len_a）"""
    # 计算根号内的部分
    sqrt_term = math.sqrt(4 * (len_a ** 2) - (len_p ** 2))
    # 计算分子部分
    numerator = (len_p ** 2) * sqrt_term
    # 返回最终结果
    return numerator / 24


# 测试示例
len_a = 3.0
len_p = 4.0

# print(calculate(len_a, len_p))

# Generate random lengths
len_p = round(len_scaling_factor * float(len_p), 2)
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, len_p)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_21_2",
    "type": 5,
    "level": 3,
    "cn_problem": f"如图，在四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 中，{point_P}{point_A}⊥平面 {point_A}{point_B}{point_C}{point_D}，且 {point_P}{point_A}={len_p}>0；底面满足 {point_A}{point_D}∥{point_B}{point_C}，{point_A}{point_B}={point_A}{point_C}={point_A}{point_D}={len_a}>0，{point_B}{point_C}={len_p}；点 {point_M} 在 {point_A}{point_D} 上，使 {point_A}{point_M}:{point_M}{point_D}=2:1；点 {point_N} 为棱 {point_P}{point_C} 的中点。设四面体 {point_N}-{point_B}{point_C}{point_M} 的体积为 volume_V。求 volume_V。",
    "en_problem": f"As shown, in quadrilateral pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, {point_P}{point_A}⊥plane {point_A}{point_B}{point_C}{point_D} with {point_P}{point_A}={len_p}>0; the base satisfies {point_A}{point_D}∥{point_B}{point_C}, {point_A}{point_B}={point_A}{point_C}={point_A}{point_D}={len_a}>0, {point_B}{point_C}={len_p}; point {point_M} is on {point_A}{point_D} such that {point_A}{point_M}:{point_M}{point_D}=2:1; point {point_N} is the midpoint of edge {point_P}{point_C}. Let volume_V be the volume of tetrahedron {point_N}-{point_B}{point_C}{point_M}. Find volume_V.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_21_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
