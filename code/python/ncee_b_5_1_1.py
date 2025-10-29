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
point_A, point_B, point_C, point_D, point_M = random.sample(string.ascii_uppercase, 5)

# Generate random lengths
len_a = 1.0
len_a = round(len_scaling_factor * float(len_a), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_5_1_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"在四面体{point_A}{point_B}{point_C}{point_D}中，△{point_A}{point_B}{point_C}是等边三角形，平面{point_A}{point_B}{point_C}⊥平面{point_A}{point_B}{point_D}，点{point_M}为棱{point_A}{point_B}的中点，{point_A}{point_B}=2*{len_a}，{point_A}{point_D}=2√3*{len_a}，∠{point_B}{point_A}{point_D}=90°（{len_a}>0）。求由图上顶点构成的与{point_B}{point_C}垂直的唯一的直线是哪条？",
    "en_problem": f"In the tetrahedron {point_A}{point_B}{point_C}{point_D}, △{point_A}{point_B}{point_C} is an equilateral triangle, plane {point_A}{point_B}{point_C}⊥ plane {point_A}{point_B}{point_D}, point {point_M} is the midpoint of edge {point_A}{point_B}, {point_A}{point_B}=2*{len_a}, {point_A}{point_D}=2√3*{len_a}, ∠{point_B}{point_A}{point_D}=90° ({len_a}>0). Which unique line formed by the vertices in the figure is perpendicular to {point_B}{point_C}?",
    "solution": f"{point_A}{point_D}",
    "image": f"images/{os.path.splitext(os.path.basename(__file__))[0]}.png"
}

# video mode
if args.mode == 1:
    json_data["image"] = f"videos/{os.path.splitext(os.path.basename(__file__))[0]}.mp4"



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
    f.write(json.dumps({json_data["id"]: f"ncee_b_5_1_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}')"}, ensure_ascii=False) + "\n")
