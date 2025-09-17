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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1 = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_edge, len_distance):
    """
    计算给定的几何表达式（四棱柱的侧面积）

    参数:
    len_edge (float): 底面边长
    len_distance (float): 点到平面的距离

    返回:
    float: 计算结果
    """
    return (2 * math.sqrt(2) * (len_edge ** 2) * len_distance) / math.sqrt(2 * (len_edge ** 2) - len_distance ** 2)


# 定义题干中的变量
len_edge = 1
len_distance = 4 / 3

# result = calculate(len_edge, len_distance)
# print(f"计算结果: {result:.6f}")

 
# Generate random lengths
len_edge = round(len_scaling_factor * float(len_edge), 2)
len_distance = round(len_scaling_factor * float(len_distance), 2)

# Calculate the result
result = calculate(len_edge, len_distance)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area1_6_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"已知四棱柱 {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1} 的底面为正方形，底面边长为 {len_edge}，侧棱与底面垂直。若点 {point_C} 到平面 {point_A}{point_B1}{point_D1} 的距离为 {len_distance}，则四棱柱 {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1} 的侧面积为多少？",
    "en_problem": f"A rectangular prism {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1} has a square base with edge length {len_edge}, and its lateral edges are perpendicular to the base. If the distance from point {point_C} to plane {point_A}{point_B1}{point_D1} is {len_distance}, find the lateral surface area of the rectangular prism {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1}.",
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
    f.write(json.dumps({json_data["id"]: f"area1_6_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}')"}, ensure_ascii=False) + "\n")
