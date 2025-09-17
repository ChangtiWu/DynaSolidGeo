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
point_A, point_B1, point_C, point_D1, point_B, point_D, point_A1, point_C1 = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math

def calculate(len_m, len_n, len_p):
    """
    计算四面体 A-B1CD1 外接球的表面积

    参数:
    len_m (float): AD₁
    len_n (float): AC
    len_p (float): AB₁

    返回:
    float: 外接球表面积
    """
    # 根据题解公式 S = π * (len_m^2 + len_n^2 + len_p^2) / 2
    return math.pi * (len_m ** 2 + len_n ** 2 + len_p ** 2) / 2


# 定义题干中的参数
len_m = math.sqrt(3)
len_n = 2.0
len_p = math.sqrt(5)

# 验证计算结果
#result = calculate(len_m, len_n, len_p)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)
len_n = round(len_scaling_factor * float(len_n), 2)
len_p = round(len_scaling_factor * float(len_p), 2)

# Calculate the result
result = calculate(len_m, len_n, len_p)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_8_2",
    "type": 4,
    "level": 1,
    "cn_problem": f"若四面体 {point_A} - {point_B1}{point_C}{point_D1} 的四个顶点均为长方体 {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1} 的顶点，且 {point_A}{point_D1} = {len_m}，{point_A}{point_C} = {len_n}，{point_A}{point_B1} = {len_p}，求四面体 {point_A} - {point_B1}{point_C}{point_D1} 外接球的表面积。",
    "en_problem": f"If the four vertices of tetrahedron {point_A} - {point_B1}{point_C}{point_D1} are all vertices of rectangular box {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1}, and {point_A}{point_D1} = {len_m}, {point_A}{point_C} = {len_n}, {point_A}{point_B1} = {len_p}, find the surface area of the circumsphere of tetrahedron {point_A} - {point_B1}{point_C}{point_D1}.",
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
    f.write(json.dumps({json_data["id"]: f"area2_8_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B1}', '{point_C}', '{point_D1}', '{point_B}', '{point_D}', '{point_A1}', '{point_C1}')"}, ensure_ascii=False) + "\n")
