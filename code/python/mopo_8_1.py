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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_F, point_P = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math


def calculate(len_a):
    """计算len_L关于len_a的表达式"""
    return (math.sqrt(5) * len_a) / 2


# 测试示例
len_a = 1.0

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_8_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"设正方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 的棱长为 ${len_a}$，{point_E}、{point_F} 分别是棱 ${point_A}{point_D}$、${point_B1}{point_C1}$ 的中点。若点 {point_P} 为侧面正方形 ${point_A}{point_D}{point_D1}{point_A1}$ 内（含边）的动点，且存在 $x, y \\\\in \\\\mathbb{{R}}$ 使 $\\\\overrightarrow{{{point_B1}{point_P}}} = x\\\\overrightarrow{{{point_B}{point_E}}} + y\\\\overrightarrow{{{point_B}{point_F}}}$ 成立，求点 {point_P} 的轨迹长度。",
    "en_problem": f"Let cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} have edge length ${len_a}$, and {point_E}, {point_F} are midpoints of edges ${point_A}{point_D}$ and ${point_B1}{point_C1}$ respectively. If point {point_P} is a moving point within lateral face ${point_A}{point_D}{point_D1}{point_A1}$ (including boundary), and there exist $x, y \\\\in \\\\mathbb{{R}}$ such that $\\\\overrightarrow{{{point_B1}{point_P}}} = x\\\\overrightarrow{{{point_B}{point_E}}} + y\\\\overrightarrow{{{point_B}{point_F}}}$, find the trajectory length of point {point_P}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_8_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_F}', '{point_P}')"}, ensure_ascii=False) + "\n")
