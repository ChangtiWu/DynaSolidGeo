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
point_P, point_A, point_B, point_C, point_D, point_O, point_E = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate():
    """计算ang_theta的值（π/4）"""
    return math.pi / 4


# 测试示例
len_a = 5.0
# print(calculate())

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_1_2",
    "type": 2,
    "level": 1,
    "cn_problem": f"如图，设正四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 的底面 {point_A}{point_B}{point_C}{point_D} 为边长 {len_a}>0 的正方形，底面中心为 {point_O}。已知：(1) 四条侧棱长度均等且满足 {point_P}{point_A}={len_a}；(2) {point_E} 为侧棱 {point_P}{point_B} 的中点。求直线 {point_B}{point_D} 与平面 {point_A}{point_E}{point_C} 所成角的大小。",
    "en_problem": f"As shown, let the regular quadrilateral pyramid {point_P}-{point_A}{point_B}{point_C}{point_D} have a square base {point_A}{point_B}{point_C}{point_D} with side length {len_a}>0, and {point_O} is the center of the base. Given: (1) All four lateral edges are equal and satisfy {point_P}{point_A}={len_a}; (2) {point_E} is the midpoint of lateral edge {point_P}{point_B}. Find the angle between line {point_B}{point_D} and plane {point_A}{point_E}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_1_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}', '{point_E}')"}, ensure_ascii=False) + "\n")
