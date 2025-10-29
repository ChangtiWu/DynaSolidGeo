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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_E, point_P = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a):
    """计算len_d关于len_a的表达式"""
    return (len_a * math.sqrt(6)) / 2


# 测试示例
len_a = 1.0

# print(calculate(len_a))


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_1_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"在直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，$\\triangle {point_A}{point_B}{point_C}$ 为腰长为 ${len_a}>0$ 的等腰直角三角形，满足 ${point_A}{point_B} \\geq {point_A}{point_C}$，故 ${point_A}{point_C} = {point_B}{point_C} = {len_a}$，侧面 ${point_A}{point_C}{point_C1}{point_A1}$ 为正方形，$\\overrightarrow{{{point_A}{point_B}}} = 2\\overrightarrow{{{point_A}{point_E}}}$（即 {point_E} 为 ${point_A}{point_B}$ 的中点），{point_P} 为平面 ${point_A1}{point_B}{point_C}$ 内的动点。求 ${point_P}{point_A} + {point_P}{point_E}$ 的最小值。",
    "en_problem": f"In a right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, $\\triangle {point_A}{point_B}{point_C}$ is an isosceles right triangle with legs of length ${len_a}>0$, satisfying ${point_A}{point_B} \\geq {point_A}{point_C}$, so ${point_A}{point_C} = {point_B}{point_C} = {len_a}$. The lateral face ${point_A}{point_C}{point_C1}{point_A1}$ is a square, $\\overrightarrow{{{point_A}{point_B}}} = 2\\overrightarrow{{{point_A}{point_E}}}$ (i.e., {point_E} is the midpoint of ${point_A}{point_B}$), and {point_P} is a moving point in plane ${point_A1}{point_B}{point_C}$. Find the minimum value of ${point_P}{point_A} + {point_P}{point_E}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_1_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_E}', '{point_P}')"}, ensure_ascii=False) + "\n")
