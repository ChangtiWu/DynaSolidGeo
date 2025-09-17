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
point_O, point_P, point_A, point_B, point_C = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(area_triangle):
    """
    计算给定的几何表达式（圆锥的表面积）

    参数:
    area_triangle (float): 轴截面三角形的面积

    返回:
    float: 计算结果
    """
    return math.pi * area_triangle * (1 + math.sqrt(2))


# 定义题干中的变量
area_triangle = 9

# result = calculate(area_triangle)
# print(f"计算结果: {result:.6f}")
 
# Generate random lengths
area_triangle = round(len_scaling_factor * float(area_triangle), 2)

# Calculate the result
result = calculate(area_triangle)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area1_15_2",
    "type": 4,
    "level": 1,
    "cn_problem": f"{point_O} 是圆锥底面圆的圆心，圆锥的轴截面 {point_P}{point_A}{point_B} 为等腰直角三角形，{point_C} 为底面圆周上一点。设圆锥的轴截面 {point_P}{point_A}{point_B} 为等腰直角三角形，若三角形 {point_P}{point_A}{point_B} 的面积为 {area_triangle}，求此圆锥的表面积。",
    "en_problem": f"{point_O} is the center of the cone's base circle, the axial cross-section {point_P}{point_A}{point_B} is an isosceles right triangle, and {point_C} is a point on the base circle. Given that the axial cross-section {point_P}{point_A}{point_B} is an isosceles right triangle with area {area_triangle}, find the surface area of the cone.",
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
    f.write(json.dumps({json_data["id"]: f"area1_15_2({mode}, {azimuth}, {elevation}, '{point_O}', '{point_P}', '{point_A}', '{point_B}', '{point_C}')"}, ensure_ascii=False) + "\n")
