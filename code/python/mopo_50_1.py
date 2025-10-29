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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_P = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math


def calculate(len_L):
    """计算表达式 π·len_L²/3 的值"""
    return (math.pi * (len_L ** 2)) / 3


# 测试示例
len_L = 6.0

# print(calculate(len_L))

# Generate random lengths
len_L = round(len_scaling_factor * float(len_L), 2)

# Calculate the result
result = calculate(len_L)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_50_1",
    "type": 7,
    "level": 3,
    "cn_problem": f"在长方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 中，${point_A}{point_B} = 2*{point_A}{point_D} = 2*{point_A}{point_A1} = {len_L}$（即 ${point_A}{point_D} = {point_A}{point_A1} = \\\\frac{{{len_L}}}{{2}}$），点 {point_E} 在棱 ${point_A}{point_B}$ 上且 ${point_B}{point_E} = 2*{point_A}{point_E}$，动点 {point_P} 满足 ${point_B}{point_P} = \\\\sqrt{{3}} \\\\cdot {point_P}{point_E}$。若点 {point_P} 在平面 {point_A}{point_B}{point_C}{point_D} 内运动，求点 {point_P} 轨迹的面积。",
    "en_problem": f"In rectangular prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, ${point_A}{point_B} = 2*{point_A}{point_D} = 2*{point_A}{point_A1} = {len_L}$ (i.e., ${point_A}{point_D} = {point_A}{point_A1} = \\\\frac{{{len_L}}}{{2}}$), point {point_E} is on edge ${point_A}{point_B}$ with ${point_B}{point_E} = 2*{point_A}{point_E}$, and moving point {point_P} satisfies ${point_B}{point_P} = \\\\sqrt{{3}} \\\\cdot {point_P}{point_E}$. If point {point_P} moves within plane {point_A}{point_B}{point_C}{point_D}, find the area of the trajectory of point {point_P}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_50_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_P}')"}, ensure_ascii=False) + "\n")
