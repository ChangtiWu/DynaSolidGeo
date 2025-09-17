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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_A2, point_B2, point_D2, point_C2, point_P = random.sample(string.ascii_uppercase, 13)

# Add result calculation code
import math


def calculate(len_a, len_h):
    """计算len_result的值（公式：√[(len_a² + 2len_h²)/6]）"""
    numerator = len_a ** 2 + 2 * (len_h ** 2)
    return math.sqrt(numerator / 6)


# 测试示例
len_a = 2.0
len_h = 1.0

# print(calculate(len_a, len_h))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_8_2_2",
    "type": 3,
    "level": 2,
    "cn_problem": f"如图，设正四棱柱 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 满足：(1) 底面 {point_A}{point_B}{point_C}{point_D} 为正方形，边长为 {len_a}>0；(2) 侧棱垂直底面，柱高为 4*{len_h}（{len_h}>0）。在四条侧棱上分别取点：{point_A}{point_A2}={len_h}，{point_B}{point_B2}={point_D}{point_D2}=2*{len_h}，{point_C}{point_C2}=3*{len_h}。设点 {point_P} 在棱 {point_B}{point_B1} 上，记 {point_B}{point_P}∈[0,4*{len_h}]。若二面角 ∠({point_P}-{point_A2}{point_C2}-{point_D2})=150°，求线段 {point_B2}{point_P} 的长度。",
    "en_problem": f"As shown, consider a right square prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} where: (1) the base {point_A}{point_B}{point_C}{point_D} is a square with side length {len_a}>0; (2) the lateral edges are perpendicular to the base with height 4*{len_h} ({len_h}>0). Points are taken on the four lateral edges: {point_A}{point_A2}={len_h}, {point_B}{point_B2}={point_D}{point_D2}=2*{len_h}, {point_C}{point_C2}=3*{len_h}. Let point {point_P} be on edge {point_B}{point_B1} with {point_B}{point_P}∈[0,4*{len_h}]. If the dihedral angle ∠({point_P}-{point_A2}{point_C2}-{point_D2})=150°, find the length of segment {point_B2}{point_P}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_8_2_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_A2}', '{point_B2}', '{point_D2}', '{point_C2}', '{point_P}')"}, ensure_ascii=False) + "\n")
