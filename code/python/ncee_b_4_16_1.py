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
point_P, point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 5)

# Generate random lengths
len_s = 2.0
len_s = round(len_scaling_factor * float(len_s), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_16_1",
    "type": 1,
    "level": 3,
    "cn_problem": f"已知四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 中：(1) 底面四边形 {point_A}{point_B}{point_C}{point_D} 满足 {point_A}{point_B}={point_B}{point_C}={len_s}>0，{point_A}{point_D}=2*{len_s}；(2) 直角条件：∠{point_B}{point_A}{point_D}=∠{point_A}{point_B}{point_C}=90°；(3) 侧面 {point_P}{point_A}{point_D} 为等边三角形且垂直于底面 {point_A}{point_B}{point_C}{point_D}。在由点集 {{{point_A},{point_B},{point_C},{point_D},{point_P}}} 任取三点确定的所有平面中，唯一与线段 {point_B}{point_C} 平行的平面是哪个？",
    "en_problem": f"In quadrilateral pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}: (1) the base quadrilateral {point_A}{point_B}{point_C}{point_D} satisfies {point_A}{point_B}={point_B}{point_C}={len_s}>0, {point_A}{point_D}=2*{len_s}; (2) right angle conditions: ∠{point_B}{point_A}{point_D}=∠{point_A}{point_B}{point_C}=90°; (3) the lateral face {point_P}{point_A}{point_D} is an equilateral triangle perpendicular to the base {point_A}{point_B}{point_C}{point_D}. Among all planes determined by selecting any three points from the set {{{point_A},{point_B},{point_C},{point_D},{point_P}}}, which is the unique plane parallel to line segment {point_B}{point_C}?",
    "solution": f"{point_P}{point_A}{point_D}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_16_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
