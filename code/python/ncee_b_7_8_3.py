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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_M, point_N = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
def calculate(len_a: float) -> float:
    """计算点C到平面AMC₁的距离（表达式为 (2/3)*len_a）"""
    return (2 / 3) * len_a


len_a = 2.0

# result = calculate(len_a)
# print(f"点C到平面AMC₁的距离 = {result:.4f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_8_3",
    "type": 3,
    "level": 2,
    "cn_problem": f"设三棱台 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 满足\n- 底面 {point_A}{point_B}{point_C} 为直角等腰三角形，{point_A}{point_B} = {point_A}{point_C} = {len_a} (>0)，且 \\angle {point_B}{point_A}{point_C} = 90°；\n- 侧棱 {point_A}{point_A1} ⟂ 平面 {point_A}{point_B}{point_C} 且 {point_A}{point_A1} = {len_a}；\n- 上底点 {point_C1} 使 {point_A1}{point_C1} = \\tfrac{{1}}{{2}}{len_a}，并保持 {point_A1}{point_C1} ∥ {point_A}{point_C}；\n- {point_M} 为 {point_B}{point_C} 中点，{point_N} 为 {point_A}{point_B} 中点。\n求点 {point_C} 到平面 {point_A}{point_M}{point_C1} 的距离。",
    "en_problem": f"In the truncated triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, let the base {point_A}{point_B}{point_C} be a right‑isosceles triangle with {point_A}{point_B} = {point_A}{point_C} = {len_a} (>0) and \\angle {point_B}{point_A}{point_C} = 90°. The lateral edge {point_A}{point_A1} is perpendicular to the base plane and {point_A}{point_A1} = {len_a}. Point {point_C1} is chosen on the top face such that {point_A1}{point_C1} = \\tfrac{{1}}{{2}}{len_a} and {point_A1}{point_C1} ∥ {point_A}{point_C}. Let {point_M} be the midpoint of {point_B}{point_C} and {point_N} the midpoint of {point_A}{point_B}. Find the distance from point {point_C} to plane {point_A}{point_M}{point_C1}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_8_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
