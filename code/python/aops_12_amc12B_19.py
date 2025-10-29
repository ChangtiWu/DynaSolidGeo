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
point_A1, point_A2, point_A3, point_A4, point_A1prime, point_A2prime, point_A3prime, point_A4prime = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a: float) -> float:
    """计算正八面体边长 octahedron_edge 的表达式值（octahedron_edge = (3√2/4)·len_a）"""
    ratio_x = 3 / 4  # 固定比例常数
    octahedron_edge = ratio_x * math.sqrt(2) * len_a
    return octahedron_edge


len_a = 1.0

# result = calculate(len_a)
# print(f"octahedron_edge = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_12_amc12B_19",
    "type": 3,
    "level": 2,
    "cn_problem": f"设正方体 {point_A1}{point_A2}{point_A3}{point_A4}{point_A1prime}{point_A2prime}{point_A3prime}{point_A4prime} 的棱长为 {len_a}>0。其中 {point_A1}{point_A1prime} 为体对角线上的对顶点，且 {point_A2},{point_A3},{point_A4} 为 {point_A1} 的三个邻点，{point_A2prime},{point_A3prime},{point_A4prime} 为 {point_A1prime} 的三个邻点。分别在 6 条棱 {point_A1}{point_A2}, {point_A1}{point_A3}, {point_A1}{point_A4}, {point_A1prime}{point_A2prime}, {point_A1prime}{point_A3prime}, {point_A1prime}{point_A4prime} 上各取一点，使它们到对应立方体顶点 {point_A1} 或 {point_A1prime} 的距离均为 ratio_x\\cdot{len_a}（0<ratio_x<1）。这 6 个点组成一个正八面体。求该正八面体的边长 octahedron_edge。",
    "en_problem": f"Let cube {point_A1}{point_A2}{point_A3}{point_A4}{point_A1prime}{point_A2prime}{point_A3prime}{point_A4prime} have edge length {len_a}>0. Here {point_A1}{point_A1prime} are opposite vertices on the body diagonal, with {point_A2},{point_A3},{point_A4} being the three neighbors of {point_A1}, and {point_A2prime},{point_A3prime},{point_A4prime} being the three neighbors of {point_A1prime}. Take one point on each of the 6 edges {point_A1}{point_A2}, {point_A1}{point_A3}, {point_A1}{point_A4}, {point_A1prime}{point_A2prime}, {point_A1prime}{point_A3prime}, {point_A1prime}{point_A4prime} such that their distances to the corresponding cube vertices {point_A1} or {point_A1prime} are all ratio_x\\cdot{len_a} where 0<ratio_x<1. These 6 points form a regular octahedron. Find the edge length of this regular octahedron.",
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
    f.write(json.dumps({json_data["id"]: f"aops_12_amc12B_19({mode}, {azimuth}, {elevation}, '{point_A1}', '{point_A2}', '{point_A3}', '{point_A4}', '{point_A1prime}', '{point_A2prime}', '{point_A3prime}', '{point_A4prime}')"}, ensure_ascii=False) + "\n")
