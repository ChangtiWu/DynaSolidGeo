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
point_S, point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
def calculate(len_a, len_b):
    """
    计算余弦值 cosθ，基于给定的公式：
    cosθ = len_a / (2 * len_b)

    参数:
    len_a (float): 分子参数（代表实际长度或其他正数）
    len_b (float): 分母参数（需为非零实数，代表实际长度或其他数值）

    返回:
    float: 计算得到的 cosθ 值
    """
    # 计算分母：2 * len_b
    denominator = 2 * len_b
    # 计算 cosθ
    cos_theta = len_a / denominator
    return cos_theta

len_a = 3.0
len_b = 2.0
# result1 = calculate(len_a, len_b)
# print(f"当 len_a={len_a}，len_b={len_b} 时，cosθ≈{result1:.4f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_5_7_1",
    "type": 2,
    "level": 1,
    "cn_problem": f"在四棱锥 {point_S}-{point_A}{point_B}{point_C}{point_D} 中，底面 {point_A}{point_B}{point_C}{point_D} 是边长为 {len_a} 的正方形，平面 {point_S}{point_A}{point_D} 垂直于平面 {point_A}{point_B}{point_C}{point_D}，且 {point_S}{point_A} = {point_S}{point_D} = {len_b}。\n\n求异面直线 {point_S}{point_A} 与 {point_B}{point_C} 所成角的余弦值。",
    "en_problem": f"In pyramid {point_S}-{point_A}{point_B}{point_C}{point_D}, the base {point_A}{point_B}{point_C}{point_D} is a square with side length {len_a}, the plane {point_S}{point_A}{point_D} is perpendicular to the plane {point_A}{point_B}{point_C}{point_D}, and {point_S}{point_A} = {point_S}{point_D} = {len_b}.\n\nFind the cosine of the angle between the skew lines {point_S}{point_A} and {point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_5_7_1({mode}, {azimuth}, {elevation}, '{point_S}', '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
