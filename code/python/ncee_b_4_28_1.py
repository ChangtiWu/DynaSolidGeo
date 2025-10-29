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
point_O, point_C, point_A, point_B, point_P, point_D = random.sample(string.ascii_uppercase, 6)

# Generate random lengths
len_a = 1.0
len_a = round(len_scaling_factor * float(len_a), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_28_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"已知AB是圆{point_O}的直径，点{point_C}是圆{point_O}上异于{point_A}，{point_B}的点，{point_P}{point_O}垂直于圆{point_O}所在的平面，且{point_P}{point_O} = {point_O}{point_B} = {len_a}（{len_a} > 0）。若{point_D}为线段{point_A}{point_C}的中点，求由图上给出的点组成的唯一与平面{point_P}{point_D}{point_O}垂直的线段。",
    "en_problem": f"Given that AB is the diameter of circle {point_O}, point {point_C} is a point on circle {point_O} different from {point_A} and {point_B}, {point_P}{point_O} is perpendicular to the plane where circle {point_O} lies, and {point_P}{point_O} = {point_O}{point_B} = {len_a} ({len_a} > 0). If {point_D} is the midpoint of line segment {point_A}{point_C}, find the unique line segment composed of the points given in the figure that is perpendicular to plane {point_P}{point_D}{point_O}.",
    "solution": f"{point_A}{point_C}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_28_1({mode}, {azimuth}, {elevation}, '{point_O}', '{point_C}', '{point_A}', '{point_B}', '{point_P}', '{point_D}')"}, ensure_ascii=False) + "\n")
