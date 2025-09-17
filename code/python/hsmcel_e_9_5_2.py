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
point_V, point_A, point_B, point_C, point_P = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_a, arg_theta):
    """计算arg_x的最小值和area_S的最小值"""
    arg_theta_rad = math.radians(arg_theta)  # 转换为弧度计算正弦值
    area_S_min = (math.sqrt(3) / 4) * (len_a ** 2) * math.sin(arg_theta_rad)
    return area_S_min


# 测试示例
len_a = 2
arg_theta = 30

# print(calculate(len_a, arg_theta))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
arg_theta = round(len_scaling_factor * float(arg_theta), 2)

# Calculate the result
result = calculate(len_a, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_9_5_2",
    "type": 4,
    "level": 3,
    "cn_problem": f"设 ${point_V}$-${point_A}{point_B}{point_C}$ 为正三棱锥，底面 $\\triangle {point_A}{point_B}{point_C}$ 为边长 ${len_a}>0$ 的正三角形；每条侧棱与底面所成夹角均为 ${arg_theta} \\in (0, 90°)$。过底边 ${point_B}{point_C}$ 作一动截面 $\\pi$，交侧棱 ${point_V}{point_A}$ 于点 ${point_P}$。设截面 $\\pi$ 与底面 ${point_A}{point_B}{point_C}$ 所成二面角为 $ arg_x  \\in (0, 90°)$。记截面三角形 $\\triangle {point_P}{point_B}{point_C}$ 的面积为 $area_S( arg_x )$。② 求最小面积 $area_S_{{\\min}}$。",
    "en_problem": f"Let ${point_V}$-${point_A}{point_B}{point_C}$ be a regular triangular pyramid with base $\\triangle {point_A}{point_B}{point_C}$ being an equilateral triangle with side length ${len_a}>0$; each lateral edge makes an angle ${arg_theta} \\in (0, 90°)$ with the base. Through the base edge ${point_B}{point_C}$, construct a movable cross-section $\\pi$ that intersects lateral edge ${point_V}{point_A}$ at point ${point_P}$. Let the dihedral angle between cross-section $\\pi$ and base ${point_A}{point_B}{point_C}$ be $ arg_x  \\in (0, 90°)$. Let the area of cross-section triangle $\\triangle {point_P}{point_B}{point_C}$ be $area_S( arg_x )$. ② Find the minimum area $area_S_{{\\min}}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_9_5_2({mode}, {azimuth}, {elevation}, '{point_V}', '{point_A}', '{point_B}', '{point_C}', '{point_P}')"}, ensure_ascii=False) + "\n")
