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
point_A, point_B, point_C, point_D, point_F, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算四棱锥 F-ABCD 截面垂直于侧棱 FC 的最大面积

    参数:
    len_a (float): 正方形边长及等边三角形边长

    返回:
    float: 截面最大面积
    """
    return (math.sqrt(2) / 3) * len_a**2


# 题干给定的数值
len_a = 4.0   # 正方形边长及等边三角形边长

# 验证输出
# area_max = calculate(len_a)
# print(f"截面最大面积: {area_max:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "zht_8_3",
    "type": 8,
    "level": 2,
    "cn_problem": f"设正方形 {point_A}{point_B}{point_C}{point_D} 与等边三角形 {point_B}{point_C}{point_F} 的边长均为 {len_a}，将 △{point_B}{point_C}{point_F} 沿 {point_B}{point_C} 折起得到正四棱锥 {point_F}-{point_A}{point_B}{point_C}{point_D}（满足 {point_F}{point_A} = {point_F}{point_B} = {point_F}{point_C} = {point_F}{point_D} = {len_a}）。点 {point_E} 是侧棱 {point_F}{point_C} 上的动点，过 {point_E} 作截面垂直于 {point_F}{point_C}，求该截面面积的最大值。",
    "en_problem": f"Let the side lengths of square {point_A}{point_B}{point_C}{point_D} and equilateral triangle {point_B}{point_C}{point_F} both be {len_a}, fold △{point_B}{point_C}{point_F} along {point_B}{point_C} to form a regular quadrangular pyramid {point_F}-{point_A}{point_B}{point_C}{point_D} (satisfying {point_F}{point_A} = {point_F}{point_B} = {point_F}{point_C} = {point_F}{point_D} = {len_a}). Point {point_E} is a moving point on the lateral edge {point_F}{point_C}, through {point_E} make a cross-section perpendicular to {point_F}{point_C}, find the maximum area of this cross-section.",
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
    f.write(json.dumps({json_data["id"]: f"zht_8_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_F}', '{point_E}')"}, ensure_ascii=False) + "\n")
