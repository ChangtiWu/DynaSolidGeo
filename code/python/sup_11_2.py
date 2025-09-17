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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_E, point_F, point_D = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math


def calculate(len_a):
    """
    计算给定的几何表达式

    参数:
    len_a (float): AB = BC = 棱长

    返回:
    float: 计算结果
    """
    # 根据题干解法，B₁D = len_a / 4
    result = len_a / 4
    return result


# 定义题干参数
len_a = 2.0

# 验证输出（与参考答案对比）
# result = calculate(len_a)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_11_2",
    "type": 7,
    "level": 2,
    "cn_problem": f"已知直三棱柱{point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}中，侧面{point_A}{point_A1}{point_B1}{point_B}为正方形（故{point_A}{point_B}={point_B}{point_B1}={len_a}），且{point_A}{point_B}={point_B}{point_C}={len_a}。{point_E}为{point_A}{point_C}中点，{point_F}为{point_C}{point_C1}中点，{point_D}为棱{point_A1}{point_B1}上的点，满足{point_B}{point_F}⊥{point_A1}{point_B1}。求：当{point_B1}{point_D}为何值时，平面{point_B}{point_B1}{point_C1}{point_C}与平面{point_D}{point_F}{point_E}所成二面角的正弦值最小？",
    "en_problem": f"In a right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, lateral face {point_A}{point_A1}{point_B1}{point_B} is a square (so {point_A}{point_B}={point_B}{point_B1}={len_a}), and {point_A}{point_B}={point_B}{point_C}={len_a}. {point_E} is the midpoint of {point_A}{point_C}, {point_F} is the midpoint of {point_C}{point_C1}, {point_D} is a point on edge {point_A1}{point_B1} such that {point_B}{point_F}⊥{point_A1}{point_B1}. Find: for what value of {point_B1}{point_D} is the sine of the dihedral angle between plane {point_B}{point_B1}{point_C1}{point_C} and plane {point_D}{point_F}{point_E} minimized?",
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
    f.write(json.dumps({json_data["id"]: f"sup_11_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_E}', '{point_F}', '{point_D}')"}, ensure_ascii=False) + "\n")
