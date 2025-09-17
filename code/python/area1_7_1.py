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
point_O = random.sample(string.ascii_uppercase, 1)[0]

# Add result calculation code
import math


def calculate(len_radius):
    """
    计算给定的几何表达式（圆锥侧面积最小值）

    参数:
    len_radius (float): 球的半径

    返回:
    float: 计算结果
    """
    return (3 + 2 * math.sqrt(2)) * math.pi * len_radius ** 2


# 定义题干中的变量
len_radius = 1

# result = calculate(len_radius)
# print(f"计算结果: {result:.6f}")

 
# Generate random lengths
len_radius = round(len_scaling_factor * float(len_radius), 2)

# Calculate the result
result = calculate(len_radius)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area1_7_1",
    "type": 4,
    "level": 2,
    "cn_problem": f"如图圆锥内的球 {point_O} 与圆锥的侧面与底面都相切，且球的半径为 {len_radius}，则圆锥侧面积的最小值为多少？",
    "en_problem": f"A sphere {point_O} inside a cone is tangent to both the lateral surface and the base of the cone, with sphere radius {len_radius}. Find the minimum value of the cone's lateral surface area.",
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
    f.write(json.dumps({json_data["id"]: f"area1_7_1({mode}, {azimuth}, {elevation}, '{point_O}')"}, ensure_ascii=False) + "\n")
