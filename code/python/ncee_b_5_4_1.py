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
point_P, point_D, point_C, point_A, point_B, point_E, point_F, point_G = random.sample(string.ascii_uppercase, 8)

# Generate random lengths
len_a = 1.0
len_a = round(len_scaling_factor * float(len_a), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_5_4_1",
    "type": 1,
    "level": 2,
    "cn_problem": f"三角形△{point_P}{point_D}{point_C}所在的平面与长方形{point_A}{point_B}{point_C}{point_D}所在的平面垂直，{point_P}{point_D}={point_P}{point_C}=4*{len_a}，{point_A}{point_B}=6*{len_a}，{point_B}{point_C}=3*{len_a}（{len_a}>0），点{point_E}是{point_C}{point_D}的中点，点{point_F}、{point_G}分别在线段{point_A}{point_B}、{point_B}{point_C}上，且{point_A}{point_F}=2*{point_F}{point_B}，{point_C}{point_G}=2*{point_G}{point_B}。求由图上顶点构成的与{point_F}{point_G}垂直的唯一的直线是哪条？",
    "en_problem": f"The plane where triangle △{point_P}{point_D}{point_C} is located is perpendicular to the plane where rectangle {point_A}{point_B}{point_C}{point_D} is located, {point_P}{point_D}={point_P}{point_C}=4*{len_a}, {point_A}{point_B}=6*{len_a}, {point_B}{point_C}=3*{len_a} ({len_a}>0), point {point_E} is the midpoint of {point_C}{point_D}, and points {point_F} and {point_G} are on line segments {point_A}{point_B} and {point_B}{point_C} respectively, with {point_A}{point_F}=2*{point_F}{point_B} and {point_C}{point_G}=2*{point_G}{point_B}. Which unique line formed by the vertices in the figure is perpendicular to {point_F}{point_G}?",
    "solution": f"{point_P}{point_E}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_5_4_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_D}', '{point_C}', '{point_A}', '{point_B}', '{point_E}', '{point_F}', '{point_G}')"}, ensure_ascii=False) + "\n")
