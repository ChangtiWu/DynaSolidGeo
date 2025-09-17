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
point_P, point_A, point_B, point_C, point_D, point_M, point_N = random.sample(string.ascii_uppercase, 7)

# Add result calculation code

import math

def calculate(len_a, len_h):
    """
    计算四棱锥 P-ABCD 中二面角 M-DN-C 的正切值

    参数:
    len_a (float): 底面正方形边长
    len_h (float): PD 高度

    返回:
    float: 正切值
    """
    return math.sqrt(5) * len_h / len_a


# 题干给定的数值
len_a = 4.0   # 底面正方形边长
len_h = 6.0   # PD 高

# 验证输出
# tan_value = calculate(len_a, len_h)
# print(f"二面角正切值: {tan_value:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_10_17",
    "type": 2,
    "level": 2,
    "cn_problem": f"已知四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}的底面是边长为{len_a}的正方形，{point_P}{point_D} ⊥ 底面{point_A}{point_B}{point_C}{point_D}，且{point_P}{point_D} = {len_h}，{point_M}、{point_N}分别为{point_P}{point_B}、{point_A}{point_B}的中点，求二面角{point_M}-{point_D}{point_N}-{point_C}的正切值。",
    "en_problem": f"Given pyramid {point_P}-{point_A}{point_B}{point_C}{point_D} where the base is a square with side length {len_a}, {point_P}{point_D} ⊥ base {point_A}{point_B}{point_C}{point_D}, and {point_P}{point_D} = {len_h}. {point_M} and {point_N} are midpoints of {point_P}{point_B} and {point_A}{point_B} respectively. Find the tangent value of dihedral angle {point_M}-{point_D}{point_N}-{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_10_17({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
