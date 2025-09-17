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
point_A, point_B, point_C, point_D, point_P, point_E, point_M, point_N = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_s):
    """计算len_l关于len_s的表达式（结果为2πlen_s/9）"""
    return (2 * math.pi * len_s) / 9


# 测试示例
len_s = 3.0

# print(calculate(len_s))

# Generate random lengths
len_s = round(len_scaling_factor * float(len_s), 2)

# Calculate the result
result = calculate(len_s)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_41_3",
    "type": 8,
    "level": 2,
    "cn_problem": f"设矩形 {point_A}{point_B}{point_C}{point_D} 中，沿对角线 ${point_B}{point_D}$ 折叠后，点 {point_A} 到 {point_P}，满足平面 {point_P}{point_B}{point_D} $\\\\perp$ 平面 {point_B}{point_C}{point_D}。设 {point_E} 为 {point_P} 在 ${point_B}{point_D}$ 上的垂足（${point_P}{point_E} \\\\perp {point_B}{point_D}$，${point_P}{point_E} =  len_h $ 为 {point_P} 到平面 {point_B}{point_C}{point_D} 的距离），{point_B}(- len_t , 0, 0)，{point_D}({len_s}, 0, 0)（${point_B}{point_D}$ 沿 $x$ 轴，{point_E} 为原点(0,0,0)），{point_M} 为 ${point_P}{point_D}$ 中点。点 {point_N}( len_x ,  len_y , 0) 在平面 {point_B}{point_C}{point_D} 内运动，若直线 {point_P}{point_N} 与直线 {point_M}{point_N} 与平面 {point_B}{point_C}{point_D} 所成角相等，求点 {point_N} 轨迹的长度。",
    "en_problem": f"Let rectangle {point_A}{point_B}{point_C}{point_D} be folded along diagonal ${point_B}{point_D}$ so that point {point_A} reaches {point_P}, with plane {point_P}{point_B}{point_D} $\\\\perp$ plane {point_B}{point_C}{point_D}. Let {point_E} be the foot of perpendicular from {point_P} to ${point_B}{point_D}$ (${point_P}{point_E} \\\\perp {point_B}{point_D}$, ${point_P}{point_E} =  len_h $ is the distance from {point_P} to plane {point_B}{point_C}{point_D}), {point_B}(- len_t , 0, 0), {point_D}({len_s}, 0, 0) (${point_B}{point_D}$ along $x$-axis, {point_E} as origin (0,0,0)), and {point_M} is the midpoint of ${point_P}{point_D}$. Point {point_N}( len_x ,  len_y , 0) moves within plane {point_B}{point_C}{point_D}. If lines {point_P}{point_N} and {point_M}{point_N} make equal angles with plane {point_B}{point_C}{point_D}, find the trajectory length of point {point_N}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_41_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}', '{point_E}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
