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
point_A, point_B, point_C, point_D, point_E, point_F, point_P = random.sample(string.ascii_uppercase, 7)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_19_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"如图，四边形 {point_A}{point_B}{point_C}{point_D} 为正方形，{point_E}，{point_F} 分别为 {point_A}{point_D}，{point_B}{point_C} 的中点，以 {point_D}{point_F} 为折痕把△{point_D}{point_F}{point_C} 折起，使点 {point_C} 到达点 {point_P} 的位置，且 {point_P}{point_F}⊥{point_B}{point_F}。求由图上至少三个顶点构成的与平面 {point_A}{point_B}{point_F}{point_D} 垂直的唯一的平面是哪个？",
    "en_problem": f"As shown in the figure, quadrilateral {point_A}{point_B}{point_C}{point_D} is a square, {point_E} and {point_F} are the midpoints of {point_A}{point_D} and {point_B}{point_C} respectively. Fold △{point_D}{point_F}{point_C} along the crease {point_D}{point_F} so that point {point_C} reaches the position of point {point_P}, and {point_P}{point_F}⊥{point_B}{point_F}. Which is the unique plane composed of at least three vertices in the figure that is perpendicular to plane {point_A}{point_B}{point_F}{point_D}?",
    "solution": f"{point_P}{point_E}{point_F}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_19_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_P}')"}, ensure_ascii=False) + "\n")
