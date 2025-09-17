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
point_A, point_B, point_C, point_D, point_P, point_O = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_a, len_b, len_R):
    """计算cos(arg_theta)的值（表达式为(len_a²·len_b²)/(len_a⁴ + len_b⁴ + len_a²·len_b²)）"""
    numerator = (len_a ** 2) * (len_b ** 2)
    denominator = (len_a ** 4) + (len_b ** 4) + (len_a ** 2 * len_b ** 2)
    return numerator / denominator


# 测试示例
len_a = 2.0
len_b = 2 * math.sqrt(3)
len_R = 2  # 公式中未使用，但需保持变量名一致

# print(calculate(len_a, len_b, len_R))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_R = round(len_scaling_factor * float(len_R), 2)

# Calculate the result
result = calculate(len_a, len_b, len_R)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_41_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在矩形 {point_A}{point_B}{point_C}{point_D} 中，设 ${point_A}{point_B} = {len_a}$，${point_A}{point_D} = {len_b}$，沿对角线 ${point_B}{point_D}$ 将 $\\\\triangle {point_A}{point_B}{point_D}$ 折起，使点 {point_A} 到达点 {point_P}，且平面 {point_P}{point_B}{point_D} $\\\\perp$ 平面 {point_B}{point_C}{point_D}。三棱锥 ${point_P}-{point_B}{point_C}{point_D}$ 的外接球半径为 ${len_R}$（故 ${point_B}{point_D} = 2*{len_R}$，球心为 ${point_B}{point_D}$ 中点 {point_O}）。求平面 {point_P}{point_C}{point_B} 与平面 {point_P}{point_C}{point_D} 夹角的余弦值 。",
    "en_problem": f"In rectangle {point_A}{point_B}{point_C}{point_D}, let ${point_A}{point_B} = {len_a}$ and ${point_A}{point_D} = {len_b}$. Fold $\\\\triangle {point_A}{point_B}{point_D}$ along diagonal ${point_B}{point_D}$ so that point {point_A} reaches point {point_P}, with plane {point_P}{point_B}{point_D} $\\\\perp$ plane {point_B}{point_C}{point_D}. The circumradius of tetrahedron ${point_P}-{point_B}{point_C}{point_D}$ is ${len_R}$ (so ${point_B}{point_D} = 2*{len_R}$, with center {point_O} at the midpoint of ${point_B}{point_D}$). Find the cosine value of the angle between planes {point_P}{point_C}{point_B} and {point_P}{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_41_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}', '{point_O}')"}, ensure_ascii=False) + "\n")
