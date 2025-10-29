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


def calculate(len_a, len_b, len_h):
    """计算距离d的值（表达式为分子2len_b²len_h除以分母平方根）"""
    numerator = 2 * (len_b ** 2) * len_h
    denominator_sq = 4 * (len_b ** 4) + (len_b ** 2) * (len_h ** 2) + (len_h ** 2) * (len_a + len_b) ** 2
    denominator = math.sqrt(denominator_sq)
    return numerator / denominator


# 测试示例
len_a = 2.0
len_b = 1.0
len_h = 2.0

# print(calculate(len_a, len_b, len_h))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_b, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_3_2_3",
    "type": 3,
    "level": 2,
    "cn_problem": f"如图，已知四棱柱 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 中，底面 {point_A}{point_B}{point_C}{point_D} 为梯形，{point_A}{point_B}∥{point_C}{point_D}，{point_A1}{point_A}⊥平面 {point_A}{point_B}{point_C}{point_D}，{point_A}{point_D}⊥{point_A}{point_B}，其中 {point_A}{point_B}={len_a}>0，{point_A}{point_D}={point_D}{point_C}={len_b}>0，{point_A}{point_A1}={len_h}>0。{point_N} 是 {point_B1}{point_C1} 的中点，{point_M} 是 {point_D}{point_D1} 的中点。求点 {point_B} 到平面 {point_C}{point_B1}{point_M} 的距离 d。",
    "en_problem": f"As shown, given a quadrilateral prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} where the base {point_A}{point_B}{point_C}{point_D} is a trapezoid with {point_A}{point_B}∥{point_C}{point_D}, {point_A1}{point_A}⊥plane {point_A}{point_B}{point_C}{point_D}, {point_A}{point_D}⊥{point_A}{point_B}. Given {point_A}{point_B}={len_a}>0, {point_A}{point_D}={point_D}{point_C}={len_b}>0, {point_A}{point_A1}={len_h}>0. {point_N} is the midpoint of {point_B1}{point_C1}, {point_M} is the midpoint of {point_D}{point_D1}. Find the distance d from point {point_B} to plane {point_C}{point_B1}{point_M}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_3_2_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_N}', '{point_M}')"}, ensure_ascii=False) + "\n")
