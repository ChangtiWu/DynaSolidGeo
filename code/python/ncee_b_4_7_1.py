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
point_P, point_A, point_B, point_C, point_D, point_M = random.sample(string.ascii_uppercase, 6)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_7_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}的底面是矩形，{point_P}{point_D}⊥底面{point_A}{point_B}{point_C}{point_D}，{point_M}为{point_B}{point_C}的中点，且{point_P}{point_B}⊥{point_A}{point_M}。在图上的所有平面中，唯一与平面{point_P}{point_A}{point_M}垂直的平面是哪个？",
    "en_problem": f"The bottom surface of the quadrangular pyramid {point_P}-{point_A}{point_B}{point_C}{point_D} is a rectangle, {point_P}{point_D}⊥ the bottom surface {point_A}{point_B}{point_C}{point_D}, {point_M} is the midpoint of {point_B}{point_C}, and {point_P}{point_B}⊥{point_A}{point_M}. Among all the planes in the figure, which plane is uniquely perpendicular to the plane {point_P}{point_A}{point_M}?",
    "solution": f"{point_P}{point_B}{point_D}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_7_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}')"}, ensure_ascii=False) + "\n")
