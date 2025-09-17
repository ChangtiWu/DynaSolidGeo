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
point_A, point_B, point_C, point_D, point_E, point_F, point_M, point_N = random.sample(string.ascii_uppercase, 8)

# Generate random lengths
len_a = 1.0
len_a = round(len_scaling_factor * float(len_a), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_6_1",
    "type": 1,
    "level": 3,
    "cn_problem": f"已知{point_A}{point_B}{point_C}{point_D}和{point_C}{point_D}{point_E}{point_F}都是直角梯形，{point_A}{point_B}∥{point_D}{point_C}，{point_D}{point_C}∥{point_E}{point_F}，{point_A}{point_B}=5*{len_a}，{point_D}{point_C}=3*{len_a}，{point_E}{point_F}={len_a}（{len_a}>0），∠{point_B}{point_A}{point_D}=∠{point_C}{point_D}{point_E}=60°，二面角{point_F}−{point_D}{point_C}−{point_B}的平面角为60°。设{point_M}，{point_N}分别为{point_A}{point_E}，{point_B}{point_C}的中点。求由图上顶点连成的与平面{point_A}{point_B}{point_C}{point_D}垂直的唯一的直线是哪条？",
    "en_problem": f"Given that {point_A}{point_B}{point_C}{point_D} and {point_C}{point_D}{point_E}{point_F} are both right trapezoids, {point_A}{point_B}∥{point_D}{point_C}, {point_D}{point_C}∥{point_E}{point_F}, {point_A}{point_B}=5*{len_a}, {point_D}{point_C}=3*{len_a}, {point_E}{point_F}={len_a} ({len_a}>0), ∠{point_B}{point_A}{point_D}=∠{point_C}{point_D}{point_E}=60°, and the dihedral angle {point_F}−{point_D}{point_C}−{point_B} has a plane angle of 60°. Let {point_M} and {point_N} be the midpoints of {point_A}{point_E} and {point_B}{point_C} respectively. Which unique line formed by the vertices in the figure is perpendicular to plane {point_A}{point_B}{point_C}{point_D}?",
    "solution": f"{point_F}{point_N}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_6_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
