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
point_A, point_B, point_C, point_D, point_P, point_Q, point_M = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_a: float, arg_beta: float, arg_theta: float) -> float:
    """计算 len_x 的值（公式：len_x = (len_a·sin(arg_theta)) / (sin(arg_beta)·√(1+cos²(arg_theta)))）"""
    numerator = len_a * math.sin(arg_theta)
    sin_beta = math.sin(arg_beta)
    cos_theta_sq = math.cos(arg_theta) ** 2
    denominator = sin_beta * math.sqrt(1 + cos_theta_sq)
    return numerator / denominator


len_a = 1.0
arg_beta = math.radians(30)
arg_theta = math.radians(30)

# result = calculate(len_a, arg_beta, arg_theta)
# print(f"len_x = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, arg_beta, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_6_6",
    "type": 3,
    "level": 3,
    "cn_problem": f"在空间中，设平面 ${point_A}{point_B}{point_C}$ 与平面 ${point_B}{point_C}{point_D}$ 交于公共直线 ${point_B}{point_C}$，且二面角 $\\angle({point_A}\\!-\\!{point_B}{point_C}\\!-\\!{point_D})=45^{{\\circ}}$；点 ${point_P}\\in\\triangle {point_A}{point_B}{point_C}$，点 ${point_Q}\\in\\triangle {point_B}{point_C}{point_D}$；点 ${point_M}\\in{point_B}{point_C}$，且 ${point_M}{point_Q}$ 为直线 ${point_P}{point_Q}$ 在平面 ${point_B}{point_C}{point_D}$ 内的射影。已知 ${point_P}{point_M}={len_a}>0$，$\\angle({point_P}{point_Q},{point_B}{point_C}{point_D})={arg_beta}$，$\\angle({point_C}{point_M}{point_Q})={arg_theta}$（$0^{{\\circ}}<{arg_theta}<90^{{\\circ}}$）。求线段 ${point_P}{point_Q}$ 的长。",
    "en_problem": f"In space, let plane ${point_A}{point_B}{point_C}$ and plane ${point_B}{point_C}{point_D}$ intersect at common line ${point_B}{point_C}$, with dihedral angle $\\angle({point_A}\\!-\\!{point_B}{point_C}\\!-\\!{point_D})=45^{{\\circ}}$; point ${point_P}\\in\\triangle {point_A}{point_B}{point_C}$, point ${point_Q}\\in\\triangle {point_B}{point_C}{point_D}$; point ${point_M}\\in{point_B}{point_C}$, and ${point_M}{point_Q}$ is the projection of line ${point_P}{point_Q}$ onto plane ${point_B}{point_C}{point_D}$. Given ${point_P}{point_M}={len_a}>0$, $\\angle({point_P}{point_Q},{point_B}{point_C}{point_D})={arg_beta}$, $\\angle({point_C}{point_M}{point_Q})={arg_theta}$ ($0^{{\\circ}}<{arg_theta}<90^{{\\circ}}$). Find the length of segment ${point_P}{point_Q}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_6_6({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}', '{point_Q}', '{point_M}')"}, ensure_ascii=False) + "\n")
