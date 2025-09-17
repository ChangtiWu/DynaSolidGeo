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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D, point_E, point_F, point_G = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math


def calculate(len_a: float, len_p: float, len_q: float) -> float:
    """计算 cosθ 的表达式值"""
    numerator = len_p * len_q
    denominator_part = 4 * len_a ** 2 * len_p ** 2 + len_a ** 2 * len_q ** 2 - len_p ** 4
    denominator = 2 * math.sqrt(denominator_part)
    return numerator / denominator


len_a = math.sqrt(5)
len_p = 2.0
len_q = 2.0

# result = calculate(len_a, len_p, len_q)
# print(f"cosθ = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_p = round(len_scaling_factor * float(len_p), 2)
len_q = round(len_scaling_factor * float(len_q), 2)

# Calculate the result
result = calculate(len_a, len_p, len_q)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_24_2",
    "type": 2,
    "level": 3,
    "cn_problem": f"在三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，{point_C}{point_C1}⊥平面 {point_A}{point_B}{point_C}，{point_D},{point_E},{point_F},{point_G} 分别为 {point_A}{point_A1}, {point_A}{point_C}, {point_A1}{point_C1}, {point_B}{point_B1} 的中点。设 {point_A}{point_B}={point_B}{point_C}={len_a}>0，{point_A}{point_C}={len_p}>0，{point_A}{point_A1}={len_q}>0，且 {len_p}<2*{len_a}。求二面角 {point_B}-{point_C}{point_D}-{point_C1} 的余弦值 cos θ。",
    "en_problem": f"In triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, {point_C}{point_C1}⊥plane {point_A}{point_B}{point_C}, and {point_D},{point_E},{point_F},{point_G} are midpoints of {point_A}{point_A1}, {point_A}{point_C}, {point_A1}{point_C1}, {point_B}{point_B1} respectively. Let {point_A}{point_B}={point_B}{point_C}={len_a}>0, {point_A}{point_C}={len_p}>0, {point_A}{point_A1}={len_q}>0, where {len_p}<2*{len_a}. Find the cosine value of dihedral angle {point_B}-{point_C}{point_D}-{point_C1}, expressing the result.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_24_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}', '{point_E}', '{point_F}', '{point_G}')"}, ensure_ascii=False) + "\n")
