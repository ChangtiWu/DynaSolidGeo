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
point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math


def calculate(len_a: float, arg_beta: float) -> float:
    """计算 len_h 的平方（公式：len_h² = (len_a²/4)·tan²(arg_beta)）"""
    tan_squared = math.tan(arg_beta) ** 2
    return (len_a ** 2 / 4) * tan_squared


len_a = 12.0
arg_beta = math.pi / 3

# result = calculate(len_a, arg_beta)
# print(f"len_h² = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, arg_beta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_16_aimeI_4",
    "type": 3,
    "level": 2,
    "cn_problem": f"有一正六棱柱，其底面为边长 ${len_a}>0$ 的正六边形，上、下底面互相平行，柱高记为 $len_h$。取下底面某顶点 ${point_A}$，以及与 ${point_A}$ 相邻的两个下底顶点 ${point_B},{point_C}$ 和上底面中与 ${point_A}$ 对应的顶点 ${point_D}$，构成四面体 ${point_A}{point_B}{point_C}{point_D}$。设四面体两个面 $\\triangle {point_A}{point_B}{point_C}$（位于下底面内）与 $\\triangle {point_B}{point_C}{point_D}$（不含点 ${point_A}$ 的侧面）之间的二面角为 ${arg_beta}\\ (0<{arg_beta}<\\frac{{\\pi}}{2})$。求柱高 $len_h$ 的平方 $len_h^{2}$ 。",
    "en_problem": f"There is a regular hexagonal prism with base being a regular hexagon of side length ${len_a}>0$, and the upper and lower bases are parallel to each other, with prism height denoted as $len_h$. Take a vertex ${point_A}$ of the lower base, along with two adjacent lower base vertices ${point_B},{point_C}$ and the corresponding vertex ${point_D}$ on the upper base, forming tetrahedron ${point_A}{point_B}{point_C}{point_D}$. Let the dihedral angle between the two faces $\\triangle {point_A}{point_B}{point_C}$ (lying within the lower base) and $\\triangle {point_B}{point_C}{point_D}$ (the side face not containing point ${point_A}$) be ${arg_beta}\\ (0<{arg_beta}<\\frac{{\\pi}}{2})$. Find the explicit formula for the square of the prism height $len_h^{2}$.",
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
    f.write(json.dumps({json_data["id"]: f"aops_16_aimeI_4({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
