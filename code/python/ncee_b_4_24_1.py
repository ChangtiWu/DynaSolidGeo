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
point_A, point_B, point_C, point_D, point_G, point_E = random.sample(string.ascii_uppercase, 6)


# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_24_1",
    "type": 1,
    "level": 3,
    "cn_problem": f"已知几何体中：(1) 四边形 {point_A}{point_B}{point_C}{point_D} 为菱形，边长为  len_s >0；(2) 点 {point_G} 为对角线 {point_A}{point_C} 与 {point_B}{point_D} 的交点（菱形对角线互相垂直）；(3) 点 {point_E} 为平面外一点，满足 {point_B}{point_E}⊥平面 {point_A}{point_B}{point_C}{point_D}，{point_B}{point_E}= len_h >0。在由点集 {{{point_A},{point_B},{point_C},{point_D},{point_E}}} 任取三点所确定的所有平面中，唯一与平面 {point_B}{point_E}{point_D} 垂直的平面是哪个？",
    "en_problem": f"In the given geometric figure: (1) quadrilateral {point_A}{point_B}{point_C}{point_D} is a rhombus with side length  len_s >0; (2) point {point_G} is the intersection of diagonals {point_A}{point_C} and {point_B}{point_D} (rhombus diagonals are perpendicular); (3) point {point_E} is a point outside the plane such that {point_B}{point_E}⊥plane {point_A}{point_B}{point_C}{point_D}, {point_B}{point_E}= len_h >0. Among all planes determined by selecting any three points from the set {{{point_A},{point_B},{point_C},{point_D},{point_E}}}, which is the unique plane perpendicular to plane {point_B}{point_E}{point_D}?",
    "solution": f"{point_A}{point_E}{point_C}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_24_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_G}', '{point_E}')"}, ensure_ascii=False) + "\n")
