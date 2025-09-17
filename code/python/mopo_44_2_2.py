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
point_A, point_B, point_C, point_D, point_M, point_N, point_P, point_Q = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate():
    """返回区间 [1, √2] 的列表形式"""
    return math.sqrt(2)


# 测试示例
len_b = 2 * math.sqrt(2)
len_a = math.sqrt(2)

# print(calculate())

# Generate random lengths
len_b = round(len_scaling_factor * float(len_b), 2)
len_a = round(len_scaling_factor * float(len_a), 2)


# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_44_2_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在直角梯形 {point_A}{point_B}{point_C}{point_D} 中，${point_A}{point_D} \\\\parallel {point_B}{point_C}$，${point_B}{point_C} = 2*{point_A}{point_D} = 2*{point_A}{point_B} = {len_b}$（即 ${point_A}{point_D} = {point_A}{point_B} = {len_a}$，${point_B}{point_C} = 2*{len_a}$），$\\\\angle {point_A}{point_B}{point_C} = 90°$。将 $\\\\triangle {point_A}{point_B}{point_D}$ 沿 ${point_B}{point_D}$ 翻折，二面角 ${point_A}-{point_B}{point_D}-{point_C}$ 的平面角为 $ arg_theta $，{point_M}、{point_N} 分别为 ${point_B}{point_D}$、${point_B}{point_C}$ 的中点。若 {point_P}、{point_Q} 分别在 ${point_A}{point_B}$、${point_D}{point_N}$ 上，满足 $\\\\frac{{{point_A}{point_P}}}{{{point_P}{point_B}}} = \\\\frac{{{point_N}{point_Q}}}{{{point_Q}{point_D}}} = //lambda$（$//lambda \\\\in \\\\mathbb{{R}}$），记 {point_P}{point_Q} 与 ${point_B}{point_D}$、${point_A}{point_N}$ 所成角为 $ arg_theta_1 $、$ arg_theta_2 $，求 $\\\\sin  arg_theta_1  + \\\\sin  arg_theta_2 $ 的最大值。",
    "en_problem": f"In right trapezoid {point_A}{point_B}{point_C}{point_D}, ${point_A}{point_D} \\\\parallel {point_B}{point_C}$, ${point_B}{point_C} = 2*{point_A}{point_D} = 2*{point_A}{point_B} = {len_b}$ (i.e., ${point_A}{point_D} = {point_A}{point_B} = {len_a}$, ${point_B}{point_C} = 2*{len_a}$), $\\\\angle {point_A}{point_B}{point_C} = 90°$. Fold $\\\\triangle {point_A}{point_B}{point_D}$ along ${point_B}{point_D}$ so that the plane angle of dihedral angle ${point_A}-{point_B}{point_D}-{point_C}$ is $ arg_theta $. Let {point_M}, {point_N} be midpoints of ${point_B}{point_D}$, ${point_B}{point_C}$ respectively. If {point_P}, {point_Q} are on ${point_A}{point_B}$, ${point_D}{point_N}$ respectively, satisfying $\\\\frac{{{point_A}{point_P}}}{{{point_P}{point_B}}} = \\\\frac{{{point_N}{point_Q}}}{{{point_Q}{point_D}}} = //lambda$ ($//lambda \\\\in \\\\mathbb{{R}}$), and {point_P}{point_Q} makes angles $ arg_theta_1 $, $ arg_theta_2 $ with ${point_B}{point_D}$, ${point_A}{point_N}$ respectively, find the maximum value of $\\\\sin  arg_theta_1  + \\\\sin  arg_theta_2 $.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_44_2_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}', '{point_N}', '{point_P}', '{point_Q}')"}, ensure_ascii=False) + "\n")
