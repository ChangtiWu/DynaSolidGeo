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
point_A, point_B, point_C, point_D, point_E, point_P, point_Q = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_m, len_h):
    """
    计算二面角条件下的 λ 值

    参数:
    len_m (float): AD 的半长（即 AD/2）
    len_h (float): CE 的长度

    返回:
    float: λ 的值
    """
    return (2 * math.sqrt(3) * len_h) / (3 * len_m)


# 题干给定的数值
len_m = 2.0      # AD/2
len_h = 1.0      # CE

# 验证输出
# lambda_value = calculate(len_m, len_h)
# print(f"λ = {lambda_value:.6f}")

# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_m, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "zht_11_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在梯形 {point_A}{point_B}{point_C}{point_D} 中，{point_A}{point_D} ∥ {point_B}{point_C}，{point_E} 为 {point_A}{point_D} 中点（故 {point_A}{point_E} = {point_D}{point_E} = {len_m}，{point_A}{point_D} = 2*{len_m}），{point_B}{point_C} = {len_m}/2，{point_C}{point_E} ⊥ {point_A}{point_D} 且 {point_C}{point_E} = {len_h}，{point_C}{point_D} = √({len_m}^2 + {len_h}^2)。将 △{point_D}{point_E}{point_C} 沿 {point_C}{point_E} 翻折至 △{point_P}{point_E}{point_C}，使得 ∠{point_P}{point_E}{point_A} = π/3（此时 △{point_P}{point_E}{point_A} 为正三角形）。设 {point_Q} 为线段 {point_P}{point_A} 上一点，满足 {point_A}{point_Q} = λ{point_A}{point_P}，若二面角 {point_Q}-{point_B}{point_C}-{point_A} 的大小为 π/4，求实数 λ 的值。",
    "en_problem": f"In trapezoid {point_A}{point_B}{point_C}{point_D}, {point_A}{point_D} ∥ {point_B}{point_C}, {point_E} is the midpoint of {point_A}{point_D} (so {point_A}{point_E} = {point_D}{point_E} = {len_m}, {point_A}{point_D} = 2*{len_m}), {point_B}{point_C} = {len_m}/2, {point_C}{point_E} ⊥ {point_A}{point_D} and {point_C}{point_E} = {len_h}, {point_C}{point_D} = √({len_m}^2 + {len_h}^2). Fold △{point_D}{point_E}{point_C} along {point_C}{point_E} to △{point_P}{point_E}{point_C}, so that ∠{point_P}{point_E}{point_A} = π/3 (at this time △{point_P}{point_E}{point_A} is an equilateral triangle). Let {point_Q} be a point on line segment {point_P}{point_A}, satisfying {point_A}{point_Q} = λ{point_A}{point_P}, if the dihedral angle {point_Q}-{point_B}{point_C}-{point_A} is π/4, find the value of real number λ.",
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
    f.write(json.dumps({json_data["id"]: f"zht_11_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_P}', '{point_Q}')"}, ensure_ascii=False) + "\n")
