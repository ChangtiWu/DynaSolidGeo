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

# Add result calculation code
import math


def calculate(len_height, len_radius, len_ratio, volume_cone):
    """
    计算给定的几何表达式（圆锥的表面积）

    参数:
    len_height (float): 圆锥的高
    len_radius (float): 底面半径
    len_ratio (float): 高与底面半径的比值
    volume_cone (float): 圆锥的体积

    返回:
    float: 计算结果
    """
    return math.pi * ((3 * volume_cone) / (math.pi * len_ratio)) ** (2 / 3) * (1 + math.sqrt(len_ratio ** 2 + 1))


# 定义题干中的变量
len_height = 3  # 题干给了比值，不直接需要具体数值，但仍定义
len_radius = 2  # 同上
len_ratio = 3 / 2
volume_cone = 32 * math.pi

# result = calculate(len_height, len_radius, len_ratio, volume_cone)
# print(f"计算结果: {result:.6f}")

 
# Generate random lengths
len_height = round(len_scaling_factor * float(len_height), 2)
len_radius = round(len_scaling_factor * float(len_radius), 2)
len_ratio = round(len_scaling_factor * float(len_ratio), 2)
volume_cone = round((len_scaling_factor**3) * float(volume_cone), 2)

# Calculate the result
result = calculate(len_height, len_radius, len_ratio, volume_cone)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area1_14_2",
    "type": 4,
    "level": 1,
    "cn_problem": f"已知圆锥的高为 {len_height}，底面半径为 {len_radius}，满足高与底面半径的比 \\frac{{len_height}}{{len_radius}} = {len_ratio}（{len_ratio} 为正常数），且圆锥的体积为 {volume_cone}，求该圆锥的表面积。",
    "en_problem": f"A cone has height {len_height} and base radius {len_radius}, with height-to-radius ratio \\frac{{len_height}}{{len_radius}} = {len_ratio} ({len_ratio} is a positive constant), and volume {volume_cone}. Find the surface area of the cone.",
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
    f.write(json.dumps({json_data["id"]: f"area1_14_2({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
