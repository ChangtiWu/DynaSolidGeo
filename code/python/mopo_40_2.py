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
point_A, point_B, point_C, point_D, point_P, point_M = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_a, arg_alpha, arg_beta, len_h):
    """计算两部分结果：(i) len_L为len_a与角度差的乘积；(ii) cos(arg_theta)为len_h与平方根表达式的比值"""
    len_L = len_a * (arg_beta - arg_alpha)
    cos_value = len_h / math.sqrt(2 * len_h ** 2 + len_a ** 2)
    return cos_value


# 测试示例
len_a = 2.0
arg_alpha = math.radians(45)
arg_beta = math.radians(60)
len_h = 4.0

# print(calculate(len_a, arg_alpha, arg_beta, len_h))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, arg_alpha, arg_beta, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_40_2",
    "type": 7,
    "level": 2,
    "cn_problem": f"设正方形 {point_A}{point_B}{point_C}{point_D} 的边长为 ${len_a}$，${point_P}{point_A}$ 的长度为 ${len_h}$，平面 {point_P}{point_A}{point_B} $\\\\perp$ 平面 {point_A}{point_B}{point_C}{point_D}，平面 {point_P}{point_A}{point_D} $\\\\perp$ 平面 {point_A}{point_B}{point_C}{point_D}。点 {point_M} 在正方形 {point_A}{point_B}{point_C}{point_D} 内（包括边界），满足：\\n\\n(i) 平面 {point_P}{point_A}{point_M} $\\\\perp$ 平面 {point_P}{point_D}{point_M} 且 $\\\\angle {point_A}{point_D}{point_M} \\\\in [{arg_alpha}, {arg_beta}]$（$0 < {arg_alpha} < {arg_beta} < \\\\frac{{\\\\pi}}{{2}}$，且 $2*{arg_beta} \\\\leq \\\\pi$）。\\n\\n(ii) 是否存在 {point_M} 点，使得平面 {point_B}{point_P}{point_M} $\\\\perp$ 平面 {point_C}{point_P}{point_M}$，若存在，求二面角 ${point_A}-{point_P}{point_D}-{point_M}$ 的余弦值 。",
    "en_problem": f"Let square {point_A}{point_B}{point_C}{point_D} have side length ${len_a}$, length ${point_P}{point_A} = {len_h}$, plane {point_P}{point_A}{point_B} $\\\\perp$ plane {point_A}{point_B}{point_C}{point_D}, plane {point_P}{point_A}{point_D} $\\\\perp$ plane {point_A}{point_B}{point_C}{point_D}. Point {point_M} is inside square {point_A}{point_B}{point_C}{point_D} (including boundary), satisfying:\\n\\n(i) Plane {point_P}{point_A}{point_M} $\\\\perp$ plane {point_P}{point_D}{point_M} and $\\\\angle {point_A}{point_D}{point_M} \\\\in [{arg_alpha}, {arg_beta}]$ (where $0 < {arg_alpha} < {arg_beta} < \\\\frac{{\\\\pi}}{{2}}$ and $2*{arg_beta} \\\\leq \\\\pi$).\\n\\n(ii) Does there exist point {point_M} such that plane {point_B}{point_P}{point_M} $\\\\perp$ plane {point_C}{point_P}{point_M}$? If yes, find the cosine value of dihedral angle ${point_A}-{point_P}{point_D}-{point_M}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_40_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}', '{point_M}')"}, ensure_ascii=False) + "\n")
