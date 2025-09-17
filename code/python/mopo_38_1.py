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
point_P, point_A, point_B, point_C, point_D, point_O, point_Q, point_T = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a, len_h):
    """计算area_S关于len_a和len_h的表达式（结果为5*len_a*√(len_a²+2len_h²)/16）"""
    return (5 * len_a * math.sqrt(len_a ** 2 + 2 * len_h ** 2)) / 16


# 测试示例
len_a = 2 * math.sqrt(2)
len_h = 4.0

# print(calculate(len_a, len_h))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_38_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"在四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 中，底面 {point_A}{point_B}{point_C}{point_D} 是边长为 ${len_a}$ 的正方形，顶点 {point_P} 在底面的射影为正方形中心 {point_O}，高 ${point_P}{point_O} = {len_h}$。点 {point_Q} 为 ${point_A}{point_O}$ 的中点，动点 {point_T} 在四棱锥表面上，满足 ${point_P}{point_A}$ 和 ${point_B}{point_D}$ 都平行于过 ${point_Q}{point_T}$ 的截面，求动点 {point_T} 的轨迹围成的多边形的面积。",
    "en_problem": f"In pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, the base {point_A}{point_B}{point_C}{point_D} is a square with side length ${len_a}$, vertex {point_P} has projection {point_O} at the center of the square base, and height ${point_P}{point_O} = {len_h}$. Point {point_Q} is the midpoint of ${point_A}{point_O}$, and moving point {point_T} is on the surface of the pyramid satisfying that both ${point_P}{point_A}$ and ${point_B}{point_D}$ are parallel to the cross-section through ${point_Q}{point_T}$. Find the area of the polygon formed by the trajectory of moving point {point_T}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_38_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}', '{point_Q}', '{point_T}')"}, ensure_ascii=False) + "\n")
