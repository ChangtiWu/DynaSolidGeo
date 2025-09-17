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
point_C, point_V, point_O = random.sample(string.ascii_uppercase, 3)

# Add result calculation code
import math


def calculate(len_radius):
    """
    计算给定的几何表达式（圆锥的侧面积）

    参数:
    len_radius (float): 球的半径

    返回:
    float: 计算结果
    """
    return 6 * math.pi * (len_radius ** 2)


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
    "id": "area1_11_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"已知球 {point_C} 与圆锥 {point_V}{point_O} 的侧面和底面均相切，球的体积为圆锥体积的 \\frac{{1}}{{2}}。若球的半径为 {len_radius}，则该圆锥的侧面积为多少？",
    "en_problem": f"A sphere {point_C} is tangent to both the lateral surface and base of cone {point_V}{point_O}, and the sphere's volume is \\frac{{1}}{{2}} of the cone's volume. If the sphere's radius is {len_radius}, find the lateral surface area of the cone.",
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
    f.write(json.dumps({json_data["id"]: f"area1_11_1({mode}, {azimuth}, {elevation}, '{point_C}', '{point_V}', '{point_O}')"}, ensure_ascii=False) + "\n")
