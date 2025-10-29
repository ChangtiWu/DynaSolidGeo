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
point_A, point_B, point_C, point_D, point_O, point_E, point_F, point_G = random.sample(string.ascii_uppercase, 8)

# Generate random lengths
len_a = 2.0
len_a = round(len_scaling_factor * float(len_a), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_26_1",
    "type": 1,
    "level": 2,
    "cn_problem": f"如图，正方形 {point_A}{point_B}{point_C}{point_D} 的中心为 {point_O}，四边形 {point_O}{point_B}{point_E}{point_F} 为矩形，平面 {point_O}{point_B}{point_E}{point_F}⊥平面 {point_A}{point_B}{point_C}{point_D}，点 {point_G} 为 {point_A}{point_B} 的中点，{point_A}{point_B}={point_B}{point_E}={len_a}。求图上与 {point_E}{point_G} 平行的唯一的平面是哪个？",
    "en_problem": f"As shown in the figure, the center of square {point_A}{point_B}{point_C}{point_D} is {point_O}, quadrilateral {point_O}{point_B}{point_E}{point_F} is a rectangle, plane {point_O}{point_B}{point_E}{point_F} is perpendicular to plane {point_A}{point_B}{point_C}{point_D}, point {point_G} is the midpoint of {point_A}{point_B}, and {point_A}{point_B}={point_B}{point_E}={len_a}. Which is the unique plane in the figure that is parallel to {point_E}{point_G}?",
    "solution": f"{point_A}{point_D}{point_F}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_26_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}', '{point_E}', '{point_F}', '{point_G}')"}, ensure_ascii=False) + "\n")
