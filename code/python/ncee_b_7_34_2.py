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
point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(arg_alpha):
    """计算cos(theta)的值（公式：-2*cos(arg_alpha)/√(sin²(arg_alpha)+4)）"""
    numerator = -2 * math.cos(arg_alpha)
    denominator = math.sqrt(math.sin(arg_alpha) ** 2 + 4)
    return numerator / denominator


# 测试示例
arg_beta = math.pi / 2
arg_alpha = math.pi / 3

# print(calculate(arg_alpha))


# Calculate the result
result = calculate(arg_alpha)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_34_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在以{point_A}、{point_B}、{point_C}、{point_D}、{point_E}、{point_F}为顶点的五面体中，四边形{point_A}{point_B}{point_E}{point_F}为正方形，{point_A}{point_F}=2*{point_F}{point_D}，∠{point_A}{point_F}{point_D}={arg_beta}，且二面角{point_D}-{point_A}{point_F}-{point_E}与二面角{point_C}-{point_B}{point_E}-{point_F}都是{arg_alpha}。求二面角{point_E}-{point_B}{point_C}-{point_A}的余弦值。",
    "en_problem": f"In pentahedron with vertices {point_A}, {point_B}, {point_C}, {point_D}, {point_E}, {point_F}, quadrilateral {point_A}{point_B}{point_E}{point_F} is a square, {point_A}{point_F}=2*{point_F}{point_D}, ∠{point_A}{point_F}{point_D}={arg_beta}, and both dihedral angles {point_D}-{point_A}{point_F}-{point_E} and {point_C}-{point_B}{point_E}-{point_F} are {arg_alpha}. Find the cosine of dihedral angle {point_E}-{point_B}{point_C}-{point_A}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_34_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
