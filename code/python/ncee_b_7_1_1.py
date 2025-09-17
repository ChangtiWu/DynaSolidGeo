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
point_A, point_B, point_C, point_D, point_E, point_F, point_P = random.sample(string.ascii_uppercase, 7)

# Generate random lengths
len_a = 1
len_a = round(len_scaling_factor * float(len_a), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_1_1",
    "type": 1,
    "level": 2,
    "cn_problem": f"平面四边形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_B}=8*{len_a}，{point_C}{point_D}=3*{len_a}，{point_A}{point_D}=5√3*{len_a}，∠{point_A}{point_D}{point_C}=90°，∠{point_B}{point_A}{point_D}=30°（{len_a}>0），点{point_E}，{point_F}满足\\(\\overrightarrow{{AE}} = \\frac{{2}}{{5}}\\overrightarrow{{AD}}\\)，\\(\\overrightarrow{{AF}} = \\frac{{1}}{{2}}\\overrightarrow{{AB}}\\)，将△{point_A}{point_E}{point_F}沿{point_E}{point_F}翻折至△{point_P}{point_E}{point_F}，使得{point_P}{point_C}=4√3*{len_a}。求图上与{point_P}{point_D}垂直的唯一的直线是哪个？",
    "en_problem": f"In the planar quadrilateral {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B}=8*{len_a}, {point_C}{point_D}=3*{len_a}, {point_A}{point_D}=5√3*{len_a}, ∠{point_A}{point_D}{point_C}=90°, ∠{point_B}{point_A}{point_D}=30° ({len_a}>0). Points {point_E} and {point_F} satisfy \\(\\overrightarrow{{AE}} = \\frac{{2}}{{5}}\\overrightarrow{{AD}}\\), \\(\\overrightarrow{{AF}} = \\frac{{1}}{{2}}\\overrightarrow{{AB}}\\). Fold △{point_A}{point_E}{point_F} along {point_E}{point_F} to △{point_P}{point_E}{point_F} such that {point_P}{point_C}=4√3*{len_a}. Which unique line in the figure is perpendicular to {point_P}{point_D}?",
    "solution": f"{point_E}{point_F}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_1_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_P}')"}, ensure_ascii=False) + "\n")
