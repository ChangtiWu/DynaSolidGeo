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
point_A, point_B, point_C, point_D, point_F, point_E, point_N = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate():
    """返回固定区间 [√10/10, √5/3] 的列表形式"""
    return math.sqrt(10) / 10


# 测试示例
len_a = 2.0

# print(calculate())

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_47_2_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"设四边形 {point_A}{point_B}{point_C}{point_D} 为正方形，边长为 $2*{len_a}$；四边形 {point_A}{point_B}{point_F}{point_E}、{point_C}{point_D}{point_E}{point_F} 为全等的等腰梯形，满足 ${point_E}{point_F} \\\\parallel {point_A}{point_B}$，${point_A}{point_B} = 2*{point_E}{point_F}$（即 ${point_E}{point_F} = {len_a}$），且腰长 ${point_E}{point_A} = {point_E}{point_D} = {point_F}{point_B} = {point_F}{point_C} = \\\\frac{{3*{len_a}}}{{2}}$（保证 ${point_E}{point_F}$ 到平面 {point_A}{point_B}{point_C}{point_D} 的距离为 ${len_a}$）。点 {point_N} 在线段 ${point_A}{point_D}$ 上（包含端点），设 $\\\\overrightarrow{{{point_A}{point_N}}} = \\\\lambda \\\\overrightarrow{{{point_A}{point_D}}}$（$\\\\lambda \\\\in [0,1]$，$\\\\lambda = 0$ 对应 {point_A}，$\\\\lambda = 1$ 对应 {point_D}）。求平面 {point_B}{point_F}{point_N} 和平面 {point_A}{point_D}{point_E} 的夹角的余弦值的最小值。",
    "en_problem": f"Let quadrilateral {point_A}{point_B}{point_C}{point_D} be a square with side length $2*{len_a}$; quadrilaterals {point_A}{point_B}{point_F}{point_E} and {point_C}{point_D}{point_E}{point_F} are congruent isosceles trapezoids, satisfying ${point_E}{point_F} \\\\parallel {point_A}{point_B}$, ${point_A}{point_B} = 2*{point_E}{point_F}$ (i.e., ${point_E}{point_F} = {len_a}$), and leg lengths ${point_E}{point_A} = {point_E}{point_D} = {point_F}{point_B} = {point_F}{point_C} = \\\\frac{{3*{len_a}}}{{2}}$ (ensuring the distance from ${point_E}{point_F}$ to plane {point_A}{point_B}{point_C}{point_D} is ${len_a}$). Point {point_N} is on segment ${point_A}{point_D}$ (including endpoints), with $\\\\overrightarrow{{{point_A}{point_N}}} = \\\\lambda \\\\overrightarrow{{{point_A}{point_D}}}$ ($\\\\lambda \\\\in [0,1]$, $\\\\lambda = 0$ corresponds to {point_A}, $\\\\lambda = 1$ corresponds to {point_D}). Find the minimum of cosine values of the angle between plane {point_B}{point_F}{point_N} and plane {point_A}{point_D}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_47_2_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_F}', '{point_E}', '{point_N}')"}, ensure_ascii=False) + "\n")
