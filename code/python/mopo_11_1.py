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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math


def calculate(len_b):
    """计算len_BC关于len_b的表达式"""
    return 2 * len_b


# 测试示例
len_b = 1.0
len_h = math.sqrt(3)

# print(calculate(len_b))

# Generate random lengths
len_b = round(len_scaling_factor * float(len_b), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_11_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"在直四棱柱 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 中，底面 {point_A}{point_B}{point_C}{point_D} 为矩形，${point_A}{point_B} = {len_b}$（${len_b} > 0$），${point_A}{point_A1} = {len_h}$（${len_h} > 0$）。点 {point_M} 在线段 ${point_B}{point_C}$ 上，且 ${point_A}{point_M} \\\\perp {point_M}{point_D}$。当三棱锥 ${point_A1}-{point_A}{point_M}{point_D}$ 的体积最小时，求线段 ${point_B}{point_C}$ 的长度。",
    "en_problem": f"In a right quadrilateral prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} where base {point_A}{point_B}{point_C}{point_D} is a rectangle, ${point_A}{point_B} = {len_b}$ (${len_b} > 0$), and ${point_A}{point_A1} = {len_h}$ (${len_h} > 0$). Point {point_M} lies on segment ${point_B}{point_C}$ with ${point_A}{point_M} \\\\perp {point_M}{point_D}$. When the volume of triangular pyramid ${point_A1}-{point_A}{point_M}{point_D}$ is minimized, find the length of segment ${point_B}{point_C}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_11_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_M}')"}, ensure_ascii=False) + "\n")
