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
point_A, point_B, point_C, point_D, point_M = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_s, len_p):
    """
    计算三角函数 sinθ 的值，基于给定的公式：
    sinθ = (√3 * len_s) / (2 * √(len_s² + len_p²))

    参数:
    len_s (float): 长度参数（需为正数，代表实际长度）
    len_p (float): 长度参数（需为正数，代表实际长度）

    返回:
    float: 计算得到的 sinθ 值
    """
    # 计算分子：√3 * len_s
    numerator = math.sqrt(3) * len_s

    # 计算分母中的根号部分：√(len_s² + len_p²)
    sqrt_inner = math.sqrt(len_s ** 2 + len_p ** 2)
    # 计算分母：2 * 根号部分
    denominator = 2 * sqrt_inner

    # 计算 sinθ
    sin_theta = numerator / denominator
    return sin_theta


len_s = 2.0
len_p = 2 * math.sqrt(3)
# result1 = calculate(len_s, len_p)
# print(f"当 len_s={len_s}，len_p={len_p} 时，sinθ={result1:.4f}")
# Generate random lengths
len_s = round(len_scaling_factor * float(len_s), 2)
len_p = round(len_scaling_factor * float(len_p), 2)

# Calculate the result
result = calculate(len_s, len_p)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_5_1_3",
    "type": 2,
    "level": 2,
    "cn_problem": f"在四面体 {point_A}{point_B}{point_C}{point_D} 中：\n- 底面 △{point_A}{point_B}{point_C} 是等边三角形，边长 {len_s} ({len_s}>0)；\n- 平面 {point_A}{point_B}{point_C} ⟂ 平面 {point_A}{point_B}{point_D}；\n- 侧棱 {point_A}{point_D} = {len_p} ({len_p}>0)，且 ∠{point_B}{point_A}{point_D} = 90°；\n- 点 {point_M} 为棱 {point_A}{point_B} 的中点。\n求直线 {point_C}{point_D} 与平面 {point_A}{point_B}{point_D} 所成锐角 θ 的正弦值。",
    "en_problem": f"In tetrahedron {point_A}{point_B}{point_C}{point_D}:\n- The base △{point_A}{point_B}{point_C} is equilateral with side length {len_s} ({len_s}>0);\n- Plane {point_A}{point_B}{point_C} is perpendicular to plane {point_A}{point_B}{point_D};\n- Lateral edge {point_A}{point_D} = {len_p} ({len_p}>0) with ∠{point_B}{point_A}{point_D} = 90°;\n- Point {point_M} is the midpoint of {point_A}{point_B}.\nFind sin θ, where θ is the acute angle between line {point_C}{point_D} and plane {point_A}{point_B}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_5_1_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}')"}, ensure_ascii=False) + "\n")
