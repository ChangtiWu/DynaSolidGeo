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
    """
    计算截面面积 S

    参数:
    len_b (float): 长方体底边 AB 的长度

    返回:
    float: 截面面积
    """
    # 根据题解公式：S = 3 * sqrt(26) * len_b^2 / 8
    return 3 * math.sqrt(26) * len_b ** 2 / 8


# 定义题干参数
len_b = 2.0  # AB 的长度

# 验证计算结果
#result = calculate(len_b)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_22_1",
    "type": 4,
    "level": 2,
    "cn_problem": f"在长方体 {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1} 中，{point_A}{point_A1} = {point_A}{point_D} = \\sqrt{{2}}{{{point_A}{point_B}}}，设 {point_A}{point_B} = {len_b}（{len_b} > 0），点 {point_M} 在棱 {point_A1}{point_D1} 上，且 {point_A}{point_C} ⊥ {point_B}{point_M}。求平面 {point_B}{point_D}{point_M} 截长方体所得截面的面积。",
    "en_problem": f"In the cuboid {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1}, {point_A}{point_A1} = {point_A}{point_D} = \\sqrt{{2}}{{{point_A}{point_B}}}, let {point_A}{point_B} = {len_b} ({len_b} > 0), point {point_M} is on edge {point_A1}{point_D1}, and {point_A}{point_C} ⊥ {point_B}{point_M}. Find the area of the cross-section formed by plane {point_B}{point_D}{point_M}.",
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
    f.write(json.dumps({json_data["id"]: f"area2_22_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_M}')"}, ensure_ascii=False) + "\n")
