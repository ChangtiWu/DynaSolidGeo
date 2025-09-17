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
point_P, point_A, point_B, point_C, point_D, point_M, point_N = random.sample(string.ascii_uppercase, 7)

# Generate random lengths
len_a = 1.0
len_a = round(len_scaling_factor * float(len_a), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_27_1",
    "type": 1,
    "level": 2,
    "cn_problem": f"四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}中，{point_P}{point_A}⊥底面{point_A}{point_B}{point_C}{point_D}，{point_A}{point_D}∥{point_B}{point_C}，{point_A}{point_B}={point_A}{point_D}={point_A}{point_C}=3*{len_a}，{point_P}{point_A}={point_B}{point_C}=4*{len_a}（{len_a}>0），{point_M}为线段{point_A}{point_D}上一点，{point_A}{point_M}=2*{point_M}{point_D}，{point_N}为{point_P}{point_C}的中点。求图上与直线{point_M}{point_N}平行的唯一的平面是哪个？",
    "en_problem": f"In the quadrangular pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, {point_P}{point_A}⊥ the bottom surface {point_A}{point_B}{point_C}{point_D}, {point_A}{point_D}∥{point_B}{point_C}, {point_A}{point_B}={point_A}{point_D}={point_A}{point_C}=3*{len_a}, {point_P}{point_A}={point_B}{point_C}=4*{len_a} ({len_a}>0), {point_M} is a point on the line segment {point_A}{point_D}, {point_A}{point_M}=2*{point_M}{point_D}, and {point_N} is the midpoint of {point_P}{point_C}. Which unique plane in the figure is parallel to the line {point_M}{point_N}?",
    "solution": f"{point_P}{point_A}{point_B}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_27_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
