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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math

def calculate(len_a, len_b, len_c):
    """
    计算长方体截面的最大和最小面积

    参数:
    len_a (float): DA 边长
    len_b (float): DC 边长
    len_c (float): DD1 边长

    返回:
    tuple: (最大截面面积, 最小截面面积)
    """
    # 最大截面面积公式
    area_Smax = math.pi * (len_a ** 2 + len_b ** 2 + len_c ** 2) / 4


    return area_Smax


# 定义题干中的参数
len_a = 1.0   # AD


# 验证计算结果
# max_area, min_area = calculate(len_a, len_b, len_c)
# print(f"最大截面面积: {max_area:.6f}, 最小截面面积: {min_area:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = len_a*2
len_c = len_a*2

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_23_2_1",
    "type": 4,
    "level": 2,
    "cn_problem": f"在长方体 {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1} 中，设  {point_A}{point_D} = {len_a}，{point_A}{point_A1} = {point_A}{point_B} = 2*{len_a}（{len_a} > 0），{point_M} 为棱 {point_D}{point_D1} 的中点。过 {point_A1}{point_M} 作该长方体外接球的截面，求截面面积的最大值。",
    "en_problem": f"In the cuboid {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1}, let {point_A}{point_D} = {len_a}, {point_A}{point_A1} = {point_A}{point_B} = 2*{len_a} ({len_a} > 0), and let {point_M} be the midpoint of edge {point_D}{point_D1}. Find the maximum area of the cross-section passing through {point_A1}{point_M} of the circumscribed sphere of the cuboid.",
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
    f.write(json.dumps({json_data["id"]: f"area2_23_2_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_M}')"}, ensure_ascii=False) + "\n")
