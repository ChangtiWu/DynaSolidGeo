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
point_D, point_E, point_F, point_A, point_B, point_C, point_G, point_H = random.sample(string.ascii_uppercase, 8)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_40_1",
    "type": 1,
    "level": 2,
    "cn_problem": f"如图，在三棱台 {point_D}{point_E}{point_F}-{point_A}{point_B}{point_C} 中，{point_A}{point_B} = 2*{point_D}{point_E}，{point_G}，{point_H} 分别为 {point_A}{point_C}，{point_B}{point_C} 的中点。求图上与 {point_B}{point_D} 平行的唯一平面是哪个？",
    "en_problem": f"As shown in the figure, in the triangular prism platform {point_D}{point_E}{point_F}-{point_A}{point_B}{point_C}, {point_A}{point_B} = 2*{point_D}{point_E}, {point_G} and {point_H} are the midpoints of {point_A}{point_C} and {point_B}{point_C} respectively. Which is the unique plane in the figure that is parallel to {point_B}{point_D}?",
    "solution": f"{point_F}{point_G}{point_H}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_40_1({mode}, {azimuth}, {elevation}, '{point_D}', '{point_E}', '{point_F}', '{point_A}', '{point_B}', '{point_C}', '{point_G}', '{point_H}')"}, ensure_ascii=False) + "\n")
