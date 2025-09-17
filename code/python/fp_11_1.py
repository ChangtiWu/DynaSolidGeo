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
point_O, point_O1, point_A, point_B, point_B1 = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math

def calculate(len_radius, area_surface):
    """
    计算绕圆柱侧面从A到B1的最短绳长

    参数:
    len_radius (float): 圆柱底面半径
    area_surface (float): 圆柱表面积

    返回:
    float: 最短绳长
    """
    # (S - 2πr^2) / (2πr) = 圆柱高 h
    h = (area_surface - 2 * math.pi * len_radius**2) / (2 * math.pi * len_radius)

    # 公式: rope = sqrt((πr)^2 + h^2)
    return math.sqrt((math.pi * len_radius) ** 2 + h ** 2)


# 题干给定的数值
len_radius = 2.0
area_surface = 20 * math.pi

# 验证输出
# result = calculate(len_radius, area_surface)
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_radius = round(len_scaling_factor * float(len_radius), 2)
area_surface = round(len_scaling_factor * float(area_surface), 2)

# Calculate the result
result = calculate(len_radius, area_surface)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fp_11_1",
    "type": 3,
    "level": 1,
    "cn_problem": f"已知圆柱 {point_O}{point_O1} 的底面圆 {point_O} 的半径为 {len_radius}，{point_A}{point_B} 为圆 {point_O} 的直径，圆柱的表面积为 {area_surface}。求由点 {point_A} 拉一根细绳绕圆柱侧面到达 {point_B1} 的绳长的最小值。",
    "en_problem": f"Given that cylinder {point_O}{point_O1} has base circle {point_O} with radius {len_radius}, {point_A}{point_B} is the diameter of circle {point_O}, and the cylinder's surface area is {area_surface}. Find the minimum length of a thin rope pulled from point {point_A} around the lateral surface of the cylinder to reach {point_B1}.",
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
    f.write(json.dumps({json_data["id"]: f"fp_11_1({mode}, {azimuth}, {elevation}, '{point_O}', '{point_O1}', '{point_A}', '{point_B}', '{point_B1}')"}, ensure_ascii=False) + "\n")
