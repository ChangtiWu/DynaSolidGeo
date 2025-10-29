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
point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
def calculate():
    """计算cosθ的值（根据给定表达式返回2/3）"""
    return 2 / 3


# 测试示例
len_a = 4.0

# result = calculate()
# print(result)

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_42_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在几何体{point_A}{point_B}{point_C}{point_D}{point_E}中，四边形{point_A}{point_B}{point_C}{point_D}是矩形，{point_A}{point_B}⊥平面{point_B}{point_E}{point_C}，{point_B}{point_E}⊥{point_E}{point_C}，{point_A}{point_B}={point_B}{point_E}={point_E}{point_C}={len_a}，{point_F}是线段{point_D}{point_C}的中点。求平面{point_A}{point_E}{point_F}与平面{point_B}{point_E}{point_C}所成锐二面角的余弦值。",
    "en_problem": f"In polyhedron {point_A}{point_B}{point_C}{point_D}{point_E}, quadrilateral {point_A}{point_B}{point_C}{point_D} is a rectangle, {point_A}{point_B}⊥plane {point_B}{point_E}{point_C}, {point_B}{point_E}⊥{point_E}{point_C}, {point_A}{point_B}={point_B}{point_E}={point_E}{point_C}={len_a}, {point_F} is the midpoint of segment {point_D}{point_C}. Find the cosine value of the acute dihedral angle between plane {point_A}{point_E}{point_F} and plane {point_B}{point_E}{point_C}.",
    "solution": f"{result}",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_42_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
