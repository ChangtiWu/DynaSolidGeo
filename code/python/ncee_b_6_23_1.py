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
point_P, point_A, point_B, point_C, point_D, point_E = random.sample(string.ascii_uppercase, 6)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_23_1",
    "type": 1,
    "level": 2,
    "cn_problem": f"如图，已知四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D}，△{point_P}{point_A}{point_D} 是以 {point_A}{point_D} 为斜边的等腰直角三角形，{point_B}{point_C}∥{point_A}{point_D}，{point_C}{point_D}⊥{point_A}{point_D}，{point_P}{point_C}={point_A}{point_D}=2*{point_D}{point_C}=2*{point_C}{point_B}，{point_E} 为 {point_P}{point_D} 的中点。求由图上顶点连成的与平面 {point_P}{point_A}{point_B} 平行的唯一的直线是哪条？",
    "en_problem": f"As shown in the figure, given the quadrangular pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, △{point_P}{point_A}{point_D} is an isosceles right triangle with {point_A}{point_D} as the hypotenuse, {point_B}{point_C}∥{point_A}{point_D}, {point_C}{point_D}⊥{point_A}{point_D}, {point_P}{point_C}={point_A}{point_D}=2*{point_D}{point_C}=2*{point_C}{point_B}, and {point_E} is the midpoint of {point_P}{point_D}. Which is the unique straight line connected by the vertices in the figure that is parallel to the plane {point_P}{point_A}{point_B}?",
    "solution": f"{point_C}{point_E}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_23_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
