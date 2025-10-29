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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math


def calculate():
    """返回固定二维坐标点 (1/2, √3/2)"""
    return math.sqrt(3) / 2


# 测试示例
len_a = 2.0
arg_theta = math.pi / 3

# print(calculate())

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_45_3_2",
    "type": 7,
    "level": 2,
    "cn_problem": f"在三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，底面 $\\\\triangle {point_A}{point_B}{point_C}$ 是边长为 ${len_a}$ 的等边三角形；菱形 {point_A}{point_C}{point_C1}{point_A1} 中，${point_A}{point_C} = {point_C}{point_C1} = {len_a}$，$\\\\angle {point_A}{point_C}{point_C1} = {arg_theta}$，且平面 {point_A}{point_C}{point_C1}{point_A1} $\\\\perp$ 平面 {point_A}{point_B}{point_C}。{point_D}、{point_E} 分别是 ${point_A}{point_C}$、${point_C}{point_C1}$ 的中点。若点 {point_F} 为线段 ${point_B1}{point_C1}$ 上的动点（不包括端点）， {point_F} 的位置为 {point_F} = {point_B1} + \\\\lambda \\\\cdot \\\\overrightarrow{{{point_B1}{point_C1}}}$（$\\\\lambda \\\\in (0,1)$），求锐二面角 ${point_F}-{point_B}{point_D}-{point_E}$ 的余弦值的最大值。",
    "en_problem": f"In triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, the base $\\\\triangle {point_A}{point_B}{point_C}$ is an equilateral triangle with side length ${len_a}$; in rhombus {point_A}{point_C}{point_C1}{point_A1}, ${point_A}{point_C} = {point_C}{point_C1} = {len_a}$, $\\\\angle {point_A}{point_C}{point_C1} = {arg_theta}$, and plane {point_A}{point_C}{point_C1}{point_A1} $\\\\perp$ plane {point_A}{point_B}{point_C}. {point_D}, {point_E} are midpoints of ${point_A}{point_C}$, ${point_C}{point_C1}$ respectively. If point {point_F} is a moving point on segment ${point_B1}{point_C1}$ (excluding endpoints), {point_F}'s position is {point_F} = {point_B1} + \\\\lambda \\\\cdot \\\\overrightarrow{{{point_B1}{point_C1}}}$ ($\\\\lambda \\\\in (0,1)$), find the maximum of cosine values of acute dihedral angle ${point_F}-{point_B}{point_D}-{point_E}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_45_3_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
