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
point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 6)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_5_5_1",
    "type": 1,
    "level": 3,
    "cn_problem": f"如图，四边形{point_A}{point_B}{point_C}{point_D}为菱形，∠{point_A}{point_B}{point_C}=120°，{point_E}，{point_F}是平面{point_A}{point_B}{point_C}{point_D}同一侧的两点，{point_B}{point_E}⊥平面{point_A}{point_B}{point_C}{point_D}，{point_D}{point_F}⊥平面{point_A}{point_B}{point_C}{point_D}，{point_B}{point_E}=2*{point_D}{point_F}，{point_A}{point_E}⊥{point_E}{point_C}。求由图上至少三个顶点构成的与平面{point_A}{point_E}{point_C}垂直的唯一的平面是哪个",
    "en_problem": f"As shown in the figure, quadrilateral {point_A}{point_B}{point_C}{point_D} is a rhombus, ∠{point_A}{point_B}{point_C}=120°, {point_E} and {point_F} are two points on the same side of plane {point_A}{point_B}{point_C}{point_D}, {point_B}{point_E} ⊥ plane {point_A}{point_B}{point_C}{point_D}, {point_D}{point_F} ⊥ plane {point_A}{point_B}{point_C}{point_D}, {point_B}{point_E}=2*{point_D}{point_F}, and {point_A}{point_E} ⊥ {point_E}{point_C}. Which unique plane formed by at least three vertices in the figure is perpendicular to plane {point_A}{point_E}{point_C}?",
    "solution": f"{point_A}{point_F}{point_C}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_5_5_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
