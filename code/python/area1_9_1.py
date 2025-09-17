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
point_E, point_A, point_B, point_C, point_D, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_edge):
    """
    计算给定的几何表达式（由立方体面心连线构成的八面体的表面积）

    参数:
    len_edge (float): 正方体的棱长

    返回:
    float: 计算结果
    """
    return math.sqrt(3) * (len_edge ** 2)


# 定义题干中的变量
len_edge = 2

# result = calculate(len_edge)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_edge = round(len_scaling_factor * float(len_edge), 2)

# Calculate the result
result = calculate(len_edge)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area1_9_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"将棱长为 {len_edge} 的正方体六个面的中心连线，可得到八面体 {point_E} - {point_A}{point_B}{point_C}{point_D} - {point_F}，则该八面体的表面积为多少？",
    "en_problem": f"By connecting the centers of the six faces of a cube with edge length {len_edge}, we obtain an octahedron {point_E} - {point_A}{point_B}{point_C}{point_D} - {point_F}. Find the surface area of this octahedron.",
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
    f.write(json.dumps({json_data["id"]: f"area1_9_1({mode}, {azimuth}, {elevation}, '{point_E}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_F}')"}, ensure_ascii=False) + "\n")
