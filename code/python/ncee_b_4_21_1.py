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
    "id": "ncee_b_4_21_1",
    "type": 1,
    "level": 2,
    "cn_problem": f"四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}中，{point_P}{point_A}⊥平面{point_A}{point_B}{point_C}{point_D}，{point_A}{point_D}∥{point_B}{point_C}，{point_A}{point_B}={point_A}{point_D}={point_A}{point_C}=3*{len_a}，{point_P}{point_A}={point_B}{point_C}=4*{len_a}（{len_a}>0），{point_M}为线段{point_A}{point_D}上一点，{point_A}{point_M}=2*{point_M}{point_D}，{point_N}为{point_P}{point_C}的中点。在由点集 {{{point_A},{point_B},{point_C},{point_D},{point_P},{point_M},{point_N}}} 两两连线所得的所有直线中，唯一与平面{point_P}{point_A}{point_B}平行的直线是哪条？",
    "en_problem": f"In the quadrangular pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, {point_P}{point_A}⊥ plane {point_A}{point_B}{point_C}{point_D}, {point_A}{point_D}∥{point_B}{point_C}, {point_A}{point_B}={point_A}{point_D}={point_A}{point_C}=3*{len_a}, {point_P}{point_A}={point_B}{point_C}=4*{len_a} ({len_a}>0), {point_M} is a point on the line segment {point_A}{point_D}, {point_A}{point_M}=2*{point_M}{point_D}, and {point_N} is the midpoint of {point_P}{point_C}. Among all the lines formed by pairwise connections of the point set {{{point_A},{point_B},{point_C},{point_D},{point_P},{point_M},{point_N}}}, which line is uniquely parallel to the plane {point_P}{point_A}{point_B}?",
    "solution": f"{point_M}{point_N}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_21_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
