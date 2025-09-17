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
point_A, point_A1, point_B, point_C, point_B1, point_E, point_F = random.sample(string.ascii_uppercase, 7)

# Generate random lengths
len_a = 3
len_b = 2 * math.sqrt(5)
len_c = math.sqrt(7)
len_d = 2 * math.sqrt(7)

len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)
len_d = round(len_scaling_factor * float(len_d), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_32_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"如图，已知 {point_A}{point_A1}⊥平面 {point_A}{point_B}{point_C}，{point_B}{point_B1}∥{point_A}{point_A1}，{point_A}{point_B}={point_A}{point_C}={len_a}，{point_B}{point_C}={len_b}，{point_A}{point_A1}={len_c}，{point_B}{point_B1}={len_d}。点 {point_E}，{point_F} 分别是 {point_B}{point_C}，{point_A1}{point_B1} 的中点。求图上与平面 {point_A1}{point_B1}{point_B}{point_A} 平行的唯一的直线是哪条？",
    "en_problem": f"As shown in the figure, it is known that {point_A}{point_A1} is perpendicular to plane {point_A}{point_B}{point_C}, {point_B}{point_B1}∥{point_A}{point_A1}, {point_A}{point_B}={point_A}{point_C}={len_a}, {point_B}{point_C}={len_b}, {point_A}{point_A1}={len_c}, {point_B}{point_B1}={len_d}. Points {point_E} and {point_F} are the midpoints of {point_B}{point_C} and {point_A1}{point_B1} respectively. Which is the unique straight line in the figure that is parallel to the plane {point_A1}{point_B1}{point_B}{point_A}?",
    "solution": f"{point_E}{point_F}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_32_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_A1}', '{point_B}', '{point_C}', '{point_B1}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
