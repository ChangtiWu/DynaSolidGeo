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
point_A, point_C, point_B, point_D, point_O, point_E, point_F, point_H, point_D_prime = random.sample(string.ascii_uppercase, 9)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_18_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"菱形 {point_A}{point_B}{point_C}{point_D} 的对角线 {point_A}{point_C} 与 {point_B}{point_D} 交于点 {point_O}，点 {point_E}，{point_F} 分别在 {point_A}{point_D}，{point_C}{point_D} 上，{point_A}{point_E} = {point_C}{point_F}，{point_E}{point_F} 交 {point_B}{point_D} 于点 {point_H}，将△{point_D}{point_E}{point_F} 沿 {point_E}{point_F} 折起到△{point_D_prime}{point_E}{point_F} 的位置。求由 {point_A}、{point_B}、{point_C}、{point_D}、{point_D_prime} 组成的线段中，与 {point_H}{point_D_prime} 唯一垂直的线段。",
    "en_problem": f"The diagonal {point_A}{point_C} and {point_B}{point_D} of rhombus {point_A}{point_B}{point_C}{point_D} intersect at point {point_O}, points {point_E}, {point_F} are respectively on {point_A}{point_D}, {point_C}{point_D}, {point_A}{point_E} = {point_C}{point_F}, {point_E}{point_F} intersects {point_B}{point_D} at point {point_H}, and △{point_D}{point_E}{point_F} is folded along {point_E}{point_F} to the position of △{point_D_prime}{point_E}{point_F}. Find the unique line segment composed of {point_A}, {point_B}, {point_C}, {point_D}, {point_D_prime} that is perpendicular to {point_H}{point_D_prime}.",
    "solution": f"{point_A}{point_C}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_18_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_C}', '{point_B}', '{point_D}', '{point_O}', '{point_E}', '{point_F}', '{point_H}', '{point_D_prime}')"}, ensure_ascii=False) + "\n")
