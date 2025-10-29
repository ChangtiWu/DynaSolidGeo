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
point_A, point_B, point_C, point_D, point_E, point_P = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_edge):
    """
    计算给定的几何表达式（四棱锥 P-BCED 的表面积）

    参数:
    len_edge (float): 正三角形的边长

    返回:
    float: 计算结果
    """
    return ((2 + math.sqrt(3)) / 4) * (len_edge ** 2)


# 定义题干中的变量
len_edge = 4

# result = calculate(len_edge)
# print(f"计算结果: {result:.6f}")

 
# Generate random lengths
len_edge = round(len_scaling_factor * float(len_edge), 2)

# Calculate the result
result = calculate(len_edge)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area1_18_2",
    "type": 4,
    "level": 2,
    "cn_problem": f"已知正三角形 {point_A}{point_B}{point_C} 的边长为 {len_edge}，{point_D}、{point_E} 分别为线段 {point_A}{point_B}、{point_A}{point_C} 的中点，连接 {point_B}{point_E}，将三角形 {point_A}{point_D}{point_E} 沿 {point_D}{point_E} 翻折成四棱锥 {point_P} - {point_B}{point_C}{point_E}{point_D}，使得点 {point_P} 在底面 {point_B}{point_C}{point_E}{point_D} 上的射影在线段 {point_B}{point_E} 上，求四棱锥 {point_P} - {point_B}{point_C}{point_E}{point_D} 的表面积。",
    "en_problem": f"Given an equilateral triangle {point_A}{point_B}{point_C} with side length {len_edge}, where {point_D} and {point_E} are midpoints of segments {point_A}{point_B} and {point_A}{point_C} respectively, connect {point_B}{point_E}, and fold triangle {point_A}{point_D}{point_E} along {point_D}{point_E} to form pyramid {point_P} - {point_B}{point_C}{point_E}{point_D}, such that the projection of point {point_P} on base {point_B}{point_C}{point_E}{point_D} lies on segment {point_B}{point_E}. Find the surface area of pyramid {point_P} - {point_B}{point_C}{point_E}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"area1_18_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_P}')"}, ensure_ascii=False) + "\n")
