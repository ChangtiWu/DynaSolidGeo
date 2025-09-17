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


def calculate(len_p: float, len_q: float, len_w: float) -> float:
    """计算体积 V 的表达式值"""
    # 计算中间变量 s
    s = math.sqrt(len_p ** 2 + (len_q ** 2) / 2)

    # 计算括号内的三项和
    term1 = (len_q - len_w) ** 2
    term2 = (len_q - len_w) * (len_p + len_q - len_w)
    term3 = (len_p + len_q - len_w) ** 2
    sum_terms = term1 + term2 + term3

    # 计算分数部分
    fraction = (2 / (3 * len_q ** 2)) * sum_terms

    # 计算最终体积 V
    V = (s ** 3) * (1 - fraction)
    return V


len_p = 2.0
len_q = 8.0
len_w = 7.0
len_r = 10.0

# result = calculate(len_p, len_q, len_w)
# print(f"V = {result:.6f}")


# Generate random lengths
len_p = round(len_scaling_factor * float(len_p), 2)
len_q = round(len_scaling_factor * float(len_q), 2)
len_r = round(len_scaling_factor * float(len_r), 2)
len_w = round(len_scaling_factor * float(len_w), 2)

# Calculate the result
result = calculate(len_p, len_q, len_w)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_23_aimeII_14",
    "type": 5,
    "level": 2,
    "cn_problem": f"将正方体 {point_A}{point_B}{point_C}{point_D} 置于水平面 P，使平面 {point_A}{point_B}{point_D}{point_C} 与 P 垂直，且顶点 {point_A} 位于 P 上。设顶点 {point_B}、{point_C}、{point_D} 分别在 P 上方 {len_p}、{len_q}、{len_r} 米，其中 {len_r}={len_p}+{len_q}，{len_p}>0，{len_q}>{len_p}。容器中注水，水面与 P 平行，位于 P 上方 {len_w} 米（满足 {len_p}<{len_w}<{len_q}）。求水体积 V。",
    "en_problem": f"A cube {point_A}{point_B}{point_C}{point_D} is placed on a horizontal plane P such that the plane {point_A}{point_B}{point_D}{point_C} is perpendicular to P and vertex {point_A} lies on P. Vertices {point_B}, {point_C}, {point_D} are {len_p}, {len_q}, {len_r} metres above P, respectively, where {len_r}={len_p}+{len_q}, {len_p}>0 and {len_q}>{len_p}. The container is partially filled with water; the water surface is parallel to P at a height of {len_w} metres above P, with {len_p}<{len_w}<{len_q}. Find the water volume V .",
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
    f.write(json.dumps({json_data["id"]: f"aops_23_aimeII_14({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
