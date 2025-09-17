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
point_D, point_O, point_P, point_A, point_B, point_C = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(radius_r):
    """
    计算四面体 {point_P}-{point_A}{point_B}{point_C} 的体积 V

    参数:
        radius_r (float): 特征半径参数 r

    返回:
        float: 四面体体积计算结果

    公式:
        V = (√6 / 8) × radius_r³
    """
    # 计算核心表达式
    return (math.sqrt(6) / 8) * (radius_r ** 3)

# 当特征半径 r = 2 时的体积计算
radius_r = 1.0
height_h = math.sqrt(2)
# volume = calculate(radius_r)
#
# print(f"四面体体积 V = {volume:.6f}")
# Generate random lengths
radius_r = round(len_scaling_factor * float(radius_r), 2)
height_h = round(len_scaling_factor * float(height_h), 2)

# Calculate the result
result = calculate(radius_r)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_8_2",
    "type": 5,
    "level": 3,
    "cn_problem": f"设圆锥 {point_D}-（底面圆 {point_O},{radius_r}）满足：底面圆心为 {point_O}，半径为 {radius_r}>0；轴长（高）{point_D}{point_O}={height_h}（{height_h}>0），且 {height_h}≥\\frac{{{radius_r}}}{{\\sqrt{{2}}}}（保证后文的点 {point_P} 存在）；在底面圆上作内接正三角形 \\triangle {point_A}{point_B}{point_C}；取轴 {point_D}{point_O} 上一点 {point_P}，使得 ∠{point_A}{point_P}{point_C}=90°。求三棱锥 {point_P}-{point_A}{point_B}{point_C} 的体积。",
    "en_problem": f"Given cone {point_D}-(base circle {point_O},{radius_r}) where: the base has center {point_O} and radius {radius_r}>0; the axis height {point_D}{point_O}={height_h} ({height_h}>0) with {height_h}≥\\frac{{{radius_r}}}{{\\sqrt{{2}}}} (ensuring existence of point {point_P}); \\triangle {point_A}{point_B}{point_C} is an inscribed equilateral triangle in the base circle; point {point_P} lies on axis {point_D}{point_O} such that ∠{point_A}{point_P}{point_C}=90°. Find the volume of triangular pyramid {point_P}-{point_A}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_8_2({mode}, {azimuth}, {elevation}, '{point_D}', '{point_O}', '{point_P}', '{point_A}', '{point_B}', '{point_C}')"}, ensure_ascii=False) + "\n")
