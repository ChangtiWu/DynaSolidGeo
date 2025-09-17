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


def calculate(len_a: float, len_b: float, arg_alpha: float) -> float:
    """计算 cosθ 的表达式值"""
    cos_arg = math.cos(arg_alpha)
    sin_arg = math.sin(arg_alpha)
    numerator = 2 * len_a ** 2 * (1 + cos_arg) - len_b ** 2 * sin_arg ** 2
    denominator = 2 * len_a ** 2 * (1 + cos_arg) + len_b ** 2 * sin_arg ** 2
    return numerator / denominator


len_a = 3.0
len_b = 2.0
arg_alpha = math.pi / 3 * 2

# result = calculate(len_a, len_b, arg_alpha)
# print(f"cosθ = {result:.6f}")

# Generate random lengths

len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b, arg_alpha)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_26_2",
    "type": 2,
    "level": 3,
    "cn_problem": f"设矩形 {point_A}{point_B}{point_C}{point_D}（含其内部）绕直线 {point_A}{point_B} 旋转角度 {arg_alpha}（0<{arg_alpha}<π）得到几何体的一部分。旋转前矩形边长 {point_A}{point_B}={len_a}>0，{point_A}{point_D}={len_b}>0；旋转后点 {point_C}，{point_D} 分别对应点 {point_E}，{point_F}；取 {point_G} 为 {point_D}{point_F} 的中点。求二面角 {point_E}-{point_A}{point_G}-{point_C} 的大小 θ。",
    "en_problem": f"Let rectangle {point_A}{point_B}{point_C}{point_D} (including its interior) rotate around line {point_A}{point_B} by angle {arg_alpha} (0<{arg_alpha}<π) to form part of a geometric solid. Before rotation, the rectangle has side lengths {point_A}{point_B}={len_a}>0 and {point_A}{point_D}={len_b}>0. After rotation, points {point_C} and {point_D} correspond to points {point_E} and {point_F} respectively. Let {point_G} be the midpoint of {point_D}{point_F}. Find the measure θ of dihedral angle {point_E}-{point_A}{point_G}-{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_26_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_G}')"}, ensure_ascii=False) + "\n")
