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
point_P, point_A, point_B, point_C, point_D, point_M = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate():
    """计算满足cos(theta) = √10/5的角度theta（弧度制）"""
    return math.sqrt(10) / 5


# 测试示例
len_a = 1.0
arg_beta = math.pi / 2
arg_alpha = math.pi / 4

# print(calculate())

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_8_6_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}中，侧面{point_P}{point_A}{point_D}是边长为2*{len_a}的等边三角形且垂直于底面{point_A}{point_B}{point_C}{point_D}，{point_A}{point_B}={point_B}{point_C}={len_a}，∠{point_B}{point_A}{point_D}=∠{point_A}{point_B}{point_C}={arg_beta}。点{point_M}在棱{point_P}{point_C}上，且直线{point_B}{point_M}与底面{point_A}{point_B}{point_C}{point_D}所成角为{arg_alpha}，求二面角{point_M}-{point_A}{point_B}-{point_D}的余弦值。",
    "en_problem": f"In quadrilateral pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, lateral face {point_P}{point_A}{point_D} is an equilateral triangle with side length 2*{len_a} and perpendicular to base {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B}={point_B}{point_C}={len_a}, ∠{point_B}{point_A}{point_D}=∠{point_A}{point_B}{point_C}={arg_beta}. Point {point_M} is on edge {point_P}{point_C}, and the angle between line {point_B}{point_M} and base {point_A}{point_B}{point_C}{point_D} is {arg_alpha}. Find the cosine value of dihedral angle {point_M}-{point_A}{point_B}-{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_8_6_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}')"}, ensure_ascii=False) + "\n")
