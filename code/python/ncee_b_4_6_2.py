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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_E, point_F, point_D = random.sample(string.ascii_uppercase, 9)

# Generate random lengths
len_s = 1.0
len_s = round(len_scaling_factor * float(len_s), 2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_6_2",
    "type": 1,
    "level": 3,
    "cn_problem": f"已知直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中：(1) 底面 △{point_A}{point_B}{point_C} 为直角等腰三角形，∠{point_A}{point_B}{point_C}=90°，{point_A}{point_B}={point_B}{point_C}={len_s}>0；(2) 侧面 {point_A}{point_A1}{point_B1}{point_B} 为正方形，即 {point_A}{point_A1}={point_B}{point_B1}={len_s}；(3) 中点：{point_E}=mid({point_A}{point_C})，{point_F}=mid({point_C}{point_C1})；(4) 点 {point_D} 为棱 {point_A1}{point_B1} 上的任意点。与线段 {point_D}{point_E} 垂直的唯一条由点集 {{{point_A},{point_B},{point_C},{point_D},{point_E},{point_F},{point_A1},{point_B1},{point_C1}}} 确定的线段是哪条？",
    "en_problem": f"In right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}: (1) the base △{point_A}{point_B}{point_C} is a right isosceles triangle with ∠{point_A}{point_B}{point_C}=90°, {point_A}{point_B}={point_B}{point_C}={len_s}>0; (2) the lateral face {point_A}{point_A1}{point_B1}{point_B} is a square, i.e., {point_A}{point_A1}={point_B}{point_B1}={len_s}; (3) midpoints: {point_E}=mid({point_A}{point_C}), {point_F}=mid({point_C}{point_C1}); (4) point {point_D} is any point on edge {point_A1}{point_B1}. Which is the unique line segment determined by the point set {{{point_A},{point_B},{point_C},{point_D},{point_E},{point_F},{point_A1},{point_B1},{point_C1}}} that is perpendicular to line segment {point_D}{point_E}?",
    "solution": f"{point_B}{point_F}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_6_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_E}', '{point_F}', '{point_D}')"}, ensure_ascii=False) + "\n")
