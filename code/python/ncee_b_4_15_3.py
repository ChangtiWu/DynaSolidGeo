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
point_P, point_A, point_B, point_C, point_D, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
def calculate(len_a):
    """
    计算特定几何体的体积 V_{point_E-B C D}

    参数:
        len_a (float): 特征长度参数 a（与几何体尺寸直接相关的长度量）

    返回:
        float: 几何体的体积计算结果

    公式:
        V = (len_a³) / 24
    """
    return (len_a ** 3) / 24

len_a = 2.0
# volume = calculate(len_a)
#
# print(f"几何体体积 V = {volume:.4f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_15_3",
    "type": 5,
    "level": 2,
    "cn_problem": f"在三棱锥 {point_P}-{point_A}{point_B}{point_C} 中满足：{point_A}{point_B}⊥{point_B}{point_C}，{point_A}{point_B}⊥{point_P}{point_A}，{point_B}{point_C}⊥{point_P}{point_A}（三条棱两两垂直）；三条互相垂直的棱长都相等：{point_P}{point_A}={point_A}{point_B}={point_B}{point_C}={len_a}（{len_a}>0）；点 {point_D} 为底面对角线 {point_A}{point_C} 的中点；点 {point_E} 位于棱 {point_P}{point_C} 上，使直线 {point_P}{point_A}∥平面 {point_B}{point_D}{point_E}。求三棱锥 {point_E}-{point_B}{point_C}{point_D} 的体积 V_{{{point_E}-{point_B}{point_C}{point_D}}}。",
    "en_problem": f"In triangular pyramid {point_P}-{point_A}{point_B}{point_C}, the following conditions hold: {point_A}{point_B}⊥{point_B}{point_C}, {point_A}{point_B}⊥{point_P}{point_A}, {point_B}{point_C}⊥{point_P}{point_A} (three edges are mutually perpendicular); the three mutually perpendicular edges have equal length: {point_P}{point_A}={point_A}{point_B}={point_B}{point_C}={len_a} (where {len_a}>0); point {point_D} is the midpoint of diagonal {point_A}{point_C} on the base; point {point_E} lies on edge {point_P}{point_C} such that line {point_P}{point_A}∥plane {point_B}{point_D}{point_E}. Find the volume V_{{{point_E}-{point_B}{point_C}{point_D}}} of triangular pyramid {point_E}-{point_B}{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_15_3({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
