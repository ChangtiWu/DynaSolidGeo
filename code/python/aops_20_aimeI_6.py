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

# Add result calculation code
def calculate(distance: float, radius_1: float, radius_2: float) -> float:
    """计算球半径平方的表达式值（sphere_radius²）"""
    numerator = (distance ** 2 - (radius_1 ** 2 + radius_2 ** 2)) ** 2 - 4 * radius_1 ** 2 * radius_2 ** 2
    denominator = 4 * (distance ** 2 - 2 * (radius_1 ** 2 + radius_2 ** 2))
    return numerator / denominator


distance = 7.0
radius_1 = 1.0
radius_2 = 2.0

# result = calculate(distance, radius_1, radius_2)
# print(f"sphere_radius² = {result:.6f}")

# Generate random lengths
radius_1 = round(len_scaling_factor * float(radius_1), 2)
radius_2 = round(len_scaling_factor * float(radius_2), 2)
distance = round(len_scaling_factor * float(distance), 2)

# Calculate the result
result = calculate(distance, radius_1, radius_2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_20_aimeI_6",
    "type": 3,
    "level": 1,
    "cn_problem": f"一块水平木板上沿直线方向钻有两个完全贯通的圆孔，较小孔半径为 ${radius_1}>0$，较大孔半径为 ${radius_2}>{radius_1}$。两孔圆心之间的距离为 ${distance}$（满足 ${distance}>{radius_1}+{radius_2}$）。现有两个全等球体，各半径均为 $sphere_radius$，分别安放在两孔中，并且每个球与自己所在圆孔的圆周相切；两球在木板上方恰好互相外切。求球半径平方 $sphere_radius^{2}$ 。",
    "en_problem": f"A horizontal wooden board has two completely penetrating circular holes drilled along a straight line. The smaller hole has radius ${radius_1}>0$, and the larger hole has radius ${radius_2}>{radius_1}$. The distance between the centers of the two holes is ${distance}$ (satisfying ${distance}>{radius_1}+{radius_2}$). Two congruent spheres, each with radius $sphere_radius$, are placed in the two holes such that each sphere is tangent to the circumference of its hole, and the two spheres are externally tangent to each other above the board. Find the explicit expression for the square of the sphere radius $sphere_radius^{2}$ in terms of $({radius_1},{radius_2},{distance})$.",
    "solution": f"{result}",
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
    f.write(json.dumps({json_data["id"]: f"aops_20_aimeI_6({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
