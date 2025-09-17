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
point_A, point_B, point_C, point_D, point_E, point_G, point_F = random.sample(string.ascii_uppercase, 7)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_42_1",
    "type": 1,
    "level": 2,
    "cn_problem": f"如图，在几何体 {point_A}{point_B}{point_C}{point_D}{point_E} 中，四边形 {point_A}{point_B}{point_C}{point_D} 是矩形，{point_A}{point_B}⊥平面 {point_B}{point_E}{point_C}，{point_B}{point_E}⊥{point_E}{point_C}，{point_A}{point_B}={point_B}{point_E}={point_E}{point_C}，{point_G}，{point_F} 分别是线段 {point_B}{point_E}，{point_D}{point_C} 的中点。求图上与 {point_G}{point_F} 平行的唯一平面是哪个？",
    "en_problem": f"As shown in the figure, in the geometry {point_A}{point_B}{point_C}{point_D}{point_E}, the quadrilateral {point_A}{point_B}{point_C}{point_D} is a rectangle, {point_A}{point_B} is perpendicular to the plane {point_B}{point_E}{point_C}, {point_B}{point_E}⊥{point_E}{point_C}, {point_A}{point_B}={point_B}{point_E}={point_E}{point_C}, and {point_G}, {point_F} are the midpoints of the line segments {point_B}{point_E}, {point_D}{point_C} respectively. Which is the unique plane in the figure that is parallel to {point_G}{point_F}?",
    "solution": f"{point_A}{point_D}{point_E}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_42_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_G}', '{point_F}')"}, ensure_ascii=False) + "\n")
