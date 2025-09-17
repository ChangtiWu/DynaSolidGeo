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
point_A, point_B, point_C, point_D, point_E, point_F, point_P = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate():
    """计算固定值f（结果为2√5/5）"""
    return (2 * math.sqrt(5)) / 5


# 测试示例
len_a = 2.0

# print(calculate())

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_42_2",
    "type": 7,
    "level": 2,
    "cn_problem": f"四边形 {point_A}{point_B}{point_C}{point_D} 与 {point_B}{point_D}{point_E}{point_F} 均为菱形，$\\\\angle {point_D}{point_A}{point_B} = \\\\angle {point_D}{point_B}{point_F} = 60°$，菱形边长为 ${len_a}$（${len_a} > 0$）。点 {point_P} 为线段 ${point_D}{point_E}$ 上的动点，求 {point_F}{point_P} 与平面 {point_A}{point_B}{point_F} 所成角正弦值的最大值 $f$。",
    "en_problem": f"Quadrilaterals {point_A}{point_B}{point_C}{point_D} and {point_B}{point_D}{point_E}{point_F} are both rhombuses, with $\\\\angle {point_D}{point_A}{point_B} = \\\\angle {point_D}{point_B}{point_F} = 60°$ and rhombus edge length ${len_a}$ (${len_a} > 0$). Point {point_P} is a moving point on segment ${point_D}{point_E}$. Find the maximum value $f$ of the sine of the angle between {point_F}{point_P} and plane {point_A}{point_B}{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_42_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_P}')"}, ensure_ascii=False) + "\n")
