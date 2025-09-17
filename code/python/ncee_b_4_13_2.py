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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_M = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_h, len_p, len_q):
    """
    计算角度 θ（弧度制），由反正切函数定义

    参数:
        len_h (float): 高度参数 h
        len_p (float): 水平参数 p
        len_q (float): 水平参数 q

    返回:
        float: 角度 θ（弧度制）

    公式:
        θ = arctan( (2h) / √(p² + q²) )
    """
    # 计算分子：2 * len_h
    numerator = 2 * len_h

    # 计算分母：√(len_p² + len_q²)
    denominator = math.sqrt(len_p ** 2 + len_q ** 2)

    # 计算反正切值（弧度制）
    return math.atan(numerator / denominator)

len_h = 5.0
len_p = 4.0
len_q = 2.0
# theta = calculate(len_h, len_p, len_q)
#
# print(f"θ（弧度）= {theta:.6f}")  # 输出: θ（弧度）= 0.785398（即 π/4）
# Generate random lengths
len_p = round(len_scaling_factor * float(len_p), 2)
len_q = round(len_scaling_factor * float(len_q), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_h, len_p, len_q)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_13_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，底面 \\triangle {point_A}{point_B}{point_C} 为直角三角形，且 {point_A}{point_B} = {len_p}，{point_A}{point_C} = {len_q}，∠{point_B}{point_A}{point_C} = 90°（{len_p},{len_q}>0）。侧棱皆垂直于底面，设 {point_A}{point_A1} = {len_h}（{len_h}>0）。记 {point_M} 为 {point_B}{point_C} 的中点。求直线 {point_A1}{point_M} 与平面 {point_A}{point_B}{point_C} 所成角的大小。",
    "en_problem": f"In the right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, the base \\triangle {point_A}{point_B}{point_C} is a right triangle with {point_A}{point_B} = {len_p}, {point_A}{point_C} = {len_q}, and ∠{point_B}{point_A}{point_C} = 90° (where {len_p},{len_q}>0). The lateral edges are perpendicular to the base, and {point_A}{point_A1} = {len_h} ({len_h}>0). Let {point_M} be the midpoint of {point_B}{point_C}. Find the angle between line {point_A1}{point_M} and plane {point_A}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_13_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_M}')"}, ensure_ascii=False) + "\n")
