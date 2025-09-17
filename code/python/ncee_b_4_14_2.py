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
point_P, point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_a):
    """
    计算特定几何体的侧面积 S_lat

    参数:
        len_a (float): 特征长度参数 a（与几何体尺寸直接相关的长度量）

    返回:
        float: 几何体的侧面积计算结果

    公式:
        S_lat = (len_a² / 2) × (3 + √3)
    """
    return (len_a ** 2) / 2 * (3 + math.sqrt(3))

len_a = 2.0
# s_lat = calculate(len_a)
#
# print(f"侧面积 S_lat = {s_lat:.4f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_14_2",
    "type": 4,
    "level": 2,
    "cn_problem": f"设四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 满足：底面 {point_A}{point_B}{point_C}{point_D} 为等腰梯形，{point_A}{point_B}∥{point_C}{point_D}，{point_A}{point_B}={point_C}{point_D}={len_a}（{len_a}>0），{point_A}{point_D}={point_B}{point_C}=√2*{len_a}；侧棱 {point_P}{point_A}={point_P}{point_D}={len_a}；且 ∠{point_A}{point_P}{point_B}=∠{point_C}{point_P}{point_D}=90°，∠{point_B}{point_P}{point_C}=60°。求四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 的侧面积 S_lat。",
    "en_problem": f"Consider pyramid {point_P}-{point_A}{point_B}{point_C}{point_D} where: the base {point_A}{point_B}{point_C}{point_D} is an isosceles trapezoid with {point_A}{point_B}∥{point_C}{point_D}, {point_A}{point_B}={point_C}{point_D}={len_a} ({len_a}>0), {point_A}{point_D}={point_B}{point_C}=√2*{len_a}; lateral edges {point_P}{point_A}={point_P}{point_D}={len_a}; angles ∠{point_A}{point_P}{point_B}=∠{point_C}{point_P}{point_D}=90°, ∠{point_B}{point_P}{point_C}=60°. Find the lateral surface area S_lat of pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_14_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
