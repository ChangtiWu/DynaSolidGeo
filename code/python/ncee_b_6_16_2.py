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
point_A, point_B, point_C, point_A1, point_A4, point_E, point_F = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate():
    r"""
    计算固定正弦值 $\sin\theta = \frac{3}{5}$。

    返回:
    float: 固定正弦值（0.6）
    """
    # 直接返回 3/5 的结果
    return 3 / 5


len_b = math.sqrt(3)
len_h = 1.0  # 原题中侧棱的高度,任意正数

# result = calculate()
# print(f"sin_theta的值为：{result:.4f}")

# Generate random lengths
len_b = round(len_scaling_factor * float(len_b), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_16_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"设底面直角三角形 {point_A}{point_B}{point_C} 满足 ∠{point_A}{point_B}{point_C}=90°, ∠{point_B}{point_A}{point_C}=30°，并令 {point_B}{point_C}={len_b}(>0)；\n- 侧棱垂直底面，柱高取 {len_h}(>0)；\n- 在侧棱 {point_A}{point_A1} 上取点 {point_A4} 使 {point_A}{point_A4}:{point_A4}{point_C} = 1:1 (即 {point_A4}{point_A} = {point_A4}{point_C})；\n- 记 {point_E} 为 {point_A}{point_C} 的中点，{point_F} 为 {point_A4}{point_B} 的中点。\n设 θ 为直线 {point_E}{point_F} 与平面 {point_A}{point_B}{point_C} 所成锐角。求 sin θ。",
    "en_problem": f"Let the base right triangle {point_A}{point_B}{point_C} satisfy ∠{point_A}{point_B}{point_C}=90° and ∠{point_B}{point_A}{point_C}=30°, taking {point_B}{point_C}={len_b}(>0);\n- The prism is right: lateral edges are perpendicular to the base with height {len_h}(>0);\n- On edge {point_A}{point_A1} choose point {point_A4} so that {point_A}{point_A4}:{point_A4}{point_C}=1:1 (hence {point_A4}{point_A}={point_A4}{point_C});\n- Let {point_E} be the midpoint of {point_A}{point_C} and {point_F} the midpoint of {point_A4}{point_B}.\nLet θ be the acute angle between line {point_E}{point_F} and the base plane {point_A}{point_B}{point_C}. Find sin θ.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_16_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_A4}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
