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
point_P, point_A, point_B, point_C = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math

def calculate(len_b):
    """
    计算三棱锥外接球的表面积

    参数:
    len_b (float): 棱长 PA=PB=PC

    返回:
    float: 外接球表面积
    """
    # 外接球半径 R = len_b * sqrt(3) / 2
    R = len_b * math.sqrt(3) / 2
    # 球的表面积 S = 4 * pi * R^2
    return 4 * math.pi * R ** 2


# 定义题干参数
len_a = 2
len_b = math.sqrt(2)

# 验证计算结果
#result = calculate(len_b)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_18_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"在三棱锥 {point_P} - {point_A}{point_B}{point_C} 中，底面 {point_A}{point_B}{point_C} 是边长为 {len_a} 的等边三角形，且 {point_P}{point_A} = {point_P}{point_B} = {point_P}{point_C} = {len_b}，并且三条棱两两垂直。求三棱锥 {point_P} - {point_A}{point_B}{point_C} 的外接球的表面积。",
    "en_problem": f"In the tetrahedron {point_P} - {point_A}{point_B}{point_C}, the base {point_A}{point_B}{point_C} is an equilateral triangle with side length {len_a}, and {point_P}{point_A} = {point_P}{point_B} = {point_P}{point_C} = {len_b}, where the three edges are pairwise perpendicular. Find the surface area of the circumscribed sphere of tetrahedron {point_P} - {point_A}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"area2_18_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}')"}, ensure_ascii=False) + "\n")
