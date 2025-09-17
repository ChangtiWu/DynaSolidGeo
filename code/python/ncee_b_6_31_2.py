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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_a: float, len_h: float) -> float:
    """计算 sinθ 的表达式值"""
    numerator = math.sqrt(2) * len_a * len_h
    denominator = len_a**2 + 2 * len_h**2
    return numerator / denominator


len_a = 2.0
len_h = math.sqrt(14)

# result = calculate(len_a, len_h)
# print(f"当 len_a={len_a}, len_h={len_h} 时，sinθ = {result:.4f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h)

# Define LaTeX expressions separately to avoid backslashes in f-strings
overrightarrow_AA1 = f"\\overrightarrow{{{point_A}{point_A1}}}"
tfrac_len_a_2 = f"\\tfrac{{{len_a}}}{{2}}"
tfrac_len_a2_2 = f"\\tfrac{{{len_a}^{{2}}}}{{2}}"
sqrt_expr = f"\\sqrt{{{len_h}^{{2}}+{tfrac_len_a2_2}}}"
sin_theta = "\\sin\\theta"

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_31_2",
    "type": 2,
    "level": 3,
    "cn_problem": f"设底面直角等腰三角形 {point_A}{point_B}{point_C} 满足 ∠{point_B}{point_A}{point_C} = 90° ，并令\n  {point_A}{point_B} = {point_A}{point_C} = {len_a} (>0)；\n- 侧棱向量固定为\n  {overrightarrow_AA1} = ({tfrac_len_a_2}, {tfrac_len_a_2}, {len_h}) ，即上顶点 {point_A1} 的射影恰为 {point_B}{point_C} 的中点，侧棱长度\n  ℓ = {sqrt_expr}；\n- 其余侧棱 {point_B}{point_B1}, {point_C}{point_C1} 与 {point_A}{point_A1} 平行且等长；\n- 记 {point_D} 为 {point_B1}{point_C1} 的中点。\n\n设 θ 是直线 {point_A1}{point_B} 与侧面 {point_B}{point_B1}{point_C1}{point_C} 所成锐角。求\n  {sin_theta} 。",
    "en_problem": f"Base right‑isosceles triangle {point_A}{point_B}{point_C} with ∠{point_B}{point_A}{point_C}=90° and\n  {point_A}{point_B} = {point_A}{point_C} = {len_a} (>0);\n- Lateral vector fixed as\n  {overrightarrow_AA1} = ({tfrac_len_a_2},{tfrac_len_a_2},{len_h}) so the foot of {point_A1} is the midpoint of {point_B}{point_C}; lateral length\n  ℓ = {sqrt_expr};\n- Edges {point_B}{point_B1}, {point_C}{point_C1} are parallel and equal to {point_A}{point_A1};\n- Let {point_D} be the midpoint of {point_B1}{point_C1}.\n\nLet θ be the acute angle between line {point_A1}{point_B} and face {point_B}{point_B1}{point_C1}{point_C}. Express\n  {sin_theta}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_31_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}')"}, ensure_ascii=False) + "\n")
