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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_F, point_G, point_H, point_M = random.sample(string.ascii_uppercase, 13)

# Add result calculation code
def calculate(len_a):
    """计算金字塔体积（公式：len_a³/12）"""
    return (len_a ** 3) / 12


# 测试示例
len_a = 1.0

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_s1_2_25_1",
    "type": 5,
    "level": 1,
    "cn_problem": f"已知正方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}的棱长为{len_a}，除面{point_A}{point_B}{point_C}{point_D}外，该正方体其余各面（前面、后面、左面、右面、上面）的中心分别为点{point_E}，{point_F}，{point_G}，{point_H}，{point_M}，求四棱锥{point_M}-{point_E}{point_F}{point_G}{point_H}的体积。",
    "en_problem": f"A cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} has edge length {len_a}. Except for face {point_A}{point_B}{point_C}{point_D}, the centers of the remaining faces (front, back, left, right, top) are points {point_E}, {point_F}, {point_G}, {point_H}, {point_M} respectively. Find the volume of the quadrilateral pyramid {point_M}-{point_E}{point_F}{point_G}{point_H}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_s1_2_25_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_F}', '{point_G}', '{point_H}', '{point_M}')"}, ensure_ascii=False) + "\n")
