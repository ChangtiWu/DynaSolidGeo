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
len_scaling_factor = round(random.uniform(0.1, 10.0), 1)

# Generate random point names
point_P, point_O, point_O1, point_A, point_B, point_A1 = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_r, area_S, arg_alpha):
    """
    计算四面体 P-A1AB 的全面积

    参数:
    len_r (float): 圆的半径
    area_S (float): 圆柱表面积
    arg_alpha (float): ∠AOP 的角度（弧度）

    返回:
    float: 四面体全面积
    """
    # 圆柱高
    len_h = (area_S - 2 * math.pi * len_r ** 2) / (2 * math.pi * len_r)

    # S1 = len_r^2 * sin(arg_alpha)
    S1 = len_r ** 2 * math.sin(arg_alpha)

    # S2 = len_r * len_h * sin(arg_alpha/2)
    S2 = len_r * len_h * math.sin(arg_alpha / 2)

    # S3 = len_r * len_h
    S3 = len_r * len_h

    # S4 = len_r * cos(arg_alpha/2) * sqrt(len_h^2 + 4 * len_r^2 * sin^2(arg_alpha/2))
    S4 = len_r * math.cos(arg_alpha / 2) * math.sqrt(len_h ** 2 + 4 * len_r ** 2 * math.sin(arg_alpha / 2) ** 2)

    return S1 + S2 + S3 + S4


# 定义题干中的参数
len_r = 2.0          # 圆半径
area_S = 20 * math.pi # 圆柱表面积
arg_alpha = 2 * math.pi / 3  # 120°转为弧度

# 验证计算结果
#result = calculate(len_r, area_S, arg_alpha)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_r = round(len_scaling_factor * float(len_r), 2)
area_S = round((len_scaling_factor**2) * float(area_S), 2)

# Calculate the result
result = calculate(len_r, area_S, arg_alpha)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_12_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"如图，已知点 {point_P} 在圆柱 {point_O}{point_O1} 的底面圆 {point_O} 上，圆 {point_O} 的半径为 {len_r}（直径 {point_A}{point_B} = 2*{len_r}），圆柱 {point_O}{point_O1} 的表面积为 {area_S}，∠{point_A}{point_O}{point_P} = {arg_alpha}。求四面体 {point_P} - {point_A1}{point_A}{point_B} 的全面积。",
    "en_problem": f"As shown in the figure, point {point_P} is on the base circle {point_O} of cylinder {point_O}{point_O1}, the radius of circle {point_O} is {len_r} (diameter {point_A}{point_B} = 2*{len_r}), the surface area of cylinder {point_O}{point_O1} is {area_S}, and ∠{point_A}{point_O}{point_P} = {arg_alpha}. Find the total surface area of tetrahedron {point_P} - {point_A1}{point_A}{point_B}.",
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
    f.write(json.dumps({json_data["id"]: f"area2_12_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_O}', '{point_A}', '{point_B}')"}, ensure_ascii=False) + "\n")
