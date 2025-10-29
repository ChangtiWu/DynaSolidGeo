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
point_A = random.sample(string.ascii_uppercase, 1)[0]

# Add result calculation code
import math


def calculate(len_a: float) -> float:
    """计算切割后体积 volume_O_cut 的表达式值（volume_O_cut = [(10-7√2)/3]·len_a³）"""
    coefficient = (10 - 7 * math.sqrt(2)) / 3
    return coefficient * (len_a ** 3)


len_a = 1.0

# result = calculate(len_a)
# print(f"volume_O_cut = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_07_amc12A_20",
    "type": 5,
    "level": 1,
    "cn_problem": f"设一个棱长为 {len_a}>0 的正方体，其 8 个顶点 {point_A} 都被截去，使得截后 6 个原始正方形面均变为正八边形。每一顶点 {point_A} 被截去的部分都是与三条相邻棱垂直的直角四面体（顶点处的小角锥）。求这 8 个小四面体总体积。",
    "en_problem": f"Consider a cube with edge length {len_a}>0. All 8 vertices {point_A} are cut off such that the 6 original square faces become regular octagons. Each vertex {point_A} that is cut off forms a right tetrahedron (small pyramid at the vertex) perpendicular to the three adjacent edges. Find the total volume of all 8 small tetrahedra.",
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
    f.write(json.dumps({json_data["id"]: f"aops_07_amc12A_20({mode}, {azimuth}, {elevation}, '{point_A}')"}, ensure_ascii=False) + "\n")
