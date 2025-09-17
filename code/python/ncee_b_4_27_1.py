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
    "id": "ncee_b_4_27_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"在阳马 {point_P}-{point_A}{point_B}{point_C}{point_D} 中，侧棱 {point_P}{point_D} ⊥ 底面 {point_A}{point_B}{point_C}{point_D}，且 {point_P}{point_D} = {point_C}{point_D}，点 {point_E} 是 {point_P}{point_C} 的中点，连接 {point_D}{point_E}，{point_B}{point_D}，{point_B}{point_E}。求由图上给出的点组成的唯一与平面 {point_P}{point_B}{point_C} 垂直的线段。",
    "en_problem": f"In the yangma {point_P}-{point_A}{point_B}{point_C}{point_D}, the lateral edge {point_P}{point_D} is perpendicular to the base {point_A}{point_B}{point_C}{point_D}, and {point_P}{point_D} = {point_C}{point_D}, point {point_E} is the midpoint of {point_P}{point_C}, connecting {point_D}{point_E}, {point_B}{point_D}, {point_B}{point_E}. Find the unique line segment composed of the points given in the figure that is perpendicular to plane {point_P}{point_B}{point_C}.",
    "solution": f"{point_D}{point_E}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_27_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
