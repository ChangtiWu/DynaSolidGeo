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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D, point_E = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a, len_h, len_m, len_n):
    """
    计算给定的几何表达式

    参数:
    len_a (float): AC = BC 的长度
    len_h (float): CC₁ 的长度
    len_m (float): AD 的长度
    len_n (float): CE 的长度

    返回:
    float: 计算结果
    """
    numerator = abs(len_m - len_h)
    denominator = math.sqrt(2) * math.sqrt((len_m - len_n) ** 2 + (len_h - len_n) ** 2 + len_a ** 2)
    result = numerator / denominator
    return result


# 定义题干参数
len_a = 2.0
len_h = 3.0
len_m = 1.0
len_n = 2.0

# 验证输出（与参考答案对比）
# result = calculate(len_a, len_h, len_m, len_n)
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)
len_m = round(len_scaling_factor * float(len_m), 2)
len_n = round(len_scaling_factor * float(len_n), 2)

# Calculate the result
result = calculate(len_a, len_h, len_m, len_n)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_13_3",
    "type": 2,
    "level": 2,
    "cn_problem": f"设三棱柱{point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}中，{point_C}{point_C1}⊥平面{point_A}{point_B}{point_C}，{point_A}{point_C}⊥{point_B}{point_C}，{point_A}{point_C}={point_B}{point_C}={len_a}，{point_C}{point_C1}={len_h}，点{point_D}在棱{point_A}{point_A1}上且{point_A}{point_D}={len_m}，点{point_E}在棱{point_C}{point_C1}上且{point_C}{point_E}={len_n}。求直线{point_A}{point_B}与平面{point_D}{point_B1}{point_E}所成角的正弦值。",
    "en_problem": f"In triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, {point_C}{point_C1}⊥plane {point_A}{point_B}{point_C}, {point_A}{point_C}⊥{point_B}{point_C}, {point_A}{point_C}={point_B}{point_C}={len_a}, {point_C}{point_C1}={len_h}, point {point_D} is on edge {point_A}{point_A1} with {point_A}{point_D}={len_m}, point {point_E} is on edge {point_C}{point_C1} with {point_C}{point_E}={len_n}. Find the sine of the angle between line {point_A}{point_B} and plane {point_D}{point_B1}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"sup_13_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
