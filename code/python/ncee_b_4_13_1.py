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
point_A, point_B, point_C, point_A1, point_B1, point_C1 = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
def calculate(len_a, len_b, len_h):
    """计算体积V = (len_a × len_b × len_h) / 2"""
    return (len_a * len_b * len_h) / 2


# 测试示例
len_a = 4.0
len_b = 2.0
len_h = 5.0

# print(calculate(len_a, len_b, len_h))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_b, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_13_1",
    "type": 5,
    "level": 1,
    "cn_problem": f"如图，已知直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 的底面 {point_A}{point_B}{point_C} 为直角三角形，且 ∠{point_B}{point_A}{point_C}=90°，两直角边分别为 {point_A}{point_B}={len_a}>0，{point_A}{point_C}={len_b}>0，侧棱 {point_A}{point_A1}={len_h}>0。求该直三棱柱的体积。",
    "en_problem": f"As shown, given a right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} where the base {point_A}{point_B}{point_C} is a right triangle with ∠{point_B}{point_A}{point_C}=90°, the two legs are {point_A}{point_B}={len_a}>0 and {point_A}{point_C}={len_b}>0, and the lateral edge {point_A}{point_A1}={len_h}>0. Find the volume of the right triangular prism.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_13_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}')"}, ensure_ascii=False) + "\n")
