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
point_P, point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
def calculate(len_p):
    """
    计算给定参数对应的体积V。

    参数:
        len_p (float): 长度参数（需满足 len_p > 0）。

    返回:
        float: 计算得到的体积V。
    """
    # 计算 len_p 的三次方
    len_p_cubed = len_p ** 3
    # 计算体积 V
    V = len_p_cubed / 162
    return V


len_p = 6.0

# V = calculate(len_p)
# print(f"体积 V = {V:.4f}")
# Generate random lengths
len_p = round(len_scaling_factor * float(len_p), 2)

# Calculate the result
result = calculate(len_p)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_22_2",
    "type": 5,
    "level": 2,
    "cn_problem": f"设正三棱锥 {point_P}-{point_A}{point_B}{point_C} 满足：\n1. 侧棱相等 {point_P}{point_A}={point_P}{point_B}={point_P}{point_C}={len_p}（{len_p}>0）；\n2. 三个侧面均为直角等腰三角形，其直角顶点都在 {point_P}。\n记 {point_D} 为 {point_P} 在底面 {point_A}{point_B}{point_C} 上的垂足；{point_E} 为 {point_D} 在平面 {point_P}{point_A}{point_B} 上的垂足；\n作 {point_F} 为 {point_E} 在平面 {point_P}{point_A}{point_C} 上的垂足。\n求四面体 {point_P}{point_D}{point_E}{point_F} 的体积 V。",
    "en_problem": f"Consider a regular triangular pyramid {point_P}-{point_A}{point_B}{point_C} such that:\n1. All lateral edges are equal: {point_P}{point_A}={point_P}{point_B}={point_P}{point_C}={len_p} ({len_p}>0);\n2. Each lateral face is a right isosceles triangle with its right angle at {point_P}.\nLet {point_D} be the foot of the perpendicular from {point_P} to the base {point_A}{point_B}{point_C}. Let {point_E} be the foot of the perpendicular from {point_D} to the plane {point_P}{point_A}{point_B}. Construct {point_F}, the foot of the perpendicular from {point_E} to the plane {point_P}{point_A}{point_C}.\nFind the volume V of tetrahedron {point_P}{point_D}{point_E}{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_22_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
