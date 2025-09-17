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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D = random.sample(string.ascii_uppercase, 7)

# Generate random lengths
len_a = 2
len_b = 4
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_31_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"如图，在三棱锥 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，∠{point_B}{point_A}{point_C}=90°，{point_A}{point_B}={point_A}{point_C}={len_a}，{point_A}{point_A1}={len_b}，{point_A1} 在底面 {point_A}{point_B}{point_C} 的射影为 {point_B}{point_C} 的中点，{point_D} 为 {point_B1}{point_C1} 的中点。求图上与 {point_A1}{point_D} 垂直的唯一的平面是哪个？",
    "en_problem": f"As shown in the figure, in the triangular pyramid {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, ∠{point_B}{point_A}{point_C}=90°, {point_A}{point_B}={point_A}{point_C}={len_a}, {point_A}{point_A1}={len_b}, the projection of {point_A1} on the base {point_A}{point_B}{point_C} is the midpoint of {point_B}{point_C}, and {point_D} is the midpoint of {point_B1}{point_C1}. Which is the unique plane in the figure that is perpendicular to {point_A1}{point_D}?",
    "solution": f"{point_A1}{point_B}{point_C}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_31_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}')"}, ensure_ascii=False) + "\n")
