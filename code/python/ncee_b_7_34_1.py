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
    "id": "ncee_b_7_34_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"如图，在以 {point_A}，{point_B}，{point_C}，{point_D}，{point_E}，{point_F} 为顶点的五面体中，四边形 {point_A}{point_B}{point_E}{point_F} 为正方形，{point_A}{point_F} = 2*{point_F}{point_D}，∠{point_A}{point_F}{point_D} = 90°，且二面角 {point_D}-{point_A}{point_F}-{point_E} 与二面角 {point_C}-{point_B}{point_E}-{point_F} 都是60°。求图上与平面 {point_A}{point_B}{point_E}{point_F} 垂直的唯一平面是哪个？",
    "en_problem": f"As shown in the figure, in the pentahedron with vertices {point_A}, {point_B}, {point_C}, {point_D}, {point_E}, {point_F}, the quadrilateral {point_A}{point_B}{point_E}{point_F} is a square, {point_A}{point_F} = 2*{point_F}{point_D}, ∠{point_A}{point_F}{point_D} = 90°, and both the dihedral angle {point_D}-{point_A}{point_F}-{point_E} and the dihedral angle {point_C}-{point_B}{point_E}-{point_F} are 60°. Which is the unique plane in the figure that is perpendicular to the plane {point_A}{point_B}{point_E}{point_F}?",
    "solution": f"{point_E}{point_F}{point_D}{point_C}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_34_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
