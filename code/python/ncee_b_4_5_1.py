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
point_A, point_B, point_C, point_D, point_O = random.sample(string.ascii_uppercase, 5)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_5_1",
    "type": 1,
    "level": 2,
    "cn_problem": f"在三棱锥{point_A}-{point_B}{point_C}{point_D}中，平面{point_A}{point_B}{point_D}⊥平面{point_B}{point_C}{point_D}，{point_A}{point_B}={point_A}{point_D}，{point_O}为{point_B}{point_D}的中点。由点集 {{{point_A},{point_B},{point_C},{point_D},{point_O}}} 所能连成的线段中，唯一与线段{point_C}{point_D}垂直的是哪条？",
    "en_problem": f"In the triangular pyramid {point_A}-{point_B}{point_C}{point_D}, plane {point_A}{point_B}{point_D}⊥ plane {point_B}{point_C}{point_D}, {point_A}{point_B}={point_A}{point_D}, and {point_O} is the midpoint of {point_B}{point_D}. Which line segment formed by the point set {{{point_A},{point_B},{point_C},{point_D},{point_O}}} is uniquely perpendicular to the line segment {point_C}{point_D}?",
    "solution": f"{point_A}{point_O}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_5_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}')"}, ensure_ascii=False) + "\n")
