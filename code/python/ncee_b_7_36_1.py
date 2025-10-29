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

# Generate random lengths
len_a = 1
len_a = round(len_scaling_factor * float(len_a), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_36_1",
    "type": 1,
    "level": 2,
    "cn_problem": f"三棱锥{point_P}-{point_A}{point_B}{point_C}中，{point_P}{point_C}⊥平面{point_A}{point_B}{point_C}，{point_P}{point_C}=3*{len_a}，∠{point_A}{point_C}{point_B}=π/2，{point_D}，{point_E}分别为线段{point_A}{point_B}，{point_B}{point_C}上的点，且{point_C}{point_D}={point_D}{point_E}=√2*{len_a}，{point_C}{point_E}=2*{point_E}{point_B}=2*{len_a}（{len_a}>0）。求图上与{point_D}{point_E}垂直的唯一平面是哪个？",
    "en_problem": f"In the triangular pyramid {point_P}-{point_A}{point_B}{point_C}, {point_P}{point_C}⊥ plane {point_A}{point_B}{point_C}, {point_P}{point_C}=3*{len_a}, ∠{point_A}{point_C}{point_B}=π/2, {point_D} and {point_E} are points on line segments {point_A}{point_B} and {point_B}{point_C} respectively, and {point_C}{point_D}={point_D}{point_E}=√2*{len_a}, {point_C}{point_E}=2*{point_E}{point_B}=2*{len_a} ({len_a}>0). Which unique plane in the figure is perpendicular to {point_D}{point_E}?",
    "solution": f"{point_P}{point_C}{point_D}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_36_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
