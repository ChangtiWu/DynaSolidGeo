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
point_A, point_B, point_C, point_D, point_E, point_F, point_G, point_H, point_M = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
def calculate(len_a: float, len_b: float, len_c: float) -> float:
    """计算体积 V 的表达式值（V = (len_a·len_b·len_c)/3）"""
    return (len_a * len_b * len_c) / 3


len_a = 3.0
len_b = 1.0
len_c = 2.0

# result = calculate(len_a, len_b, len_c)
# print(f"V = {result:.6f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_18_amc10B_10",
    "type": 5,
    "level": 1,
    "cn_problem": f"在矩形平行六面体 ${point_A}{point_B}{point_C}{point_D}{point_E}{point_F}{point_G}{point_H}$ 中，设三条互相垂直的棱长分别为 ${point_A}{point_B}={len_a}>0$，${point_B}{point_C}={len_b}>0$，${point_C}{point_G}={len_c}>0$。记上底棱 $\\overline{{{point_F}{point_G}}}$ 的中点为 ${point_M}$。以平行四边形 ${point_B}{point_C}{point_H}{point_E}$ 为底、${point_M}$ 为顶，构成四棱锥 ${point_B}{point_C}{point_H}{point_E}-{point_M}$。求该四棱锥体积 $V$。",
    "en_problem": f"In rectangular parallelepiped ${point_A}{point_B}{point_C}{point_D}{point_E}{point_F}{point_G}{point_H}$, let the three mutually perpendicular edge lengths be ${point_A}{point_B}={len_a}>0$, ${point_B}{point_C}={len_b}>0$, ${point_C}{point_G}={len_c}>0$. Let ${point_M}$ be the midpoint of the upper base edge $\\overline{{{point_F}{point_G}}}$. Form pyramid ${point_B}{point_C}{point_H}{point_E}-{point_M}$ with parallelogram ${point_B}{point_C}{point_H}{point_E}$ as base and ${point_M}$ as apex. Find the volume $V$ of this pyramid.",
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
    f.write(json.dumps({json_data["id"]: f"aops_18_amc10B_10({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_G}', '{point_H}', '{point_M}')"}, ensure_ascii=False) + "\n")
