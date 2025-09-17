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
point_A, point_B, point_P = random.sample(string.ascii_uppercase, 3)

# Add result calculation code
import math


def calculate(len_radius, len_height, len_cone_height):
    """
    计算给定的几何表达式（圆柱外接球表面积与圆锥侧面积的比值）

    参数:
    len_radius (float): 圆柱底面圆的半径
    len_height (float): 圆柱的高
    len_cone_height (float): 圆锥的轴高

    返回:
    float: 计算结果
    """
    return (4 * len_radius ** 2 + len_height ** 2) / (len_radius * math.sqrt(len_radius ** 2 + len_cone_height ** 2))


# 定义题干中的变量
len_radius = math.sqrt(2)
len_height = 2
len_cone_height = math.sqrt(2)
 
# Generate random lengths
len_radius = round(len_scaling_factor * float(len_radius), 2)
len_height = round(len_scaling_factor * float(len_height), 2)
len_cone_height = round(len_scaling_factor * float(len_cone_height), 2)

# Calculate the result
result = calculate(len_radius, len_height, len_cone_height)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area1_12_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"陀螺可近似视为由圆锥和圆柱组合而成的几何体，圆柱上、下底面圆心分别为 {point_A},{point_B}，圆锥顶点为 {point_P}。设圆柱底面圆的半径为 {len_radius}，圆柱的高为 {len_height}（即 {point_A}{point_B} = {len_height}），圆锥的轴高为 {len_cone_height}（即 {point_P}{point_A} = {len_cone_height}）。求圆柱的外接球的表面积与圆锥的侧面积的比值。",
    "en_problem": f"A spinning top can be approximated as a geometric body composed of a cone and cylinder. The centers of the cylinder's upper and lower bases are {point_A} and {point_B} respectively, and the cone's vertex is {point_P}. Let the cylinder base radius be {len_radius}, cylinder height be {len_height} (i.e., {point_A}{point_B} = {len_height}), and cone axial height be {len_cone_height} (i.e., {point_P}{point_A} = {len_cone_height}). Find the ratio of the cylinder's circumscribed sphere surface area to the cone's lateral surface area.",
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
    f.write(json.dumps({json_data["id"]: f"area1_12_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_P}')"}, ensure_ascii=False) + "\n")
