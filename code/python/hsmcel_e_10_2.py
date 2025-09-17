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
point_V, point_A, point_B, point_C = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math


def calculate(len_h, arg_theta):
    """计算体积V关于len_h和arg_theta的表达式"""
    tan_half_theta = math.tan(arg_theta / 2)
    return (math.sqrt(3) / 4) * (len_h ** 3) * (3 * tan_half_theta ** 2 - 1)


# 测试示例
len_h = 2.0
arg_theta = math.pi / 2

# print(calculate(len_h, arg_theta))

# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)


# Calculate the result
result = calculate(len_h, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_10_2",
    "type": 5,
    "level": 2,
    "cn_problem": f"设 ${point_V}$-${point_A}{point_B}{point_C}$ 为正三棱锥（底面是正三角形，且三条侧棱等长）。已知棱锥的高为 ${len_h}>0$，相邻两侧面 ${point_V}{point_A}{point_B}$ 与 ${point_V}{point_B}{point_C}$ 所成的二面角为 ${arg_theta} \\in (0, \\pi)$。求该正三棱锥的体积。",
    "en_problem": f"Let ${point_V}$-${point_A}{point_B}{point_C}$ be a regular triangular pyramid (with an equilateral triangular base and three lateral edges of equal length). Given that the pyramid height is ${len_h}>0$ and the dihedral angle between two adjacent lateral faces ${point_V}{point_A}{point_B}$ and ${point_V}{point_B}{point_C}$ is ${arg_theta} \\in (0, \\pi)$. Find the volume of this regular triangular pyramid.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_10_2({mode}, {azimuth}, {elevation}, '{point_V}', '{point_A}', '{point_B}', '{point_C}')"}, ensure_ascii=False) + "\n")
