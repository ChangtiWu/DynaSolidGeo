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
point_C, point_D, point_A, point_B, point_P, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate():
    r"""
    计算固定正弦值 $\sin\theta = \frac{\sqrt{2}}{8}$。

    返回:
    float: 固定正弦值（约0.1768）
    """
    # 计算分子：√2
    numerator = math.sqrt(2)
    # 计算分母：8
    denominator = 8
    # 计算正弦值
    sin_theta = numerator / denominator
    return sin_theta


len_d = 1.0

# result = calculate()
# print(f"sin_theta的值为：{result:.4f}")
# Generate random lengths
len_d = round(len_scaling_factor * float(len_d), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_23_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"把底棱 {point_C}{point_D} 的长度统一记作 {len_d}(>0)，并按题设比例保持\n{point_A}{point_D}=2*{len_d},\n{point_B}{point_C}={len_d},\n{point_P}{point_C}=2*{len_d}。\n其它几何条件不变：\n- △{point_P}{point_A}{point_D} 为等腰直角三角形（斜边 {point_A}{point_D}），\n- {point_B}{point_C} ∥ {point_A}{point_D},\n- {point_C}{point_D} ⟂ {point_A}{point_D},\n- {point_E} 为 {point_P}{point_D} 的中点。\n设 θ 为直线 {point_C}{point_E} 与平面 {point_P}{point_B}{point_C} 所成的锐角。求 sin θ。",
    "en_problem": f"Introduce a scale {len_d}(>0) for the base edge {point_C}{point_D}. Keep the given ratios\n{point_A}{point_D}=2*{len_d},\n{point_B}{point_C}={len_d},\n{point_P}{point_C}=2*{len_d},\nwith all original perpendicular and parallel relations:\n- △{point_P}{point_A}{point_D} is an isosceles right triangle on hypotenuse {point_A}{point_D},\n- {point_B}{point_C} ∥ {point_A}{point_D},\n- {point_C}{point_D} ⟂ {point_A}{point_D},\n- {point_E} is the midpoint of {point_P}{point_D}.\nLet θ be the acute angle between line {point_C}{point_E} and plane {point_P}{point_B}{point_C}. Find sin θ .",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_23_2({mode}, {azimuth}, {elevation}, '{point_C}', '{point_D}', '{point_A}', '{point_B}', '{point_P}', '{point_E}')"}, ensure_ascii=False) + "\n")
