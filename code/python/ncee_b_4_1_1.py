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
point_P, point_A, point_B, point_C, point_D, point_O = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_s, len_l):
    """计算体积V的表达式：V = (π·len_s²/6)·√(len_l² - len_s²/2)（要求len_l > len_s/√2）"""
    # 计算平方根内的部分
    sqrt_term = math.sqrt(len_l ** 2 - (len_s ** 2) / 2)
    # 计算系数部分
    coefficient = (math.pi * len_s ** 2) / 6
    # 返回最终结果
    return coefficient * sqrt_term


# 测试示例
len_s = 3 * math.sqrt(2)
len_l = 5.0

# print(calculate(len_s, len_l))

# Generate random lengths
len_s = round(len_scaling_factor * float(len_s), 2)
len_l = round(len_scaling_factor * float(len_l), 2)

# Calculate the result
result = calculate(len_s, len_l)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_1_1",
    "type": 5,
    "level": 2,
    "cn_problem": f"如图，在正四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 中，底面 {point_A}{point_B}{point_C}{point_D} 是边长为 {len_s}>0 的正方形，{point_O} 为底面中心，侧棱长 {point_A}{point_P}={len_l}（其中 {len_l}>\\frac{{{len_s}}}{{\\sqrt{{2}}}}）。设 ∠{point_P}{point_O}{point_A} 绕轴 {point_P}{point_O} 旋转一周所得旋转体的体积为volume_V， 求volume_V。",
    "en_problem": f"As shown, in a regular quadrilateral pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, the base {point_A}{point_B}{point_C}{point_D} is a square with side length {len_s}>0, {point_O} is the center of the base, and the lateral edge length {point_A}{point_P}={len_l} (where {len_l}>\\frac{{{len_s}}}{{\\sqrt{{2}}}}). Let volume_V be the volume of the solid of revolution formed by rotating ∠{point_P}{point_O}{point_A} about axis {point_P}{point_O}. Find volume_V.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_1_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}')"}, ensure_ascii=False) + "\n")
