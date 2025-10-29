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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_P = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math


def calculate(len_a):
    """计算区间[len_d_min, len_d_max]的左右端点（均为关于len_a的表达式）"""

    len_d_max = (3 * len_a) / 2
    return len_d_max


# 测试示例
len_a = 4.0

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_31_1_2",
    "type": 7,
    "level": 2,
    "cn_problem": f"在棱长为 ${len_a}$ 的正方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 中，{point_E} 为棱 ${point_B}{point_C}$ 的中点，{point_P} 是底面 {point_A}{point_B}{point_C}{point_D} 内的一点（包含边界），且 ${point_B1}{point_P} \\\\perp {point_D1}{point_E}$，求线段 ${point_B1}{point_P}$ 长度的最大值。",
    "en_problem": f"In a cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} with edge length ${len_a}$, {point_E} is the midpoint of edge ${point_B}{point_C}$, and {point_P} is a point in base {point_A}{point_B}{point_C}{point_D} (including boundary) such that ${point_B1}{point_P} \\\\perp {point_D1}{point_E}$. Find the maxmum of the length of segment ${point_B1}{point_P}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_31_1_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_P}')"}, ensure_ascii=False) + "\n")
