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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_P, point_Q = random.sample(string.ascii_uppercase, 10)

# Generate random lengths
len_a = 3.0
len_a = round(len_scaling_factor * float(len_a), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_26_1",
    "type": 1,
    "level": 2,
    "cn_problem": f"已知四棱台 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 的上、下底面分别是边长为 {len_a} 和 2*{len_a} 的正方形，{point_A1}{point_A} = 2*{len_a}，且 {point_A1}{point_A} ⊥ 底面 {point_A}{point_B}{point_C}{point_D}，点 {point_P}，{point_Q} 分别在棱 {point_D}{point_D1}，{point_B}{point_C} 上，{point_P} 是 {point_D}{point_D1} 的中点。求由图上给出的点组成的唯一一定与 {point_P}{point_Q} 垂直的线段。",
    "en_problem": f"Given that the upper and lower bases of the quadrangular frustum {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} are squares with side lengths {len_a} and 2*{len_a} respectively, {point_A1}{point_A} = 2*{len_a}, and {point_A1}{point_A} ⊥ the base {point_A}{point_B}{point_C}{point_D}, points {point_P}, {point_Q} are respectively on the edges {point_D}{point_D1}, {point_B}{point_C}, and {point_P} is the midpoint of {point_D}{point_D1}. Find the unique line segment composed of the points given in the figure that is necessarily perpendicular to {point_P}{point_Q}.",
    "solution": f"{point_A}{point_B1}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_26_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_P}', '{point_Q}')"}, ensure_ascii=False) + "\n")
