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
point_A, point_B, point_C, point_D, point_F, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_a, len_b, len_t):
    """计算表达式 3len_a + len_b + 2len_b√(len_t² + 2) 的值"""
    term1 = 3 * len_a
    term2 = len_b
    sqrt_part = math.sqrt(len_t ** 2 + 2)
    term3 = 2 * len_b * sqrt_part
    return term1 + term2 + term3


# 测试示例
len_a = 25.0
len_b = 10.0
len_t = math.sqrt(14) / 5

# print(calculate(len_a, len_b, len_t))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_t = round(len_scaling_factor * float(len_t), 2)

# Calculate the result
result = calculate(len_a, len_b, len_t)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_s2_3_1_1",
    "type": 3,
    "level": 2,
    "cn_problem": f"某坡屋顶可视为五面体，底面{point_A}{point_B}{point_C}{point_D}为平行四边形，其中{point_A}{point_B}={point_C}{point_D}={len_a}，{point_A}{point_D}={point_B}{point_C}={len_b}。两个等腰梯形（{point_A}{point_B}{point_F}{point_E}、{point_D}{point_C}{point_F}{point_E}）和两个等腰三角形（{point_A}{point_D}{point_E}、{point_B}{point_C}{point_F}）所在平面与底面{point_A}{point_B}{point_C}{point_D}的二面角正切值均为{len_t}。求该五面体的所有棱长之和。",
    "en_problem": f"A sloped roof can be viewed as a pentahedron with base {point_A}{point_B}{point_C}{point_D} as a parallelogram, where {point_A}{point_B}={point_C}{point_D}={len_a}, {point_A}{point_D}={point_B}{point_C}={len_b}. Two isosceles trapezoids ({point_A}{point_B}{point_F}{point_E}, {point_D}{point_C}{point_F}{point_E}) and two isosceles triangles ({point_A}{point_D}{point_E}, {point_B}{point_C}{point_F}) have planes that form dihedral angles with base plane {point_A}{point_B}{point_C}{point_D}, all with tangent value {len_t}. Find the sum of all edge lengths of this pentahedron.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_s2_3_1_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_F}', '{point_E}')"}, ensure_ascii=False) + "\n")
