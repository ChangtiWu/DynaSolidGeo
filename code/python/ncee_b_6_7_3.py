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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math


def calculate():
    r"""
    计算固定余弦值 $\cos\theta = \frac{\sqrt{10}}{10}$。

    返回:
    float: 固定余弦值（约0.3162）
    """
    # 计算分子：√10
    numerator = math.sqrt(10)
    # 计算分母：10
    denominator = 10
    # 计算余弦值
    cos_theta = numerator / denominator
    return cos_theta


len_a = 2.0

# result = calculate()
# print(f"cos_theta的值为：{result:.4f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_7_3",
    "type": 2,
    "level": 2,
    "cn_problem": f"在直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中：\n- 设公共边长 {len_a} > 0，使 {point_A}{point_B} = {point_A}{point_C} = {point_A}{point_A1} = {len_a}；\n- {point_A}{point_A1} ⟂ 平面 {point_A}{point_B}{point_C}，且 {point_A}{point_C} ⟂ {point_A}{point_B}；\n- {point_D} 为 {point_A1}{point_B1} 的中点，{point_E} 为 {point_A}{point_A1} 的中点，{point_F} 为 {point_C}{point_D} 的中点。\n设 θ 为平面 {point_A1}{point_C}{point_D} 与平面 {point_C}{point_C1}{point_D} 所成的锐角。求 cos θ。",
    "en_problem": f"In the right prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}:\n- All edges from {point_A} have equal length {len_a} (>0), i.e. {point_A}{point_B} = {point_A}{point_C} = {point_A}{point_A1} = {len_a};\n- Edge {point_A}{point_A1} is perpendicular to the base plane {point_A}{point_B}{point_C}, and {point_A}{point_C} ⟂ {point_A}{point_B};\n- {point_D} is the midpoint of {point_A1}{point_B1}; {point_E} is the midpoint of {point_A}{point_A1}; {point_F} is the midpoint of {point_C}{point_D}.\nLet θ be the acute angle between planes {point_A1}{point_C}{point_D} and {point_C}{point_C1}{point_D}. Find cos θ (note: the value is independent of {len_a}).",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_7_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
