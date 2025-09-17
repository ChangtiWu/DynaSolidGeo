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
point_A, point_C, point_O, point_E, point_F, point_O_prime, point_B = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate():
    """计算满足cos(theta) = √7/7的角度theta（弧度制）"""
    return math.sqrt(7) / 7


# 测试示例
len_r = 2 * math.sqrt(3)

# print(calculate())

# Generate random lengths
len_r = round(len_scaling_factor * float(len_r), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_31_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在圆台中，{point_A}{point_C}是下底面圆{point_O}的直径，{point_E}{point_F}是上底面圆{point_O_prime}的直径，{point_F}{point_B}是圆台的一条母线。已知{point_E}{point_F}={point_F}{point_B}={len_r}/2，{point_A}{point_B}={point_B}{point_C}，求二面角{point_F}-{point_B}{point_C}-{point_A}的余弦值。",
    "en_problem": f"In the truncated cone, {point_A}{point_C} is the diameter of the lower base circle {point_O}, {point_E}{point_F} is the diameter of the upper base circle {point_O_prime}, and {point_F}{point_B} is a generatrix of the truncated cone. Given that {point_E}{point_F}={point_F}{point_B}={len_r}/2 and {point_A}{point_B}={point_B}{point_C}, find the cosine of dihedral angle {point_F}-{point_B}{point_C}-{point_A}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_31_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_C}', '{point_O}', '{point_E}', '{point_F}', '{point_O_prime}', '{point_B}')"}, ensure_ascii=False) + "\n")
