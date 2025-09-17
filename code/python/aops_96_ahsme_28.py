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
point_D, point_A, point_B, point_C = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math

def calculate(len_a: float, len_b: float, len_c: float) -> float:
    """计算高度 len_h 的表达式值（公式：len_h = (len_a·len_b·len_c) / √(len_b²len_c² + len_a²len_c² + len_a²len_b²)）"""
    numerator = len_a * len_b * len_c
    denominator = math.sqrt((len_b**2 * len_c**2) + (len_a**2 * len_c**2) + (len_a**2 * len_b**2))
    return numerator / denominator

len_a = 4.0
len_b = 4.0
len_c = 3.0


# result = calculate(len_a, len_b, len_c)
# print(f"len_h = {result:.6f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_96_ahsme_28",
    "type": 3,
    "level": 1,
    "cn_problem": f"给定一矩形平行六面体（长方体），其三条两两垂直的棱长分别为 ${len_a}>0, {len_b}>0, {len_c}>0$。设顶点 ${point_D}$ 的三个相邻顶点分别为 ${point_A}(0,0,{len_c}), {point_B}({len_a},0,0), {point_C}(0,{len_b},0)$，（即 ${point_D}{point_A}\\parallel z$ 轴，${point_D}{point_B}\\parallel x$ 轴，${point_D}{point_C}\\parallel y$ 轴）。求顶点 ${point_D}$ 到由点 ${point_A},{point_B},{point_C}$ 所确定平面 ${point_A}{point_B}{point_C}$ 的垂直距离。",
    "en_problem": f"Given a rectangular parallelepiped (cuboid) with three mutually perpendicular edge lengths ${len_a}>0, {len_b}>0, {len_c}>0$. Let vertex ${point_D}$ have three adjacent vertices ${point_A}(0,0,{len_c}), {point_B}({len_a},0,0), {point_C}(0,{len_b},0)$ (i.e., ${point_D}{point_A}\\parallel z$-axis, ${point_D}{point_B}\\parallel x$-axis, ${point_D}{point_C}\\parallel y$-axis). Find the explicit expression for the perpendicular distance from vertex ${point_D}$ to plane ${point_A}{point_B}{point_C}$.",
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
    f.write(json.dumps({json_data["id"]: f"aops_96_ahsme_28({mode}, {azimuth}, {elevation}, '{point_D}', '{point_A}', '{point_B}', '{point_C}')"}, ensure_ascii=False) + "\n")
