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
point_A, point_B, point_C, point_P, point_D, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_s: float, len_h: float) -> float:
    """计算长度 len_d 的表达式值（公式：len_d = (len_h·len_s)/(4√(len_h² + len_s²/16))）"""
    numerator = len_h * len_s
    denominator = 4 * math.sqrt(len_h ** 2 + (len_s ** 2) / 16)
    return numerator / denominator


len_s = 4 * math.sqrt(2)
len_h = 2.0

# result = calculate(len_s, len_h)
# print(f"len_d = {result:.6f}")
# Generate random lengths
len_s = round(len_scaling_factor * float(len_s), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_s, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_5_3",
    "type": 3,
    "level": 2,
    "cn_problem": f"设 $\\triangle {point_A}{point_B}{point_C}$ 为边长 ${len_s}>0$ 的正三角形，点 {point_P} 在其外侧，满足 ${point_P}{point_A} \\perp$ 平面 {point_A}{point_B}{point_C}，${point_P}{point_A}={len_h}>0$。设 {point_D} 为 ${point_B}{point_C}$ 的中点，{point_E} 为 ${point_A}{point_C}$ 的中点。求异面直线 ${point_A}{point_D}$ 与 ${point_P}{point_E}$ 之间的距离。",
    "en_problem": f"Let $\\triangle {point_A}{point_B}{point_C}$ be an equilateral triangle with side length ${len_s}>0$, and point {point_P} be outside the triangle such that ${point_P}{point_A} \\perp$ plane {point_A}{point_B}{point_C} and ${point_P}{point_A}={len_h}>0$. Let {point_D} be the midpoint of ${point_B}{point_C}$ and {point_E} be the midpoint of ${point_A}{point_C}$. Find the distance between the skew lines ${point_A}{point_D}$ and ${point_P}{point_E}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_5_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_P}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
