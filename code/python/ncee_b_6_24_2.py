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


import math

def calculate(len_a, len_b):
    """
    计算四棱锥 P-ABCD 中二面角 B-PD-A 的大小

    参数:
    len_a (float): 正方形底面边长 (AB = AD = len_a)
    len_b (float): PA = PD 的长度

    返回:
    float: 二面角大小 (弧度制)
    """
    numerator = math.sqrt(4 * len_b**2 - len_a**2)
    denominator = math.sqrt(8 * len_b**2 - len_a**2)
    return math.acos(numerator / denominator)


# ====== 验证例子 ======
len_a = 4
len_b = math.sqrt(6)

#theta = dihedral_angle(len_a, len_b)
# print(f"二面角大小: {math.degrees(theta):.6f}°")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_24_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}中，底面{point_A}{point_B}{point_C}{point_D}为正方形（边长{point_A}{point_B} = {point_A}{point_D} = {len_a}），平面{point_P}{point_A}{point_D} ⊥ 平面{point_A}{point_B}{point_C}{point_D}，且{point_P}{point_A} = {point_P}{point_D} = {len_b}。求二面角{point_B}-{point_P}{point_D}-{point_A}的大小。",
    "en_problem": f"In pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, the base {point_A}{point_B}{point_C}{point_D} is a square with side length {point_A}{point_B} = {point_A}{point_D} = {len_a}, plane {point_P}{point_A}{point_D} ⊥ plane {point_A}{point_B}{point_C}{point_D}, and {point_P}{point_A} = {point_P}{point_D} = {len_b}. Find the measure of dihedral angle {point_B}-{point_P}{point_D}-{point_A}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_24_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
