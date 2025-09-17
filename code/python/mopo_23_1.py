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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_S, point_P, point_Q = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math


def calculate(len_a):
    """计算len_L关于len_a的表达式（结果为√5乘以len_a的一半）"""
    return (math.sqrt(5) * len_a) / 2


# 测试示例
len_a = 2.0

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_23_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"正方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 的棱长为 ${len_a}$，{point_S} 是 ${point_A1}{point_B1}$ 的中点，{point_P} 是 ${point_A1}{point_D1}$ 的中点，点 {point_Q} 在正方形 ${point_D}{point_C}{point_C1}{point_D1}$ 及其内部运动，若 ${point_P}{point_Q} \\\\parallel$ 平面 ${point_S}{point_B}{point_C1}$，求点 {point_Q} 的轨迹长度。",
    "en_problem": f"In cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} with edge length ${len_a}$, {point_S} is the midpoint of ${point_A1}{point_B1}$, {point_P} is the midpoint of ${point_A1}{point_D1}$, and point {point_Q} moves within square ${point_D}{point_C}{point_C1}{point_D1}$ and its interior. If ${point_P}{point_Q} \\\\parallel$ plane ${point_S}{point_B}{point_C1}$, find the trajectory length of point {point_Q}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_23_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_S}', '{point_P}', '{point_Q}')"}, ensure_ascii=False) + "\n")
