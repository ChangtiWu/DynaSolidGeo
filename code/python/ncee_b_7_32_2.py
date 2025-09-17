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


def calculate(len_b, len_c):
    """计算余弦值（公式：len_b / (2*√(len_b² + 3len_c²))）"""
    denominator = 2 * math.sqrt(len_b ** 2 + 3 * len_c ** 2)
    return len_b / denominator


# 测试示例
len_b = 3.0
len_c = 1.0
arg_alpha = math.pi / 2

# print(calculate(len_b, len_c))

# Generate random lengths
len_c = round(len_scaling_factor * float(len_c), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_32_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"三棱台{point_A}{point_B}{point_C}-{point_D}{point_E}{point_F}中，平面{point_B}{point_C}{point_F}{point_E}⊥平面{point_A}{point_B}{point_C}，∠{point_A}{point_C}{point_B}={arg_alpha}，{point_B}{point_C}=2*{len_c}，{point_A}{point_C}={len_b}，{point_B}{point_E}={point_E}{point_F}={point_F}{point_C}={len_c}。求二面角{point_B}-{point_A}{point_D}-{point_F}的平面角的余弦值。",
    "en_problem": f"In triangular frustum {point_A}{point_B}{point_C}-{point_D}{point_E}{point_F}, plane {point_B}{point_C}{point_F}{point_E}⊥plane {point_A}{point_B}{point_C}, ∠{point_A}{point_C}{point_B}={arg_alpha}, {point_B}{point_C}=2*{len_c}, {point_A}{point_C}={len_b}, {point_B}{point_E}={point_E}{point_F}={point_F}{point_C}={len_c}. Find the cosine of the plane angle of dihedral angle {point_B}-{point_A}{point_D}-{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_32_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
