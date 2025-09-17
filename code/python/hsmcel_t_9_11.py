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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M, point_N = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算单位正方体中点 C 到截面 MB1ND 的距离

    参数:
    len_a (float): 正方体边长

    返回:
    float: 距离
    """
    return math.sqrt(6) / 3 * len_a


# 题干给定的数值
len_a = 1.0  # 正方体边长

# 验证输出
# distance = calculate(len_a)
# print(f"点C到截面MB1ND的距离: {distance:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_9_11",
    "type": 3,
    "level": 2,
    "cn_problem": f"在边长为{len_a}的正方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}中，{point_M}、{point_N}分别为{point_A}{point_B}、{point_C1}{point_D1}的中点，求点{point_C}到截面{point_M}{point_B1}{point_N}{point_D}的距离。",
    "en_problem": f"In a cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} with edge length {len_a}, {point_M} and {point_N} are midpoints of {point_A}{point_B} and {point_C1}{point_D1} respectively. Find the distance from point {point_C} to the cross-section {point_M}{point_B1}{point_N}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_9_11({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
