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
point_A, point_B, point_C, point_D, point_O, point_E, point_F = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_c: float, len_d: float, len_h: float) -> float:
    """计算 sinθ 的表达式值"""
    # 分子部分计算
    numerator_part1 = 12 * len_d * len_h
    numerator_sqrt = math.sqrt(
        (4 * len_c**2 - len_d**2) *
        (4 * len_c**2 + 3 * len_d**2 + 4 * len_h**2)
    )
    numerator = numerator_part1 * numerator_sqrt

    # 分母部分计算
    denominator_part1 = 4 * len_c**2 * len_d**2 + 16 * len_c**2 * len_h**2 - len_d**4
    denominator_part2 = 100 * len_c**2 * len_d**2 + 16 * len_c**2 * len_h**2 - 25 * len_d**4 + 192 * len_d**2 * len_h**2
    denominator_sqrt = math.sqrt(denominator_part1 * denominator_part2)

    # 计算并返回 sinθ
    return numerator / denominator_sqrt

len_c = math.sqrt(5)
len_d = 2.0
len_h = 2.0


# result = calculate(len_c, len_d, len_h)
# print(f"sinθ = {result:.6f}")
# Generate random lengths
len_c = round(len_scaling_factor * float(len_c), 2)
len_d = round(len_scaling_factor * float(len_d), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_c, len_d, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_17_2",
    "type": 2,
    "level": 3,
    "cn_problem": f"在三棱锥 {point_A}-{point_B}{point_C}{point_D} 中，底面 $\\triangle {point_B}{point_C}{point_D}$ 为等腰三角形，满足 {point_C}{point_B}={point_C}{point_D}={len_c}>0，{point_B}{point_D}={len_d}>0，且 {len_d}<2*{len_c}。记 {point_O} 为棱 {point_B}{point_D} 的中点，且设 {point_A}{point_O}={len_h}>0，{point_A}{point_O}⊥平面 {point_B}{point_C}{point_D}。设 {point_E} 为棱 {point_A}{point_C} 的中点，点 {point_F} 在 {point_B}{point_C} 上且 {point_B}{point_F}=\\frac{{1}}{{4}}{point_B}{point_C}。若二面角 {point_F}-{point_D}{point_E}-{point_C} 的平面角为 θ，求 sin θ 。",
    "en_problem": f"In triangular pyramid {point_A}-{point_B}{point_C}{point_D}, the base $\\triangle {point_B}{point_C}{point_D}$ is an isosceles triangle with {point_C}{point_B}={point_C}{point_D}={len_c}>0, {point_B}{point_D}={len_d}>0, and {len_d}<2*{len_c}. Let {point_O} be the midpoint of edge {point_B}{point_D}, with {point_A}{point_O}={len_h}>0 and {point_A}{point_O}⊥plane {point_B}{point_C}{point_D}. Let {point_E} be the midpoint of edge {point_A}{point_C}, and point {point_F} on {point_B}{point_C} such that {point_B}{point_F}=\\frac{{1}}{{4}}{point_B}{point_C}. If the planar angle of dihedral angle {point_F}-{point_D}{point_E}-{point_C} is θ, find sin θ .",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_17_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
