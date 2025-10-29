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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M, point_N, point_E = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math


def calculate(len_p, len_k, len_n, len_q):
    """计算len_t的值（公式：[√(len_p²(1-len_k²)-len_n²len_k²)]/(2len_k) - √(len_q² - len_n²/4)）"""
    # 计算第一部分的分子：√[len_p²(1-len_k²) - len_n²len_k²]
    numerator_part1 = math.sqrt(len_p ** 2 * (1 - len_k ** 2) - len_n ** 2 * len_k ** 2)
    # 第一部分整体：分子 / (2len_k)
    part1 = numerator_part1 / (2 * len_k)

    # 计算第二部分的内部表达式：len_q² - (len_n²)/4
    inside_sqrt_part2 = len_q ** 2 - (len_n ** 2) / 4
    # 第二部分：√(内部表达式)
    part2 = math.sqrt(inside_sqrt_part2)

    # len_t为两部分之差
    return part1 - part2


# 测试示例
len_m = 1.0
len_p = 2.0
len_k = 1 / 3
len_n = 2.0
len_q = math.sqrt(5)

# print(calculate(len_p, len_k, len_n, len_q))

# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)
len_n = round(len_scaling_factor * float(len_n), 2)
len_p = round(len_scaling_factor * float(len_p), 2)
len_q = round(len_scaling_factor * float(len_q), 2)

# Calculate the result
result = calculate(len_p, len_k, len_n, len_q)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_8_7_3",
    "type": 3,
    "level": 2,
    "cn_problem": f"在四棱柱{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}中，侧棱{point_A1}{point_A}⊥底面{point_A}{point_B}{point_C}{point_D}，{point_A}{point_B}⊥{point_A}{point_C}。设{point_A}{point_B}={len_m}，{point_A}{point_C}={len_n}，{point_A}{point_A1}={len_p}，{point_A}{point_D}={point_C}{point_D}={len_q}，且点{point_M}和{point_N}分别为{point_B1}{point_C}和{point_D1}{point_D}的中点。设{point_E}为棱{point_A1}{point_B1}上的点，若直线{point_N}{point_E}和平面{point_A}{point_B}{point_C}{point_D}所成角的正弦值为{len_k}，求线段{point_A1}{point_E}的长。",
    "en_problem": f"In quadrilateral prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, lateral edge {point_A1}{point_A}⊥base {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B}⊥{point_A}{point_C}. Let {point_A}{point_B}={len_m}, {point_A}{point_C}={len_n}, {point_A}{point_A1}={len_p}, {point_A}{point_D}={point_C}{point_D}={len_q}, and points {point_M} and {point_N} are midpoints of {point_B1}{point_C} and {point_D1}{point_D} respectively. Let {point_E} be a point on edge {point_A1}{point_B1}, if the sine value of the angle between line {point_N}{point_E} and plane {point_A}{point_B}{point_C}{point_D} is {len_k}, find the length of segment {point_A1}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_8_7_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_M}', '{point_N}', '{point_E}')"}, ensure_ascii=False) + "\n")
