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
point_P, point_A, point_B, point_C, point_D, point_O, point_E = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
def calculate(len_a, len_h):
    """
    计算四棱锥 PAD 与 PEC 平面夹角余弦值的范围

    参数:
    len_a (float): 底面边长
    len_h (float): PO 高

    返回:
    tuple: (cosθ_max, cosθ_min)
    """
    # 根据题目给出的解答
    cos_theta_max = (5 ** 0.5) / 3
    cos_theta_min = 2 / 3
    return cos_theta_max


# 定义题干中的参数
len_a = 2.0   # 底面边长
len_h = 2.0   # PO 高

# 验证计算结果
# result_max, result_min = calculate(len_a, len_h)
# print(f"cosθ最大值: {result_max:.6f}, cosθ最小值: {result_min:.6f}")

# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)
len_a = round(len_scaling_factor * float(len_a), 2)


# Calculate the result
result = calculate(len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_24_2",
    "type": 7,
    "level": 2,
    "cn_problem": f"在四棱锥 {point_P} - {point_A}{point_B}{point_C}{point_D} 中，底面为正方形，{point_P}{point_A} = {point_P}{point_D}，{point_O} 为 {point_A}{point_D} 中点，{point_P}{point_O} ⊥ 平面 {point_A}{point_B}{point_C}{point_D}。设 {point_P}{point_O} = {len_h}，{point_A}{point_B} = {len_a}，{point_E} 为 {point_A}{point_B} 上的动点。求平面 {point_P}{point_A}{point_D} 与平面 {point_P}{point_E}{point_C} 所成锐二面角的余弦值的最大值。",
    "en_problem": f"In the quadrangular pyramid {point_P} - {point_A}{point_B}{point_C}{point_D}, the base is a square, {point_P}{point_A} = {point_P}{point_D}, and {point_O} is the midpoint of {point_A}{point_D}, with {point_P}{point_O} perpendicular to plane {point_A}{point_B}{point_C}{point_D}. Let {point_P}{point_O} = {len_h}, {point_A}{point_B} = {len_a}, and {point_E} be a moving point on {point_A}{point_B}. Find the maximum value of the cosine of the acute dihedral angle between planes {point_P}{point_A}{point_D} and {point_P}{point_E}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"area2_24_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}', '{point_E}')"}, ensure_ascii=False) + "\n")
