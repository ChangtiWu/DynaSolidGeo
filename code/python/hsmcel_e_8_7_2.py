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
import math


def calculate(len_s):
    """计算len_d关于len_s的表达式"""
    return (math.sqrt(15) / 5) * len_s


# 测试示例
len_s = 1

# print(calculate(len_s))

# Generate random lengths
len_s = round(len_scaling_factor * float(len_s), 2)

# Calculate the result
result = calculate(len_s)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_8_7_2",
    "type": 3,
    "level": 3,
    "cn_problem": f"在斜三棱柱 ${point_A}{point_B}{point_C}$-${point_A1}{point_B1}{point_C1}$ 中，底面 $\\triangle {point_A}{point_B}{point_C}$ 为边长为 ${len_s}>0$ 的正三角形。侧面 ${point_A}{point_A1}{point_C1}{point_C}$ 构成一条边长同为 ${len_s}$、且面积为 $\\frac{{\\sqrt{3}}}{{2}}{len_s}^2$ 的菱形（其锐角 $=60°$）。又已知侧面 ${point_A}{point_B}{point_B1}{point_A1}$ 与侧面 ${point_A}{point_A1}{point_C1}{point_C}$ 互相垂直，并满足 ${point_A}{point_B}={point_A}{point_C}={len_s}$。求直线 ${point_A1}{point_B1}$ 到平面 ${point_A}{point_B}{point_C}$ 的距离。",
    "en_problem": f"In the oblique triangular prism ${point_A}{point_B}{point_C}$-${point_A1}{point_B1}{point_C1}$, the base $\\triangle {point_A}{point_B}{point_C}$ is an equilateral triangle with side length ${len_s}>0$. The lateral face ${point_A}{point_A1}{point_C1}{point_C}$ forms a rhombus with side length ${len_s}$ and area $\\frac{{\\sqrt{3}}}{{2}}{len_s}^2$ (with acute angle $=60°$). It is also known that the lateral face ${point_A}{point_B}{point_B1}{point_A1}$ is perpendicular to the lateral face ${point_A}{point_A1}{point_C1}{point_C}$, and ${point_A}{point_B}={point_A}{point_C}={len_s}$. Find the distance from line ${point_A1}{point_B1}$ to plane ${point_A}{point_B}{point_C}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_8_7_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}')"}, ensure_ascii=False) + "\n")
