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
point_P, point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 7)

# Generate random lengths
len_a = 2
len_b = 3
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_20_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"如图，在四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 中，{point_P}{point_A}⊥平面 {point_A}{point_B}{point_C}{point_D}，{point_A}{point_D}⊥{point_C}{point_D}，{point_A}{point_D}∥{point_B}{point_C}，{point_P}{point_A}={point_A}{point_D}={point_C}{point_D}={len_a}，{point_B}{point_C}={len_b}。{point_E} 为 {point_P}{point_D} 的中点，点 {point_F} 在 {point_P}{point_C} 上，且 \\(\\frac{{{point_P}{point_F}}}{{{point_P}{point_C}}}=\\frac{{1}}{{3}}\\)。求图上与平面 {point_P}{point_A}{point_D} 垂直的唯一直线是哪条？",
    "en_problem": f"As shown in the figure, in the quadrangular pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, {point_P}{point_A} is perpendicular to the plane {point_A}{point_B}{point_C}{point_D}, {point_A}{point_D}⊥{point_C}{point_D}, {point_A}{point_D}∥{point_B}{point_C}, {point_P}{point_A}={point_A}{point_D}={point_C}{point_D}={len_a}, {point_B}{point_C}={len_b}. {point_E} is the midpoint of {point_P}{point_D}, and point {point_F} is on {point_P}{point_C} with \\(\\frac{{{point_P}{point_F}}}{{{point_P}{point_C}}}=\\frac{{1}}{{3}}\\). Which is the unique straight line in the figure that is perpendicular to the plane {point_P}{point_A}{point_D}?",
    "solution": f"{point_C}{point_D}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_20_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
