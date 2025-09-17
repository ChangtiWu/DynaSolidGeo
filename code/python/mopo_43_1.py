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
point_A, point_B, point_C, point_A1, point_B1, point_C1 = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_a, len_b, len_c, len_h, arg_theta):
    """计算cos(arg_alpha)的值（表达式为|len_a·len_b·cos(arg_theta) - len_h²| / √[(len_a²+len_h²)(len_b²+len_h²)]）"""
    numerator = abs(len_a * len_b * math.cos(arg_theta) - len_h ** 2)
    denominator = math.sqrt((len_a ** 2 + len_h ** 2) * (len_b ** 2 + len_h ** 2))
    return numerator / denominator


# 测试示例
len_a = math.sqrt(2)
len_b = 2.0
len_c = math.sqrt(10)
len_h = math.sqrt(2)
arg_theta = math.radians(135)

# print(calculate(len_a, len_b, len_c, len_h, arg_theta))

# Generate random lengths
len_c = round(len_scaling_factor * float(len_c), 2)
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c, len_h, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_43_1",
    "type": 2,
    "level": 2,
    "cn_problem": f"在直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，设 $\\\\angle {point_A}{point_C}{point_B} = {arg_theta}$，${point_A}{point_B} = {len_c}$，${point_B}{point_C} = {len_a}$，侧棱 ${point_C}{point_C1} = {len_h}$（直三棱柱中 ${point_C}{point_C1} \\\\perp$ 底面 {point_A}{point_B}{point_C}）。求异面直线 ${point_B}{point_C1}$ 与 ${point_A1}{point_C}$ 所成角的余弦值。",
    "en_problem": f"In right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, let $\\\\angle {point_A}{point_C}{point_B} = {arg_theta}$, ${point_A}{point_B} = {len_c}$, ${point_B}{point_C} = {len_a}$, and lateral edge ${point_C}{point_C1} = {len_h}$ (in right triangular prism, ${point_C}{point_C1} \\\\perp$ base {point_A}{point_B}{point_C}). Find the cosine value of the angle between skew lines ${point_B}{point_C1}$ and ${point_A1}{point_C}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_43_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}')"}, ensure_ascii=False) + "\n")
