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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M, point_N, point_Q = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math


def calculate(len_a):
    """计算len_d_min关于len_a的表达式"""
    return (len_a * math.sqrt(38)) / 6


# 测试示例
len_a = 3.0

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_6_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"设正方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 的棱长为 ${len_a}$，点 {point_M}、{point_N} 分别在棱 ${point_A}{point_A1}$、${point_A1}{point_D1}$ 上，满足 ${point_A}{point_A1} = 3*({point_A}{point_M})$，${point_A1}{point_D1} = 3*({point_D1}{point_N})$。点 {point_Q} 在正方体的面 ${point_B}{point_C}{point_C1}{point_B1}$ 内，且 ${point_A1}{point_Q} \\\\parallel$ 平面 ${point_C1}{point_M}{point_N}$，求线段 ${point_A1}{point_Q}$ 长度的最小值。",
    "en_problem": f"Let cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} have edge length ${len_a}$, points {point_M}, {point_N} are on edges ${point_A}{point_A1}$, ${point_A1}{point_D1}$ respectively, satisfying ${point_A}{point_A1} = 3*({point_A}{point_M})$, ${point_A1}{point_D1} = 3*({point_D1}{point_N})$. Point {point_Q} is within face ${point_B}{point_C}{point_C1}{point_B1}$ and ${point_A1}{point_Q} \\\\parallel$ plane ${point_C1}{point_M}{point_N}$. Find the minimum value of segment ${point_A1}{point_Q}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_6_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_M}', '{point_N}', '{point_Q}')"}, ensure_ascii=False) + "\n")
