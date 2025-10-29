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
point_A, point_B, point_C, point_D, point_E, point_F, point_G, point_H, point_J, point_I = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math


def calculate(param_k: float) -> float:
    """计算 R² 的表达式值（R² = 2*(param_k² - param_k + 1)）"""
    return 2 * (param_k ** 2 - param_k + 1)


param_k = 1 / 2
 # cube_side = s

# result = calculate(param_k)
# print(f"R² = {result:.6f}")

# Generate random lengths
param_k = round(len_scaling_factor * float(param_k), 2)

# Calculate the result
result = calculate(param_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_18_amc8_24",
    "type": 3,
    "level": 2,
    "cn_problem": f"设正方体 {point_A}{point_B}{point_C}{point_D}{point_E}{point_F}{point_G}{point_H} 的棱长为 cube_side。在棱 $\\overline{{{point_F}{point_B}}}$ 上取点 {point_J}，使 $\\frac{{{point_F}{point_J}}}{{{point_J}{point_B}}}={param_k}:(1-{param_k})$，$0<{param_k}<1$，并在棱 $\\overline{{{point_H}{point_D}}}$ 上取点 {point_I}，使 $\\frac{{{point_H}{point_I}}}{{{point_I}{point_D}}}={param_k}:(1-{param_k})$。过四点 {point_E},{point_J},{point_C},{point_I} 作截面，得到四边形 {point_E}{point_J}{point_C}{point_I}。设 $R=\\frac{{\\operatorname{{Area}}({point_E}{point_J}{point_C}{point_I})}}{{\\operatorname{{Area}}(\\text{{立方体任一面}})}}$，求 $R^{2}$ 。",
    "en_problem": f"Let cube {point_A}{point_B}{point_C}{point_D}{point_E}{point_F}{point_G}{point_H} have edge length cube_side. On edge $\\overline{{{point_F}{point_B}}}$, take point {point_J} such that $\\frac{{{point_F}{point_J}}}{{{point_J}{point_B}}}={param_k}:(1-{param_k})$ where $0<{param_k}<1$, and on edge $\\overline{{{point_H}{point_D}}}$, take point {point_I} such that $\\frac{{{point_H}{point_I}}}{{{point_I}{point_D}}}={param_k}:(1-{param_k})$. A cross-section is made through the four points {point_E},{point_J},{point_C},{point_I}, forming quadrilateral {point_E}{point_J}{point_C}{point_I}. Let $R=\\frac{{\\operatorname{{Area}}({point_E}{point_J}{point_C}{point_I})}}{{\\operatorname{{Area}}(\\text{{cube face}})}}$, find the explicit expression for $R^{2}$.",
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
    f.write(json.dumps({json_data["id"]: f"aops_18_amc8_24({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_G}', '{point_H}', '{point_J}', '{point_I}')"}, ensure_ascii=False) + "\n")
