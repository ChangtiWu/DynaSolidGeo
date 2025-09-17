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
point_A, point_M, point_N, point_B, point_D, point_C, point_E, point_F = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_t, arg_theta):
    """计算len_L的值（表达式为len_t乘以(1 + sin(arg_theta/2))）"""
    return len_t * (1 + math.sin(arg_theta / 2))


# 测试示例
len_t = 1.0
arg_theta = math.pi / 3

# print(calculate(len_t, arg_theta))

# Generate random lengths
len_t = round(len_scaling_factor * float(len_t), 2)

# Calculate the result
result = calculate(len_t, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_44_1",
    "type": 8,
    "level": 2,
    "cn_problem": f"在翻折后的空间几何体中，设 ${point_A}{point_M} = {point_M}{point_N} = {len_t}$（翻折前由直角梯形对称性，${point_A}{point_M}$ 为等腰直角三角形 $\\\\triangle {point_A}{point_B}{point_D}$ 斜边中线，${point_M}{point_N}$ 为 $\\\\triangle {point_B}{point_C}{point_D}$ 中位线，故 ${point_A}{point_M} = {point_M}{point_N}$），二面角 ${point_A}-{point_B}{point_D}-{point_C}$ 的平面角为 ${arg_theta}$。{point_M}、{point_N} 分别是 ${point_B}{point_D}$ 和 ${point_B}{point_C}$ 中点，{point_E} 是线段 ${point_B}{point_N}$ 的中点，动点 {point_F} 在三棱锥 ${point_A}-{point_B}{point_M}{point_N}$ 表面上运动，且总保持 ${point_F}{point_E} \\\\perp {point_B}{point_D}$，求动点 {point_F} 的轨迹长度。",
    "en_problem": f"In the spatial geometry after folding, let ${point_A}{point_M} = {point_M}{point_N} = {len_t}$ (before folding, by symmetry of right trapezoid, ${point_A}{point_M}$ is the median to hypotenuse of isosceles right triangle $\\\\triangle {point_A}{point_B}{point_D}$, ${point_M}{point_N}$ is the midline of $\\\\triangle {point_B}{point_C}{point_D}$, so ${point_A}{point_M} = {point_M}{point_N}$), and the plane angle of dihedral angle ${point_A}-{point_B}{point_D}-{point_C}$ is ${arg_theta}$. {point_M} and {point_N} are midpoints of ${point_B}{point_D}$ and ${point_B}{point_C}$ respectively, {point_E} is the midpoint of segment ${point_B}{point_N}$, moving point {point_F} moves on the surface of tetrahedron ${point_A}-{point_B}{point_M}{point_N}$ and always maintains ${point_F}{point_E} \\\\perp {point_B}{point_D}$. Find the trajectory length of moving point {point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_44_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_M}', '{point_N}', '{point_B}', '{point_D}', '{point_C}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
