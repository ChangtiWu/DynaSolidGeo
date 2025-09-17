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


def calculate(len_a, len_h):
    """计算sin(theta)的值（公式：√3*len_a / √(4len_h² + 3len_a²)）"""
    numerator = math.sqrt(3) * len_a
    denominator = math.sqrt(4 * (len_h ** 2) + 3 * (len_a ** 2))
    return numerator / denominator


# 测试示例
len_a = 1.0
len_b = 2.0
len_h = math.sqrt(3)

# print(calculate(len_a, len_h))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_4_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}中，{point_P}{point_D}⊥底面{point_A}{point_B}{point_C}{point_D},{point_C}{point_D}//{point_A}{point_B},{point_A}{point_D}={point_D}{point_C}={point_C}{point_B}={len_a},{point_A}{point_B}={len_b},{point_D}{point_P}={len_h}。求{point_P}{point_D}与平面{point_P}{point_A}{point_B}所成角的正弦值。",
    "en_problem": f"In pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, {point_P}{point_D}⊥base {point_A}{point_B}{point_C}{point_D}, {point_C}{point_D}//{point_A}{point_B}, {point_A}{point_D}={point_D}{point_C}={point_C}{point_B}={len_a}, {point_A}{point_B}={len_b}, {point_D}{point_P}={len_h}. Find the sine of the angle between line {point_P}{point_D} and plane {point_P}{point_A}{point_B}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_4_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
