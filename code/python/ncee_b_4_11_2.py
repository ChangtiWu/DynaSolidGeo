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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
def calculate(len_s):
    """
    计算几何体 {point_E}-{point_B}{point_B1}{point_C1}{point_C} 的体积 V

    参数:
        len_s (float): 特征长度参数 s（与几何体尺寸直接相关的长度量）

    返回:
        float: 几何体的体积计算结果

    公式:
        V = (2/3) × len_s³
    """
    return (2 / 3) * (len_s ** 3)

len_s = 3.0
len_h = 3.0
# volume = calculate(len_s)
#
# print(f"几何体体积 V = {volume:.2f}")
# Generate random lengths
len_s = round(len_scaling_factor * float(len_s), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_s)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_11_2",
    "type": 5,
    "level": 2,
    "cn_problem": f"在长方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 中，底面 {point_A}{point_B}{point_C}{point_D} 为边长为 {len_s}（{len_s}>0）的正方形，设高为 2*{len_h}（{len_h}>0），即 {point_A}{point_A1}={point_B}{point_B1}={point_C}{point_C1}={point_D}{point_D1}=2*{len_h}。取点 {point_E} 为棱 {point_A}{point_A1} 的中点，故 {point_A}{point_E}={point_A1}{point_E}={len_h}。已知 {point_B}{point_E}⊥{point_B1}{point_E}。求四棱锥 {point_E}-{point_B}{point_B1}{point_C1}{point_C} 的体积 V_{{{point_E}-{point_B}{point_B1}{point_C1}{point_C}}}。",
    "en_problem": f"In the rectangular parallelepiped {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, the base {point_A}{point_B}{point_C}{point_D} is a square with side length {len_s} ({len_s}>0), and the height is 2*{len_h} ({len_h}>0), i.e., {point_A}{point_A1}={point_B}{point_B1}={point_C}{point_C1}={point_D}{point_D1}=2*{len_h}. Let point {point_E} be the midpoint of edge {point_A}{point_A1}, so {point_A}{point_E}={point_A1}{point_E}={len_h}. Given {point_B}{point_E}⊥{point_B1}{point_E}, find the volume V_{{{point_E}-{point_B}{point_B1}{point_C1}{point_C}}} of the quadrilateral pyramid {point_E}-{point_B}{point_B1}{point_C1}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_11_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}')"}, ensure_ascii=False) + "\n")
