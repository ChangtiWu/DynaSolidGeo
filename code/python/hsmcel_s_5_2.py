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
point_A, point_B, point_C, point_D, point_P, point_E, point_F = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_a: float, len_p: float) -> float:
    """计算长度 len_d 的表达式值（公式：len_d = (len_a·len_p)/√(8len_p² + 9len_a²)）"""
    numerator = len_a * len_p
    denominator = math.sqrt(8 * (len_p ** 2) + 9 * (len_a ** 2))
    return numerator / denominator


len_a = 4.0
len_p = 2.0

# result = calculate(len_a, len_p)
# print(f"len_d = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_p = round(len_scaling_factor * float(len_p), 2)

# Calculate the result
result = calculate(len_a, len_p)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_s_5_2",
    "type": 3,
    "level": 3,
    "cn_problem": f"设边长参数 ${len_a}>0$，使平面四边形 {point_A}{point_B}{point_C}{point_D} 为边长为 ${len_a}$ 的正方形；长度参数 ${len_p}>0$，满足 ${point_P}{point_C}={len_p}$。记 {point_E}、{point_F} 分别为棱 ${point_A}{point_B}$、${point_A}{point_D}$ 的中点；点 {point_P} 满足 ${point_P}{point_E}\\perp$(平面 {point_A}{point_B}{point_C}{point_D})。求点 {point_B} 到平面 ${point_P}{point_E}{point_F}$ 的距离。",
    "en_problem": f"Let the side length parameter ${len_a}>0$ such that planar quadrilateral {point_A}{point_B}{point_C}{point_D} is a square with side length ${len_a}$; let the length parameter ${len_p}>0$ satisfy ${point_P}{point_C}={len_p}$. Let {point_E} and {point_F} be the midpoints of edges ${point_A}{point_B}$ and ${point_A}{point_D}$ respectively; point {point_P} satisfies ${point_P}{point_E}\\perp$(plane {point_A}{point_B}{point_C}{point_D}). Find the distance from point {point_B} to plane ${point_P}{point_E}{point_F}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_s_5_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
