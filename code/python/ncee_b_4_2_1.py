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
point_P, point_A, point_B, point_C, point_D, point_E, point_O, point_F = random.sample(string.ascii_uppercase, 8)

# Generate random lengths
len_a = 1.0
len_a = round(len_scaling_factor * float(len_a), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_2_1",
    "type": 1,
    "level": 3,
    "cn_problem": f"在三棱锥{point_P}-{point_A}{point_B}{point_C}中，{point_A}{point_B}⊥{point_B}{point_C}，{point_A}{point_B}=2*{len_a}，{point_B}{point_C}=2√2*{len_a}，{point_P}{point_B}={point_P}{point_C}=√6*{len_a}（{len_a}>0），{point_B}{point_P}，{point_A}{point_P}，{point_B}{point_C}的中点分别为{point_D}，{point_E}，{point_O}，点{point_F}在{point_A}{point_C}上，{point_B}{point_F}⊥{point_A}{point_O}。过点{point_A}与线段{point_E}{point_F}平行的唯一个由顶点或中点确定的平面是哪个？",
    "en_problem": f"In the triangular pyramid {point_P}-{point_A}{point_B}{point_C}, {point_A}{point_B}⊥{point_B}{point_C}, {point_A}{point_B}=2*{len_a}, {point_B}{point_C}=2√2*{len_a}, {point_P}{point_B}={point_P}{point_C}=√6*{len_a} ({len_a}>0). The midpoints of {point_B}{point_P}, {point_A}{point_P}, and {point_B}{point_C} are {point_D}, {point_E}, and {point_O} respectively, and point {point_F} is on {point_A}{point_C} with {point_B}{point_F}⊥{point_A}{point_O}. Which unique plane determined by vertices or midpoints and passing through point {point_A} is parallel to the line segment {point_E}{point_F}?",
    "solution": f"{point_A}{point_D}{point_O}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_2_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_O}', '{point_F}')"}, ensure_ascii=False) + "\n")
