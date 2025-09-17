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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_F = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math


def calculate():
    """计算满足sin(theta) = √42/7的角度theta（弧度制）"""
    return (math.sqrt(42) / 7)


# 测试示例
len_a = 2.0
len_b = 1.0
len_c = 3.0

# print(calculate())

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_18_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在长方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}中，{point_A}{point_B}={len_a}，{point_A}{point_D}={len_b}，{point_A}{point_A1}={len_c}，点{point_E}在棱{point_D}{point_D1}上满足2*{point_D}{point_E}={point_E}{point_D1}，点{point_F}在棱{point_B}{point_B1}上满足{point_B}{point_F}=2*{point_F}{point_B1}。求二面角{point_A}-{point_E}{point_F}-{point_A1}的正弦值。",
    "en_problem": f"In rectangular prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, {point_A}{point_B}={len_a}, {point_A}{point_D}={len_b}, {point_A}{point_A1}={len_c}, point {point_E} is on edge {point_D}{point_D1} satisfying 2*{point_D}{point_E}={point_E}{point_D1}, and point {point_F} is on edge {point_B}{point_B1} satisfying {point_B}{point_F}=2*{point_F}{point_B1}. Find the sine of dihedral angle {point_A}-{point_E}{point_F}-{point_A1}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_18_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
