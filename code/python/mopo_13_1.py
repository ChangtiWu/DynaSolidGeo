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
point_A, point_B, point_C, point_D, point_E, point_F, point_G = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_a):
    """计算len_d_min关于len_a的表达式"""
    return (3 * len_a * math.sqrt(2)) / 4


# 测试示例
len_a = 3.0

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_13_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"设圆柱的一个轴截面是边长为 ${len_a}$ 的正方形 {point_A}{point_B}{point_C}{point_D}，点 {point_E} 在下底面圆周上，且 ${point_C}{point_E} = \\\\sqrt{3}{point_B}{point_E}$，点 {point_F} 在母线 ${point_A}{point_B}$ 上，点 {point_G} 是线段 ${point_A}{point_C}$ 上靠近点 {point_A} 的四等分点，求 ${point_E}{point_F} + {point_F}{point_G}$ 的最小值 。",
    "en_problem": f"Let a cylinder have an axial cross-section that is a square {point_A}{point_B}{point_C}{point_D} with side length ${len_a}$. Point {point_E} is on the circumference of the lower base, satisfying ${point_C}{point_E} = \\\\sqrt{3}{point_B}{point_E}$. Point {point_F} is on generatrix ${point_A}{point_B}$, and point {point_G} is the quarter point of segment ${point_A}{point_C}$ closer to point {point_A}. Find the minimum value of ${point_E}{point_F} + {point_F}{point_G}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_13_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_G}')"}, ensure_ascii=False) + "\n")
