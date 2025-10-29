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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_M, point_N, point_P, point_E, point_F = random.sample(string.ascii_uppercase, 11)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_9_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"已知三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 的底面是正三角形，侧面 {point_B}{point_B1}{point_C1}{point_C} 是矩形，{point_M}，{point_N} 分别为 {point_B}{point_C}，{point_B1}{point_C1} 的中点，{point_P} 为 {point_A}{point_M} 上一点。过 {point_B1}{point_C1} 和 {point_P} 的平面交 {point_A}{point_B} 于 {point_E}，交 {point_A}{point_C} 于 {point_F}。求由图上给出的点组成的与平面 {point_E}{point_B1}{point_C1}{point_F} 垂直的唯一平面。",
    "en_problem": f"Given that the bottom surface of the triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} is an equilateral triangle, the side {point_B}{point_B1}{point_C1}{point_C} is a rectangle, {point_M}, {point_N} are the midpoints of {point_B}{point_C}, {point_B1}{point_C1} respectively, and {point_P} is a point on {point_A}{point_M}. The plane passing through {point_B1}{point_C1} and {point_P} intersects {point_A}{point_B} at {point_E} and {point_A}{point_C} at {point_F}. Find the unique plane composed of the points given in the figure that is perpendicular to plane {point_E}{point_B1}{point_C1}{point_F}.",
    "solution": f"{point_A1}{point_A}{point_M}{point_N}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_9_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_M}', '{point_N}', '{point_P}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
