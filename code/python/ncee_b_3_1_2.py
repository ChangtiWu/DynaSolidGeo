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
point_A, point_B, point_C, point_D, point_E, point_F, point_M = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_a, len_b, len_c):
    """
    计算给定的几何表达式

    参数:
    len_a (float): 长度参数 a
    len_b (float): 长度参数 b
    len_c (float): 长度参数 c

    返回:
    float: 计算结果
    """
    # 计算分子: len_a * len_c * sqrt(len_b^2 - (len_a^2)/4)
    numerator = len_a * len_c * math.sqrt(len_b ** 2 - (len_a ** 2) / 4)

    # 计算分母中的平方项: (len_a^2 + len_c^2 - len_b^2)
    inner_expr = len_a ** 2 + len_c ** 2 - len_b ** 2

    # 计算分母: sqrt(4 * len_a^2 * len_c^2 - inner_expr^2)
    denominator = math.sqrt(4 * (len_a ** 2) * (len_c ** 2) - inner_expr ** 2)

    # 返回分子除以分母的结果
    return numerator / denominator

len_a=2.0
len_b=math.sqrt(10)
len_c=2 * math.sqrt(3)

# result = calculate(
#     len_a=2.0,
#     len_b=math.sqrt(10),
#     len_c=2 * math.sqrt(3)
# )
# print(f"计算结果: {result:.6f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_3_1_2",
    "type": 3,
    "level": 2,
    "cn_problem": f"已知 {point_A}{point_B} \\parallel {point_C}{point_D} \\parallel {point_E}{point_F}，且 {point_A}{point_B}={point_D}{point_E}={point_E}{point_F}={point_C}{point_F}={len_a}，{point_C}{point_D}=2*{len_a}，{point_A}{point_D}={point_B}{point_C}={len_b}，{point_A}{point_E}={len_c}（其中 {len_a},{len_b},{len_c}>0，且 \\triangle {point_A}{point_D}{point_E} 能构成）。设 {point_M} 为 {point_C}{point_D} 的中点。求点 {point_M} 到平面 {point_A}{point_D}{point_E} 的距离。",
    "en_problem": f"As shown, {point_A}{point_B} \\parallel {point_C}{point_D} \\parallel {point_E}{point_F}. Given {point_A}{point_B}={point_D}{point_E}={point_E}{point_F}={point_C}{point_F}={len_a}, {point_C}{point_D}=2*{len_a}, {point_A}{point_D}={point_B}{point_C}={len_b}, and {point_A}{point_E}={len_c} (where {len_a},{len_b},{len_c}>0 and triangle {point_A}{point_D}{point_E} is valid). Let {point_M} be the midpoint of {point_C}{point_D}. Find the distance from {point_M} to the plane {point_A}{point_D}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_3_1_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_M}')"}, ensure_ascii=False) + "\n")
