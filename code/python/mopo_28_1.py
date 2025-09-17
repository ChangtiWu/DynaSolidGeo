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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_P = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_h):
    """计算len_d_min关于len_h的表达式（结果为len_h乘以√7）"""
    return len_h * math.sqrt(7)


# 测试示例
len_h = 1.0
len_a = math.sqrt(3)
# print(calculate(len_h))

# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_28_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"在直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，侧棱 ${point_A}{point_A1} = {len_h}$，底面 $\\\\triangle {point_A}{point_B}{point_C}$ 满足 ${point_A}{point_B} = {point_B}{point_C} = {len_a}$，$\\\\cos\\\\angle {point_A}{point_B}{point_C} = //theta$，且满足 $\\\\sqrt{{{len_h}^2 + {len_a}^2}} = {len_a}\\\\sqrt{{2(1 - //theta)}}$。动点 {point_P} 在线段 ${point_A1}{point_B}$ 上运动，求 ${point_A}{point_P} + {point_P}{point_C1}$ 的最小值。",
    "en_problem": f"In right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} with lateral edge ${point_A}{point_A1} = {len_h}$, base $\\\\triangle {point_A}{point_B}{point_C}$ satisfies ${point_A}{point_B} = {point_B}{point_C} = {len_a}$ and $\\\\cos\\\\angle {point_A}{point_B}{point_C} = //theta$, with condition $\\\\sqrt{{{len_h}^2 + {len_a}^2}} = {len_a}\\\\sqrt{{2(1 - //theta)}}$. Moving point {point_P} moves on segment ${point_A1}{point_B}$. Find the minimum value of ${point_A}{point_P} + {point_P}{point_C1}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_28_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_P}')"}, ensure_ascii=False) + "\n")
