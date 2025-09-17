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
point_A1, point_B1, point_D1, point_D, point_C, point_B, point_A, point_E = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate():
    """计算cosθ对应的右边值√6/3"""
    return math.sqrt(6) / 3



len_a = 1.0

# print(calculate())

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_41_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在多面体{point_A1}{point_B1}{point_D1}{point_D}{point_C}{point_B}{point_A}{point_A1}中，四边形{point_A}{point_A1}{point_B1}{point_B}、{point_A}{point_D}{point_D1}{point_A1}、{point_A}{point_B}{point_C}{point_D}均为边长为{len_a}的正方形，{point_E}为{point_B1}{point_D1}的中点。求二面角{point_E}-{point_A1}{point_D}-{point_B1}的余弦值。",
    "en_problem": f"In polyhedron {point_A1}{point_B1}{point_D1}{point_D}{point_C}{point_B}{point_A}{point_A1}, quadrilaterals {point_A}{point_A1}{point_B1}{point_B}, {point_A}{point_D}{point_D1}{point_A1}, {point_A}{point_B}{point_C}{point_D} are all squares with side length {len_a}, {point_E} is the midpoint of {point_B1}{point_D1}. Find the cosine value of dihedral angle {point_E}-{point_A1}{point_D}-{point_B1}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_41_2({mode}, {azimuth}, {elevation}, '{point_A1}', '{point_B1}', '{point_D1}', '{point_D}', '{point_C}', '{point_B}', '{point_A}', '{point_E}')"}, ensure_ascii=False) + "\n")
