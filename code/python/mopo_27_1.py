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
point_S, point_A, point_B, point_C, point_D, point_P = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_a):
    """计算len_L关于len_a的表达式（结果为len_a乘以(√3 + √2)）"""
    return len_a * (math.sqrt(3) + math.sqrt(2))


# 测试示例
len_a = 2.0

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_27_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"四棱锥 {point_S}-{point_A}{point_B}{point_C}{point_D} 的底面是边长为 ${len_a}$ 的正方形，侧面 {point_S}{point_A}{point_B}、{point_S}{point_B}{point_C}、{point_S}{point_C}{point_D}、{point_S}{point_D}{point_A} 均为等边三角形。动点 {point_P} 在四棱锥表面运动，且始终满足 ${point_P}{point_B} \\\\perp {point_S}{point_C}$，求 {point_P} 从 {point_B} 出发回到 {point_B} 的最短路程。",
    "en_problem": f"In quadrangular pyramid {point_S}-{point_A}{point_B}{point_C}{point_D} with square base of edge length ${len_a}$, lateral faces {point_S}{point_A}{point_B}, {point_S}{point_B}{point_C}, {point_S}{point_C}{point_D}, {point_S}{point_D}{point_A} are all equilateral triangles. Moving point {point_P} moves on the surface of the pyramid and always satisfies ${point_P}{point_B} \\\\perp {point_S}{point_C}$. Find the shortest path length for {point_P} to travel from {point_B} back to {point_B}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_27_1({mode}, {azimuth}, {elevation}, '{point_S}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}')"}, ensure_ascii=False) + "\n")
