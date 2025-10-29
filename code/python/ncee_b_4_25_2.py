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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_E, point_F = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a, ang_theta):
    """计算体积V的表达式：V = (√3/48) * len_a³ * √(3/(4sin²θ) - 1)（要求0 < θ < π/3）"""
    # 计算根号内部分
    sin_theta_sq = (math.sin(ang_theta)) ** 2
    sqrt_inner = 3 / (4 * sin_theta_sq) - 1
    sqrt_term = math.sqrt(sqrt_inner)
    # 计算系数与len_a³的乘积
    coefficient = math.sqrt(3) / 48
    len_a_cubed = len_a ** 3
    # 最终结果
    return coefficient * len_a_cubed * sqrt_term


# 测试示例
len_a = 2.0
ang_theta = math.pi / 4

# print(calculate(len_a, ang_theta))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, ang_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_25_2",
    "type": 5,
    "level": 3,
    "cn_problem": f"如图，已知直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 的底面 {point_A}{point_B}{point_C} 为边长 {len_a}>0 的正三角形，侧棱均垂直于底面。记 {point_E} 为 {point_B}{point_C} 的中点，{point_F} 为 {point_C}{point_C1} 的中点，直线 {point_A1}{point_C} 与平面 {point_A1}{point_A}{point_B}{point_B1} 所成的夹角为 {ang_theta}（0<{ang_theta}<π/3）。求三棱锥 {point_F}-{point_A}{point_E}{point_C} 的体积。",
    "en_problem": f"As shown, given a right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} where the base {point_A}{point_B}{point_C} is an equilateral triangle with side length {len_a}>0, and all lateral edges are perpendicular to the base. Let {point_E} be the midpoint of {point_B}{point_C}, {point_F} be the midpoint of {point_C}{point_C1}, and the angle between line {point_A1}{point_C} and plane {point_A1}{point_A}{point_B}{point_B1} be {ang_theta} (0<{ang_theta}<π/3). Find the volume of triangular pyramid {point_F}-{point_A}{point_E}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_25_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
