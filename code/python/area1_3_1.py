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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_O, point_O1 = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate():
    """
    计算给定的几何表达式（圆柱侧面积与外接球表面积的比值）

    返回:
    float: 计算结果
    """
    return 2 * math.sqrt(3) / 7


# 定义题干中的变量
len_edge = 2 # 题干中出现，但公式没用到，仍需定义

# result = calculate()
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_edge = round(len_scaling_factor * float(len_edge), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area1_3_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"如图，棱长均为 {len_edge} 的直三棱柱 {point_A}{point_B}{point_C} - {point_A1}{point_B1}{point_C1} 的上、下底面均内接于圆柱 {point_O}{point_O1} 的上、下底面，则圆柱 {point_O}{point_O1} 的侧面积与其外接球的表面积之比为多少。",
    "en_problem": f"A regular triangular prism {point_A}{point_B}{point_C} - {point_A1}{point_B1}{point_C1} with edge length {len_edge} has its upper and lower bases inscribed in the upper and lower bases of cylinder {point_O}{point_O1}. Find the ratio of the lateral surface area of cylinder {point_O}{point_O1} to the surface area of its circumscribed sphere.",
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
    f.write(json.dumps({json_data["id"]: f"area1_3_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_O}', '{point_O1}')"}, ensure_ascii=False) + "\n")
