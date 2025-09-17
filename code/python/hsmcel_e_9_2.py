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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M, point_N, point_P = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math


def calculate(len_a):
    """计算面积area_S_H关于len_a的表达式"""
    return (3 * math.sqrt(3) / 4) * (len_a ** 2)


# 测试示例
len_a = 1.0

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_9_2",
    "type": 4,
    "level": 2,
    "cn_problem": f"在棱长为 ${len_a}>0$ 的正方体 ${point_A}{point_B}{point_C}{point_D}$-${point_A1}{point_B1}{point_C1}{point_D1}$ 中，令 ${point_M}$、${point_N}$、${point_P}$ 分别为棱 ${point_B1}{point_C1}$、${point_C1}{point_D1}$、${point_D1}{point_D}$ 的中点。设动平面 $\\pi$ 由三点 ${point_M}$、${point_N}$、${point_P}$ 唯一确定，并与正方体表面所截得的多边形记为 $\\mathcal{{H}}$。已知当 ${len_a}=1$ 时，$\\mathcal{{H}}$ 是边长 $\\frac{{\\sqrt{{2}}}}{{2}}$ 的正六边形。求 $\\mathcal{{H}}$ 的面积。",
    "en_problem": f"In a cube ${point_A}{point_B}{point_C}{point_D}$-${point_A1}{point_B1}{point_C1}{point_D1}$ with edge length ${len_a}>0$, let ${point_M}$, ${point_N}$, ${point_P}$ be the midpoints of edges ${point_B1}{point_C1}$, ${point_C1}{point_D1}$, ${point_D1}{point_D}$ respectively. Let the movable plane $\\pi$ be uniquely determined by the three points ${point_M}$, ${point_N}$, ${point_P}$, and let the polygon formed by the intersection of $\\pi$ with the cube surface be denoted as $\\mathcal{{H}}$. It is known that when ${len_a}=1$, $\\mathcal{{H}}$ is a regular hexagon with side length $\\frac{{\\sqrt{{2}}}}{{2}}$. Find the area of $\\mathcal{{H}}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_9_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_M}', '{point_N}', '{point_P}')"}, ensure_ascii=False) + "\n")
