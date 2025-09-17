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
point_A, point_B, point_C, point_D, point_E, point_F, point_G, point_H, point_M, point_N = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
def calculate(len_a: float) -> float:
    """计算最大体积 volume_O 的最大值（volume_O_max = (41/48)·len_a³）"""
    return (41 / 48) * (len_a ** 3)


len_a = 1.0

# result = calculate(len_a)
# print(f"volume_O_max = {result:.6f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_12_aimeI_8",
    "type": 5,
    "level": 2,
    "cn_problem": f"设正方体 {point_A}{point_B}{point_C}{point_D}{point_E}{point_F}{point_G}{point_H} 的棱长为 {len_a}>0。记边 $\\overline{{{point_A}{point_B}}}$ 的中点为 {point_M}，边 $\\overline{{{point_C}{point_G}}}$ 的中点为 {point_N}。过三点 {point_D},{point_M},{point_N} 作平面，将正方体分成两个多面体。求其中体积较大的那一部分。",
    "en_problem": f"Let cube {point_A}{point_B}{point_C}{point_D}{point_E}{point_F}{point_G}{point_H} have edge length {len_a}>0. Let {point_M} be the midpoint of edge $\\overline{{{point_A}{point_B}}}$ and {point_N} be the midpoint of edge $\\overline{{{point_C}{point_G}}}$. A plane is made through the three points {point_D}, {point_M}, {point_N}, dividing the cube into two polyhedra. Find the larger volume.",
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
    f.write(json.dumps({json_data["id"]: f"aops_12_aimeI_8({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_G}', '{point_H}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
