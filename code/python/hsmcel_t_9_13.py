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
point_A, point_B, point_C, point_D, point_M, point_N = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算正四面体 ABCD 中，过 MN 的平面截得的最小截面面积

    参数:
    len_a (float): 棱长

    返回:
    float: 最小截面面积
    """
    return (1 / 4) * len_a**2


# 题干给定的数值
len_a = 1.0  # 正四面体棱长

# 验证输出
# area_min = calculate(len_a)
# print(f"最小截面面积: {area_min:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_9_13",
    "type": 4,
    "level": 2,
    "cn_problem": f"在棱长为{len_a}的正四面体{point_A}{point_B}{point_C}{point_D}中，{point_M}、{point_N}分别为棱{point_A}{point_D}、{point_B}{point_C}的中点，过{point_M}{point_N}的平面被此四面体所截得截面面积的最小值为多少？",
    "en_problem": f"In a regular tetrahedron {point_A}{point_B}{point_C}{point_D} with edge length {len_a}, {point_M} and {point_N} are the midpoints of edges {point_A}{point_D} and {point_B}{point_C} respectively. What is the minimum area of the cross-section formed when a plane passing through {point_M}{point_N} intersects the tetrahedron?",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_9_13({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
