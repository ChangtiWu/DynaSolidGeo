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
point_P, point_A, point_B, point_C, point_D, point_E, point_F, point_T = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a):
    """计算len_L关于len_a的表达式"""
    return (len_a * math.sqrt(5)) / 6


# 测试示例
len_a = 2.0

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_22_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"在四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 中，${point_P}{point_A} \\\\perp$ 平面 {point_A}{point_B}{point_C}{point_D}，底面 {point_A}{point_B}{point_C}{point_D} 为正方形，${point_P}{point_A} = {point_A}{point_B} = {len_a}$。点 {point_E}、{point_F} 分别为 ${point_C}{point_D}$、${point_C}{point_P}$ 的中点，点 {point_T} 为 $\\\\triangle {point_P}{point_A}{point_B}$ 内的动点（含边界），若 ${point_C}{point_T} \\\\parallel$ 平面 ${point_A}{point_E}{point_F}$，求点 {point_T} 的轨迹长度。",
    "en_problem": f"In quadrangular pyramid {point_P}-{point_A}{point_B}{point_C}{point_D} where ${point_P}{point_A} \\\\perp$ plane {point_A}{point_B}{point_C}{point_D}, base {point_A}{point_B}{point_C}{point_D} is a square, and ${point_P}{point_A} = {point_A}{point_B} = {len_a}$. Points {point_E} and {point_F} are midpoints of ${point_C}{point_D}$ and ${point_C}{point_P}$ respectively, and point {point_T} is a moving point within $\\\\triangle {point_P}{point_A}{point_B}$ (including boundary). If ${point_C}{point_T} \\\\parallel$ plane ${point_A}{point_E}{point_F}$, find the trajectory length of point {point_T}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_22_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_T}')"}, ensure_ascii=False) + "\n")
