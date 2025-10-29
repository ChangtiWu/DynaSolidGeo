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
point_P, point_A1, point_B1, point_C1, point_D1, point_A, point_B, point_C, point_D, point_O1, point_O = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
def calculate(len_a, len_h1, param_k):
    """计算体积V = len_a²·len_h1·(param_k + 1/3)"""
    return (len_a ** 2) * len_h1 * (param_k + 1 / 3)


# 测试示例
len_a = 6.0
len_h1 = 2.0
param_k = 4.0
len_h2 = 8.0

# print(calculate(len_a, len_h1, param_k))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h1 = round(len_scaling_factor * float(len_h1), 2)
len_h2 = round(len_scaling_factor * float(len_h2), 2)

# Calculate the result
result = calculate(len_a, len_h1, param_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_17_1",
    "type": 5,
    "level": 2,
    "cn_problem": f"如图，需要设计一个仓库，它由上下两部分组成：上部分的形状是正四棱锥 {point_P}-{point_A1}{point_B1}{point_C1}{point_D1}，下部分的形状是正四棱柱 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}。底面 {point_A}{point_B}{point_C}{point_D} 是边长为 {len_a}>0 的正方形，正四棱锥的高 {point_P}{point_O1}={len_h1}>0，正四棱柱的高 {point_O}{point_O1}={len_h2}，且 {len_h2}={param_k}·{len_h1}（其中 {param_k}>0 是给定常数）。求仓库总体积。",
    "en_problem": f"As shown, a warehouse needs to be designed consisting of two parts: the upper part is a regular quadrilateral pyramid {point_P}-{point_A1}{point_B1}{point_C1}{point_D1}, and the lower part is a regular quadrilateral prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}. The base {point_A}{point_B}{point_C}{point_D} is a square with side length {len_a}>0, the height of the pyramid {point_P}{point_O1}={len_h1}>0, the height of the prism {point_O}{point_O1}={len_h2}, and {len_h2}={param_k}·{len_h1} (where {param_k}>0 is a given constant). Find the total volume of the warehouse.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_17_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O1}', '{point_O}')"}, ensure_ascii=False) + "\n")
