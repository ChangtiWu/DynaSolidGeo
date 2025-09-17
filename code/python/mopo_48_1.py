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
point_P, point_A, point_B, point_C, point_Q = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate():
    """计算π/2的值"""
    return math.pi / 2


# 测试示例
len_a = 2.0

# print(calculate())

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_48_1",
    "type": 7,
    "level": 1,
    "cn_problem": f"设正三棱锥 {point_P}-{point_A}{point_B}{point_C} 和正三棱锥 {point_Q}-{point_A}{point_B}{point_C} 的底面 {point_A}{point_B}{point_C} 为正三角形（边长为 ${len_a}$，${len_a} > 0$），{point_P} 和 {point_Q} 位于底面 {point_A}{point_B}{point_C} 的异侧，且所有顶点共外接球。求 $\\\\angle {point_P}{point_B}{point_Q}$ 的值。",
    "en_problem": f"Let regular triangular pyramids {point_P}-{point_A}{point_B}{point_C} and {point_Q}-{point_A}{point_B}{point_C} have base {point_A}{point_B}{point_C} as an equilateral triangle (with side length ${len_a}$, ${len_a} > 0$). {point_P} and {point_Q} are located on opposite sides of base {point_A}{point_B}{point_C}, and all vertices lie on the same circumsphere. Find the value of $\\\\angle {point_P}{point_B}{point_Q}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_48_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_Q}')"}, ensure_ascii=False) + "\n")
