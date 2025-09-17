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
point_O, point_A, point_B, point_C, point_E, point_F, point_A1, point_B1, point_C1 = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math


def calculate(len_k: float) -> float:
    """计算 tan(arg_theta) 的值（公式：tan(arg_theta) = √(1 + 1/(2len_k - 1)²)）"""
    denominator = 2 * len_k - 1
    if denominator == 0:
        raise ValueError("2len_k - 1 不能为0，否则分母为0")
    return math.sqrt(1 + 1 / (denominator ** 2))


len_t = 2.0
len_k = 3 / 4

# result = calculate(len_k)
# print(f"tan_arg_theta = {result:.6f}")

# Generate random lengths
len_t = round(len_scaling_factor * float(len_t), 2)
len_k = round(len_scaling_factor * float(len_k), 2)

# Calculate the result
result = calculate(len_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_6_2",
    "type": 2,
    "level": 3,
    "cn_problem": f"设三条侧棱两两互相垂直、且长度均为 ${len_t}>0$ 的直三棱锥 {point_O}-{point_A}{point_B}{point_C}，满足 ${point_O}{point_A} \\perp {point_O}{point_B}$、${point_O}{point_B} \\perp {point_O}{point_C}$、${point_O}{point_C} \\perp {point_O}{point_A}$，且 $|{point_O}{point_A}|=|{point_O}{point_B}|=|{point_O}{point_C}|={len_t}$。记 {point_E}、{point_F} 分别为棱 ${point_A}{point_B}$、${point_A}{point_C}$ 的中点；取比例参数 ${len_k} \\in (\\frac{1}{2},1)$，在棱 ${point_O}{point_A}$ 上取点 ${point_A1}$，使 ${point_O}{point_A1}={len_k}{len_t}$。过点 ${point_A1}$ 与直线 ${point_E}{point_F}$ 作平面，它与直线 ${point_O}{point_B}$、${point_O}{point_C}$ 的延长线分别交于 ${point_B1}$、${point_C1}$。求二面角 ${point_O}$—${point_A1}{point_B1}$—${point_C1}$ 的平面角正切值 。",
    "en_problem": f"Let the right triangular pyramid {point_O}-{point_A}{point_B}{point_C} have three lateral edges that are mutually perpendicular with equal length ${len_t}>0$, satisfying ${point_O}{point_A} \\perp {point_O}{point_B}$, ${point_O}{point_B} \\perp {point_O}{point_C}$, ${point_O}{point_C} \\perp {point_O}{point_A}$, and $|{point_O}{point_A}|=|{point_O}{point_B}|=|{point_O}{point_C}|={len_t}$. Let {point_E} and {point_F} be the midpoints of edges ${point_A}{point_B}$ and ${point_A}{point_C}$ respectively; take the ratio parameter ${len_k} \\in (\\frac{1}{2},1)$, and take point ${point_A1}$ on edge ${point_O}{point_A}$ such that ${point_O}{point_A1}={len_k}{len_t}$. The plane passing through point ${point_A1}$ and line ${point_E}{point_F}$ intersects the extensions of lines ${point_O}{point_B}$ and ${point_O}{point_C}$ at ${point_B1}$ and ${point_C1}$ respectively. Find the tangent of the planar angle of the dihedral angle ${point_O}$—${point_A1}{point_B1}$—${point_C1}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_6_2({mode}, {azimuth}, {elevation}, '{point_O}', '{point_A}', '{point_B}', '{point_C}', '{point_E}', '{point_F}', '{point_A1}', '{point_B1}', '{point_C1}')"}, ensure_ascii=False) + "\n")
