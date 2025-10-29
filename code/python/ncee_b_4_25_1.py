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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_E, point_F = random.sample(string.ascii_uppercase, 8)

# Generate random lengths
len_a = 2.0
len_a = round(len_scaling_factor * float(len_a), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_25_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 的底面是边长为 {len_a} 的正三角形，{point_E}，{point_F} 分别是 {point_B}{point_C}，{point_C}{point_C1} 的中点。求由图上给出的点组成的唯一与平面 {point_A}{point_E}{point_F} 垂直的平面。",
    "en_problem": f"The bottom surface of the right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} is an equilateral triangle with side length {len_a}, and {point_E}, {point_F} are the midpoints of {point_B}{point_C}, {point_C}{point_C1} respectively. Find the unique plane composed of the points given in the figure that is perpendicular to plane {point_A}{point_E}{point_F}.",
    "solution": f"{point_B}{point_B1}{point_C}{point_C1}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_25_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
