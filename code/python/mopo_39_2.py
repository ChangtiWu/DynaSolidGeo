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
point_P, point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate():
    return math.sqrt(5) / 5


# 测试示例
len_t = 2.0

# print(calculate())

# Generate random lengths
len_t = round(len_scaling_factor * float(len_t), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_39_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 中，底面 {point_A}{point_B}{point_C}{point_D} 为直角梯形，满足：${point_A}{point_B} \\\\parallel {point_C}{point_D}$，${point_A}{point_B} \\\\perp {point_B}{point_C}$；${point_A}{point_B} = {point_B}{point_D} = 2*{point_C}{point_D} = 2*{len_t}$（即 ${point_A}{point_B} = 2*{len_t}$，${point_C}{point_D} = {len_t}$，${point_B}{point_D} = 2*{len_t}$）；侧面 {point_P}{point_C}{point_D} 是正三角形，且侧面 {point_P}{point_C}{point_D} $\\\\perp$ 底面 {point_A}{point_B}{point_C}{point_D}。求平面 {point_P}{point_B}{point_D} 与平面 {point_P}{point_B}{point_C} 的夹角的余弦值 。",
    "en_problem": f"In pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, the base {point_A}{point_B}{point_C}{point_D} is a right trapezoid satisfying: ${point_A}{point_B} \\\\parallel {point_C}{point_D}$, ${point_A}{point_B} \\\\perp {point_B}{point_C}$; ${point_A}{point_B} = {point_B}{point_D} = 2*{point_C}{point_D} = 2*{len_t}$ (i.e., ${point_A}{point_B} = 2*{len_t}$, ${point_C}{point_D} = {len_t}$, ${point_B}{point_D} = 2*{len_t}$); lateral face {point_P}{point_C}{point_D} is an equilateral triangle, and lateral face {point_P}{point_C}{point_D} $\\\\perp$ base {point_A}{point_B}{point_C}{point_D}. Find the cosine value of the angle between plane {point_P}{point_B}{point_D} and plane {point_P}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_39_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
