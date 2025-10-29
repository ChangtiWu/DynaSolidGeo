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
point_A, point_B, point_C, point_D, point_G, point_M = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算四面体 MBCD 的外接球表面积

    参数:
    len_a (float): 正四面体边长

    返回:
    float: 外接球表面积
    """
    return (3 / 2) * math.pi * len_a**2


# 题干给定的数值
len_a = 1.0  # 正四面体边长

# 验证输出
# surface_area = calculate(len_a)
# print(f"外接球表面积: {surface_area:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_10_4",
    "type": 4,
    "level": 2,
    "cn_problem": f"在棱长为{len_a}的正四面体{point_A}{point_B}{point_C}{point_D}中，{point_G}为△{point_B}{point_C}{point_D}的重心，{point_M}是线段{point_A}{point_G}的中点。求四面体{point_M}{point_B}{point_C}{point_D}的外接球的表面积。",
    "en_problem": f"In a regular tetrahedron {point_A}{point_B}{point_C}{point_D} with edge length {len_a}, {point_G} is the centroid of triangle {point_B}{point_C}{point_D}, and {point_M} is the midpoint of segment {point_A}{point_G}. Find the surface area of the circumsphere of tetrahedron {point_M}{point_B}{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_10_4({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_G}', '{point_M}')"}, ensure_ascii=False) + "\n")
