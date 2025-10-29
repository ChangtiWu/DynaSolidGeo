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

# Generate random lengths
len_a = 1.0
len_a = round(len_scaling_factor * float(len_a), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_18_1",
    "type": 1,
    "level": 3,
    "cn_problem": f"已知多面体{point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}，{point_A1}{point_A},{point_B1}{point_B},{point_C1}{point_C}均垂直于平面{point_A}{point_B}{point_C}，∠{point_A}{point_B}{point_C}=120°，{point_A1}{point_A}=4*{len_a}，{point_C1}{point_C}=1*{len_a}，{point_A}{point_B}={point_B}{point_C}={point_B1}{point_B}=2*{len_a}（{len_a}>0）。求由图上顶点连成的与平面{point_A1}{point_B1}{point_C1}垂直的唯一的直线是哪条？",
    "en_problem": f"Given the polyhedron {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, {point_A1}{point_A}, {point_B1}{point_B}, {point_C1}{point_C} are all perpendicular to the plane {point_A}{point_B}{point_C}, ∠{point_A}{point_B}{point_C}=120°, {point_A1}{point_A}=4*{len_a}, {point_C1}{point_C}=1*{len_a}, {point_A}{point_B}={point_B}{point_C}={point_B1}{point_B}=2*{len_a} ({len_a}>0). Which unique line connected by the vertices in the figure is perpendicular to the plane {point_A1}{point_B1}{point_C1}?",
    "solution": f"{point_A}{point_B1}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_18_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}')"}, ensure_ascii=False) + "\n")
