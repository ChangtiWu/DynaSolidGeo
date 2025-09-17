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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_F, point_P = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math


def calculate(len_m):
    """计算len_L关于len_a的表达式"""
    return len_m


# 测试示例
len_m = math.sqrt(3)

# print(calculate(len_m))

# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)

# Calculate the result
result = calculate(len_m)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_7_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"在正方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}中，{point_E}为{point_A}{point_A1}的中点，{point_F}为{point_A}{point_B}的中点，且{point_E}{point_F} = {len_m}。点{point_P}是正方形{point_A}{point_B}{point_B1}{point_A1}内的动点，若{point_C1}{point_P} ∥ 平面{point_C}{point_D1}{point_E}{point_F}，求{point_P}点的轨迹长度。",
    "en_problem": f"In cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, {point_E} is the midpoint of {point_A}{point_A1}, {point_F} is the midpoint of {point_A}{point_B}, and {point_E}{point_F} = {len_m}. Point {point_P} is a moving point inside square {point_A}{point_B}{point_B1}{point_A1}. If {point_C1}{point_P} ∥ plane {point_C}{point_D1}{point_E}{point_F}, find the length of the trajectory of point {point_P}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_7_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_F}', '{point_P}')"}, ensure_ascii=False) + "\n")
