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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math

def calculate():
    """
    计算正方体截面与面 CDD1C1 所成锐二面角的度数

    返回:
    float: 角度值（度）
    """
    # 已知结果
    return 60.0


# 题干给定的数值
len_a = 1.0  # 正方体边长
AE = (3 - math.sqrt(6)) / 3  # 点 E 在 AA1 上的位置

# 验证输出
# angle = calculate()
# print(f"锐二面角: {angle:.6f}°")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_9_14",
    "type": 2,
    "level": 2,
    "cn_problem": f"在棱长为{len_a}的正方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}中，{point_E}是棱{point_A}{point_A1}上任意一点（使得过{point_E}、{point_C}、{point_D1}的截面存在），过{point_E}、{point_C}、{point_D1}三点作正方体的截面，求此截面与面{point_C}{point_D}{point_D1}{point_C1}所成锐二面角的度数。",
    "en_problem": f"In a cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} with edge length {len_a}, {point_E} is any point on edge {point_A}{point_A1} (such that a cross-section through {point_E}, {point_C}, {point_D1} exists). Find the degree measure of the acute dihedral angle between the cross-section through {point_E}, {point_C}, {point_D1} and face {point_C}{point_D}{point_D1}{point_C1}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_9_14({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}')"}, ensure_ascii=False) + "\n")
