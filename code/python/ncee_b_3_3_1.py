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
point_A, point_B, point_C, point_A1, point_B1, point_C1 = random.sample(string.ascii_uppercase, 6)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_3_3_1",
    "type": 1,
    "level": 2,
    "cn_problem": f"在三棱柱{point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}中，{point_A1}{point_C}⊥平面{point_A}{point_B}{point_C}，∠{point_A}{point_C}{point_B}=90°。与平面{point_B}{point_B1}{point_C1}{point_C}垂直的唯一个由四个顶点组成的平面是哪个？",
    "en_problem": f"In the triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, {point_A1}{point_C}⊥ plane {point_A}{point_B}{point_C}, and ∠{point_A}{point_C}{point_B}=90°. Which unique plane composed of four vertices is perpendicular to the plane {point_B}{point_B1}{point_C1}{point_C}?",
    "solution": f"{point_A}{point_C}{point_C1}{point_A1}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_3_3_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}')"}, ensure_ascii=False) + "\n")
