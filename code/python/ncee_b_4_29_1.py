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
point_V, point_A, point_B, point_C, point_O, point_M = random.sample(string.ascii_uppercase, 6)

# Generate random lengths
len_a = 1.0
len_a = round(len_scaling_factor * float(len_a), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_29_1",
    "type": 1,
    "level": 1,
    "cn_problem": f"在三棱锥{point_V}-{point_A}{point_B}{point_C}中，平面{point_V}{point_A}{point_B}⊥平面{point_A}{point_B}{point_C}，△{point_V}{point_A}{point_B}为等边三角形，{point_A}{point_C}⊥{point_B}{point_C}且{point_A}{point_C}={point_B}{point_C}=√2*{len_a}（{len_a}>0），{point_O}，{point_M}分别为{point_A}{point_B}，{point_V}{point_A}的中点。在由点集 {{{point_V},{point_B},{point_M},{point_O},{point_C}}} 至少3点确定的所有平面中，唯一与直线{point_V}{point_B}平行的平面是哪个？",
    "en_problem": f"In the triangular pyramid {point_V}-{point_A}{point_B}{point_C}, plane {point_V}{point_A}{point_B}⊥ plane {point_A}{point_B}{point_C}, △{point_V}{point_A}{point_B} is an equilateral triangle, {point_A}{point_C}⊥{point_B}{point_C} and {point_A}{point_C}={point_B}{point_C}=√2*{len_a} ({len_a}>0), {point_O} and {point_M} are the midpoints of {point_A}{point_B} and {point_V}{point_A} respectively. Among all the planes determined by at least 3 points from the point set {{{point_V},{point_B},{point_M},{point_O},{point_C}}}, which plane is uniquely parallel to the line {point_V}{point_B}?",
    "solution": f"{point_M}{point_O}{point_C}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_29_1({mode}, {azimuth}, {elevation}, '{point_V}', '{point_A}', '{point_B}', '{point_C}', '{point_O}', '{point_M}')"}, ensure_ascii=False) + "\n")
