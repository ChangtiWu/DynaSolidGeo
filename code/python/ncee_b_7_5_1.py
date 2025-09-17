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
point_A, point_B, point_C, point_D, point_E = random.sample(string.ascii_uppercase, 5)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_5_1",
    "type": 1,
    "level": 2,
    "cn_problem": f"如图，三棱锥 {point_A}-{point_B}{point_C}{point_D} 中，{point_D}{point_A} = {point_D}{point_B} = {point_D}{point_C}，{point_B}{point_D}⊥{point_C}{point_D}，∠{point_A}{point_D}{point_B} = ∠{point_A}{point_D}{point_C} = 60°，{point_E} 为 {point_B}{point_C} 的中点。求由点 {point_A}{point_B}{point_C}{point_D} 构成的，与 {point_B}{point_C} 垂直的唯一的直线是哪条？",
    "en_problem": f"As shown in the figure, in the triangular pyramid {point_A}-{point_B}{point_C}{point_D}, {point_D}{point_A} = {point_D}{point_B} = {point_D}{point_C}, {point_B}{point_D}⊥{point_C}{point_D}, ∠{point_A}{point_D}{point_B} = ∠{point_A}{point_D}{point_C} = 60°, and {point_E} is the midpoint of {point_B}{point_C}. Which is the unique straight line formed by points {point_A}{point_B}{point_C}{point_D} that is perpendicular to {point_B}{point_C}?",
    "solution": f"{point_D}{point_A}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_5_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
