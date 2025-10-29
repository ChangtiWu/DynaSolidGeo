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
point_M, point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_p):
    """计算len_R的值（当t=√2·len_p时）"""
    return (math.sqrt(5) / 5) * len_p


# 测试示例
len_p = 1.0
area_A = 1.0
# print(calculate(len_p))

# Generate random lengths
len_p = round(len_scaling_factor * float(len_p), 2)
area_A = round(len_scaling_factor * float(area_A), 2)

# Calculate the result
result = calculate(len_p)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_12_4",
    "type": 3,
    "level": 3,
    "cn_problem": f"设四棱锥 ${point_M}\\text{{-}}{point_A}{point_B}{point_C}{point_D}$ 的底面 ${point_A}{point_B}{point_C}{point_D}$ 是边长为 ${len_p} > 0$ 的正方形。顶点 ${point_M}$ 满足 $|{point_M}{point_A}| = |{point_M}{point_D}| = {len_p}$ 且 ${point_M}{point_A} \\perp {point_A}{point_B}$，使得三角形 $\\triangle {point_A}{point_M}{point_D}$ 的面积为 ${area_A} > 0$。记 $t = \\frac{{2*{area_A}}}{{{len_p}}} > 0$（从顶点到底边 ${point_A}{point_D}$ 的高）。在侧面 ${point_M}{point_A}{point_D}$ 内取垂足 ${point_E}$ 使 ${point_M}{point_E} \\perp {point_A}{point_D}$，在底面内取 ${point_F}$ 为 ${point_B}{point_C}$ 的中点。当 $|{point_M}{point_E}| = |{point_E}{point_F}| = t$，$|{point_M}{point_F}| = {len_p}$ 时，$\\triangle {point_M}{point_E}{point_F}$ 的内切圆半径为 $ len_r  = \\frac{{1}}{{2}}(2t - {len_p})$。求四棱锥内能容纳的最大球半径 $ len_R $。",
    "en_problem": f"Let pyramid ${point_M}\\text{{-}}{point_A}{point_B}{point_C}{point_D}$ have a square base ${point_A}{point_B}{point_C}{point_D}$ with side length ${len_p} > 0$. Vertex ${point_M}$ satisfies $|{point_M}{point_A}| = |{point_M}{point_D}| = {len_p}$ and ${point_M}{point_A} \\perp {point_A}{point_B}$, such that triangle $\\triangle {point_A}{point_M}{point_D}$ has area ${area_A} > 0$. Let $t = \\frac{{2*{area_A}}}{{{len_p}}} > 0$ (the height from vertex to base edge ${point_A}{point_D}$). In face ${point_M}{point_A}{point_D}$, take foot ${point_E}$ such that ${point_M}{point_E} \\perp {point_A}{point_D}$, and in the base, take ${point_F}$ as the midpoint of ${point_B}{point_C}$. When $|{point_M}{point_E}| = |{point_E}{point_F}| = t$ and $|{point_M}{point_F}| = {len_p}$, the incircle radius of $\\triangle {point_M}{point_E}{point_F}$ is $ len_r  = \\frac{{1}}{{2}}(2t - {len_p})$. Find the maximum radius $ len_R $ of a sphere that can be inscribed in the pyramid.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_12_4({mode}, {azimuth}, {elevation}, '{point_M}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
