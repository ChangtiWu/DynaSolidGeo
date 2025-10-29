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
point_P, point_A, point_B, point_C, point_D, point_M, point_G = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate():
    """计算固定值 2√2/3"""
    return (2 * math.sqrt(2)) / 3


# 测试示例
len_a = 2.0
len_h = math.sqrt(2)

# print(calculate())


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_46_2",
    "type": 7,
    "level": 2,
    "cn_problem": f"在四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 中，底面 {point_A}{point_B}{point_C}{point_D} 是边长为 ${len_a}$ 的正方形，侧面 {point_P}{point_A}{point_D} 为等边三角形，顶点 {point_P} 在底面 {point_A}{point_B}{point_C}{point_D} 外部，且四棱锥体积为 $ volume_V  = \\\\frac{{{len_a}^3}}{{3\\\\sqrt{2}}}$（满足几何约束：{point_P} 到底面的高 $ len_h  = \\\\frac{{{len_a}}}{{\\sqrt{{2}}}}$，等边三角形 {point_P}{point_A}{point_D} 的高 ${point_P}{point_M} = \\\\frac{{\\\\sqrt{{3}}}}{{len_a}}{2}$，其中 {point_M} 为 ${point_A}{point_D}$ 中点）。设点 {point_G} 为棱 {point_P}{point_B} 上的动点（不含端点）， {point_G} 的位置为 $\\\\overrightarrow{{{point_P}{point_G}}} = \\\\lambda \\\\overrightarrow{{{point_P}{point_B}}}$（$0 < \\\\lambda < 1$），求直线 {point_A}{point_G} 与平面 {point_P}{point_C}{point_D} 所成角的正弦值的最大值。",
    "en_problem": f"In pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, the base {point_A}{point_B}{point_C}{point_D} is a square with side length ${len_a}$, lateral face {point_P}{point_A}{point_D} is an equilateral triangle, vertex {point_P} is outside the base {point_A}{point_B}{point_C}{point_D}, and the pyramid volume is $ volume_V  = \\\\frac{{{len_a}^3}}{{3\\\\sqrt{2}}}$ (satisfying geometric constraints: the height from {point_P} to the base is $ len_h  = \\\\frac{{{len_a}}}{{\\sqrt{{2}}}}$，the height of equilateral triangle {point_P}{point_A}{point_D} is ${point_P}{point_M} = \\\\frac{{\\\\sqrt{{3}}}}{{{len_a}}}{2}$，where {point_M} is the midpoint of ${point_A}{point_D}$). Let point {point_G} be a moving point on edge {point_P}{point_B} (excluding endpoints), {point_G}'s position is $\\\\overrightarrow{{{point_P}{point_G}}} = \\\\lambda \\\\overrightarrow{{{point_P}{point_B}}}$ ($0 < \\\\lambda < 1$), find the maximum value of the sine of the angle between line {point_A}{point_G} and plane {point_P}{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_46_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}', '{point_G}')"}, ensure_ascii=False) + "\n")
