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


def calculate(len_a, len_b, len_c, len_d):
    """计算体积V的值（两种等价表达式：(√3/8)len_d²(len_a+len_c) 或 (√3/4)len_b len_d²）"""
    # 任选一个等价表达式实现（此处选择第二个表达式）
    return (math.sqrt(3) / 4) * len_b * (len_d ** 2)


# 测试示例
len_a = 1.0
len_c = 3.0
len_b = 2.0
len_d = 1.0

# print(calculate(len_a, len_b, len_c, len_d))

# Generate random lengths
len_d = round(len_scaling_factor * float(len_d), 2)
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c, len_d)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_s1_2_2_1",
    "type": 5,
    "level": 1,
    "cn_problem": f"五面体{point_A}{point_B}{point_C}-{point_D}{point_E}{point_F}中，{point_A}{point_D}//{point_B}{point_E}//{point_C}{point_F}，且两两之间距离均为{len_d}。已知{point_A}{point_D}={len_a}，{point_B}{point_E}={len_b}，{point_C}{point_F}={len_c}，其中{len_a}+{len_c}=2*{len_b}。求该五面体的体积。",
    "en_problem": f"In pentahedron {point_A}{point_B}{point_C}-{point_D}{point_E}{point_F}, {point_A}{point_D}//{point_B}{point_E}//{point_C}{point_F}, and the distances between any two of these parallel lines are all {len_d}. Given {point_A}{point_D}={len_a}, {point_B}{point_E}={len_b}, {point_C}{point_F}={len_c}, where {len_a}+{len_c}=2*{len_b}. Find the volume of this pentahedron.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_s1_2_2_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
