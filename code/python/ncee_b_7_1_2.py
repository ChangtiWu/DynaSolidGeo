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
point_A, point_B, point_C, point_D, point_E, point_P, point_F = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(param_k: float) -> float:
    """计算 sinθ 的表达式值"""
    numerator = 9 * (param_k ** 4) - 20 * (param_k ** 2) - 64
    denominator = 4 * (3 * (param_k ** 4) - 14 * (param_k ** 2) + 11)
    fraction = numerator / denominator
    return math.sqrt(fraction)


len_c = 8
len_d = 5 * math.sqrt(3)
len_e = 3 * math.sqrt(3)
param_k = 4 * math.sqrt(3) / 3

# result = calculate(param_k)
# print(f"当 param_k={param_k} 时，sinθ = {result:.6f}")
# Generate random lengths
len_c = round(len_scaling_factor * float(len_c), 2)
len_d = round(len_scaling_factor * float(len_d), 2)
len_e = round(len_scaling_factor * float(len_e), 2)

# Calculate the result
result = calculate(param_k)

# Define LaTeX expressions separately to avoid backslashes in f-strings
parallel_symbol = "\\parallel"
perp_symbol = "\\perp"
dfrac_expr = f"\\dfrac{{{point_P}{point_C}}}{{{point_C}{point_D}}}"
sin_theta = "\\sin\\theta"
text_plane = "\\text{plane}"

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_1_2",
    "type": 2,
    "level": 3,
    "cn_problem": f"设 \\(四边形 {point_A}{point_B}{point_C}{point_D}\\) 满足 {point_A}{point_B} = {point_B}{point_C} = {len_c} (>0)，{point_A}{point_D} = {len_d} (>0)，且 \\({point_B}{point_C} {parallel_symbol} {point_A}{point_D},\\; {point_A}{point_B} {perp_symbol} {point_A}{point_D}\\)。\n- 点 {point_E} 在 \\({point_A}{point_D}\\) 上，取 \\({point_P}{point_E} = {point_D}{point_E} = {len_e}\\) 且 \\({point_P}{point_E} {perp_symbol} {point_A}{point_D}\\)。\n- 过 {point_A} 作高 \\({point_A}{point_A}1 {perp_symbol} \\!\\,{text_plane}\\;{point_P}{point_A}{point_D}\\)，已知 \\({point_A}{point_B} {perp_symbol}\\!\\,{text_plane}\\;{point_P}{point_A}{point_D}\\)。\n- 记 \\(k = {param_k} = {dfrac_expr} > 2\\)。\n> （2）设 \\(\\theta\\) 为平面 {point_P}{point_C}{point_D} 与平面 {point_P}{point_B}{point_F} 的锐二面角，求\n> \\({sin_theta}\\) 。",
    "en_problem": f"In quadrilateral {point_A}{point_B}{point_C}{point_D} let {point_A}{point_B} ⟂ {point_A}{point_D} with {point_A}{point_B} = {point_B}{point_C} = {len_c} (>0) and {point_A}{point_D} = {len_d} (>0) while {point_B}{point_C} ∥ {point_A}{point_D}.\n- Choose {point_E} on {point_A}{point_D} so that {point_P}{point_E} = {point_D}{point_E} = {len_e} (>0) and {point_P}{point_E} ⟂ {point_A}{point_D}.\n- Fold △{point_A}{point_E}{point_F} about {point_E}{point_F} to △{point_P}{point_E}{point_F} making {point_P}{point_C} = k·{point_C}{point_D} with k = {param_k} (>2); here {point_C}{point_D} = {len_c}.\n> (2) Let θ be the acute dihedral angle between planes {point_P}{point_C}{point_D} and {point_P}{point_B}{point_F}. Find \\(\\sinθ\\).",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_1_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_P}', '{point_F}')"}, ensure_ascii=False) + "\n")
