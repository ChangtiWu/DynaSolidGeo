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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D, point_E, point_F, point_G = random.sample(string.ascii_uppercase, 10)

# Generate random lengths
len_a = math.sqrt(5)
len_b = 2
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_24_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"如图，在三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，{point_C}{point_C1}⊥平面 {point_A}{point_B}{point_C}，{point_D}，{point_E}，{point_F}，{point_G} 分别为 {point_A}{point_A1}，{point_A}{point_C}，{point_A1}{point_C1}，{point_B}{point_B1} 的中点，{point_A}{point_B}={point_B}{point_C}={len_a}，{point_A}{point_C}={point_A}{point_A1}={len_b}。求图上与直线 {point_A}{point_C} 垂直的唯一平面是哪个？",
    "en_problem": f"As shown in the figure, in the triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, {point_C}{point_C1} is perpendicular to the plane {point_A}{point_B}{point_C}, {point_D}, {point_E}, {point_F}, {point_G} are the midpoints of {point_A}{point_A1}, {point_A}{point_C}, {point_A1}{point_C1}, {point_B}{point_B1} respectively, {point_A}{point_B}={point_B}{point_C}={len_a}, {point_A}{point_C}={point_A}{point_A1}={len_b}. Which is the unique plane in the figure that is perpendicular to the line {point_A}{point_C}?",
    "solution": f"{point_B}{point_E}{point_F}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_24_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}', '{point_E}', '{point_F}', '{point_G}')"}, ensure_ascii=False) + "\n")
