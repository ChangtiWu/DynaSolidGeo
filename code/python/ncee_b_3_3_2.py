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
point_A, point_B, point_C, point_A1, point_B1, point_C1 = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
def calculate(len_h):
    """
    计算 len_h 除以 2 的结果

    参数:
    len_h (float): 输入长度值

    返回:
    float: len_h / 2 的计算结果
    """
    return len_h / 2

len_h=2
# result1 = calculate(len_h)
# print(result1)  # 输出: 5.0
# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_3_3_2",
    "type": 3,
    "level": 1,
    "cn_problem": f"如图，在三棱柱 {point_A}{point_B}{point_C}−{point_A1}{point_B1}{point_C1} 中，已知 {point_A1}{point_C1} ⟂ 平面 {point_A}{point_B}{point_C}，且 ∠{point_A}{point_C}{point_B} = 90°。\n设 {point_A}{point_B} = {point_A1}{point_B}，{point_A}{point_A1} = {len_h}（{len_h}>0）。\n求四棱锥 {point_A}−{point_B}{point_B1}{point_C1}{point_C} 的高。",
    "en_problem": f"In the triangular prism {point_A}{point_B}{point_C}−{point_A1}{point_B1}{point_C1}, assume {point_A1}{point_C1} ⟂ plane {point_A}{point_B}{point_C} and ∠{point_A}{point_C}{point_B} = 90°.\nGiven {point_A}{point_B} = {point_A1}{point_B} and {point_A}{point_A1} = {len_h} (>0), find the height of the quadrilateral pyramid {point_A}−{point_B}{point_B1}{point_C1}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_3_3_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}')"}, ensure_ascii=False) + "\n")
