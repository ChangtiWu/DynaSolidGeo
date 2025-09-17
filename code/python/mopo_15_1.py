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
point_O, point_A, point_B, point_C, point_D, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_a):
    """计算表达式√2/2 * len_a的值"""
    return (math.sqrt(2) / 2) * len_a


# 测试示例
len_a = math.sqrt(3)

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_15_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"三棱锥 {point_O}-{point_A}{point_B}{point_C} 各棱的棱长均为 ${len_a}$，点 {point_D} 是棱 ${point_A}{point_B}$ 的中点，点 {point_E} 在棱 ${point_O}{point_C}$ 上运动，求 ${point_D}{point_E}$ 的最小值。",
    "en_problem": f"In tetrahedron {point_O}-{point_A}{point_B}{point_C}, all edges have length ${len_a}$. Point {point_D} is the midpoint of edge ${point_A}{point_B}$, and point {point_E} moves on edge ${point_O}{point_C}$. Find the minimum value of ${point_D}{point_E}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_15_1({mode}, {azimuth}, {elevation}, '{point_O}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
