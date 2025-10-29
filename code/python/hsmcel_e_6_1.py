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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_F, point_G = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math


def calculate() -> tuple[float, float]:
    """返回常数 len_lambda 和 arg_theta 的值（len_lambda=1/4，arg_theta=π/2）"""
    arg_theta = math.pi / 2
    return arg_theta

len_a = 10
len_lambda = 1 / 4

# arg_theta = calculate()
# print(f"len_lambda = {len_lambda:.6f}, arg_theta = {arg_theta:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_lambda = round(len_scaling_factor * float(len_lambda), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_6_1",
    "type": 2,
    "level": 2,
    "cn_problem": f"设正方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 的棱长为 ${len_a}>0$。记 {point_E}、{point_F} 分别为棱 ${point_A}{point_A1}$、${point_B}{point_B1}$ 的中点；点 {point_G} 位于棱 ${point_B}{point_C}$ 上，满足 ${point_B}{point_G}={len_lambda}{len_a}$（$0<{len_lambda}<1$）。已知 ${point_D1}{point_F} \\perp {point_F}{point_G}$。求：(1) 参数 ${len_lambda}$ 的值；(2) 异面直线 ${point_C1}{point_F}$ 与 ${point_E}{point_G}$ 所成的角。",
    "en_problem": f"Let cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} have edge length ${len_a}>0$. Let {point_E} and {point_F} be the midpoints of edges ${point_A}{point_A1}$ and ${point_B}{point_B1}$ respectively; point {point_G} lies on edge ${point_B}{point_C}$ satisfying ${point_B}{point_G}={len_lambda}{len_a}$ where $0<{len_lambda}<1$. Given that ${point_D1}{point_F} \\perp {point_F}{point_G}$. Find: (1) the value of parameter ${len_lambda}$; (2) the angle between skew lines ${point_C1}{point_F}$ and ${point_E}{point_G}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_6_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_F}', '{point_G}')"}, ensure_ascii=False) + "\n")
