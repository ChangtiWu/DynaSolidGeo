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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_P, point_F, point_Q = random.sample(string.ascii_uppercase, 12)

# Add result calculation code
import math


def calculate(len_a, len_b):
    """计算len_d_min关于len_a和len_b的表达式（结果为len_a*√6 - len_b）"""
    return len_a * math.sqrt(6) - len_b


# 测试示例
len_a = 4.0
len_b = 1.0

# print(calculate(len_a, len_b))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_26_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"正方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 的棱长为 ${len_a}$，{point_E} 是 ${point_D}{point_D1}$ 上的动点，{point_P}、{point_F} 是上、下两底面上的动点，{point_Q} 是 ${point_E}{point_F}$ 中点，${point_E}{point_F} = 2*{len_b}$，求 ${point_P}{point_B1} + {point_P}{point_Q}$ 的最小值。",
    "en_problem": f"In a cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} with edge length ${len_a}$, {point_E} is a moving point on ${point_D}{point_D1}$, {point_P} and {point_F} are moving points on upper and lower bases respectively, {point_Q} is the midpoint of ${point_E}{point_F}$, and ${point_E}{point_F} = 2*{len_b}$. Find the minimum value of ${point_P}{point_B1} + {point_P}{point_Q}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_26_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_P}', '{point_F}', '{point_Q}')"}, ensure_ascii=False) + "\n")
