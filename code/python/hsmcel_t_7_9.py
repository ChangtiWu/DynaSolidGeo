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
point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_a, len_m, len_n):
    """
    计算正四面体 AB-C-D 中线段 EF 的长度

    参数:
    len_a (float): 四面体棱长 AB=CD=AC=AD=BC=BD
    len_m (float): AE 的长度
    len_n (float): CF 的长度

    返回:
    float: EF 长度
    """
    return math.sqrt(len_a**2 + len_m**2 + len_n**2 - len_a*len_m - len_a*len_n)


# 题干给定的数值
len_a = 6.0  # 棱长
len_m = 1.0  # AE
len_n = 2.0  # CF

# 验证输出
#ef_length = calculate(len_a, len_m, len_n)
#print(f"EF 长度: {ef_length:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_m = round(len_scaling_factor * float(len_m), 2)
len_n = round(len_scaling_factor * float(len_n), 2)

# Calculate the result
result = calculate(len_a, len_m, len_n)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_7_9",
    "type": 3,
    "level": 2,
    "cn_problem": f"正四面体{point_A}{point_B}{point_C}{point_D}的棱长为{len_a}，在棱{point_A}{point_B}上有一点{point_E}，满足{point_A}{point_E} = {len_m}；在棱{point_C}{point_D}上有一点{point_F}，满足{point_C}{point_F} = {len_n}。求线段{point_E}{point_F}的长度。",
    "en_problem": f"Regular tetrahedron {point_A}{point_B}{point_C}{point_D} has edge length {len_a}. Point {point_E} is on edge {point_A}{point_B} with {point_A}{point_E} = {len_m}, and point {point_F} is on edge {point_C}{point_D} with {point_C}{point_F} = {len_n}. Find the length of segment {point_E}{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_7_9({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
