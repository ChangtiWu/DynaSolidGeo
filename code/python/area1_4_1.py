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


def calculate(len_r1, len_r2, len_r3, len_ratio1, len_ratio2, len_height):
    """
    计算给定的几何表达式（汝窑双耳罐的侧面积）

    参数:
    len_r1 (float): 上圆台的上底面半径
    len_r2 (float): 中间圆的半径
    len_r3 (float): 下圆台的下底面半径
    len_ratio1 (int): 上圆台的高比
    len_ratio2 (int): 下圆台的高比
    len_height (float): 总高度

    返回:
    float: 计算结果
    """
    return (
        math.pi
        * math.sqrt((len_r2 - len_r1) ** 2 + (len_ratio1 * len_height / (len_ratio1 + len_ratio2)) ** 2)
        * (len_r1 + len_r2)
        + math.pi
        * math.sqrt((len_r2 - len_r3) ** 2 + (len_ratio2 * len_height / (len_ratio1 + len_ratio2)) ** 2)
        * (len_r2 + len_r3)
    )


# 定义题干中的变量
len_r1 = 8 / 2
len_r2 = 20 / 2
len_r3 = 12 / 2
len_ratio1 = 3
len_ratio2 = 4
len_height = 14

# result = calculate(len_r1, len_r2, len_r3, len_ratio1, len_ratio2, len_height)
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_r1 = round(len_scaling_factor * float(len_r1), 2)
len_r2 = round(len_scaling_factor * float(len_r2), 2)
len_r3 = round(len_scaling_factor * float(len_r3), 2)
len_height = round(len_scaling_factor * float(len_height), 2)

# Calculate the result
result = calculate(len_r1, len_r2, len_r3, len_ratio1, len_ratio2, len_height)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area1_4_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"宋代汝窑双耳罐可近似看成由两个圆台拼接而成。设上圆台的上底面半径为 {len_r1}，下底面半径为 {len_r2}；下圆台的上底面半径为 {len_r2}，下底面半径为 {len_r3}；两个圆台的高之比为 {len_ratio1}:{len_ratio2}，总高为 {len_height}。求该汝窑双耳罐的侧面积。",
    "en_problem": f"A Song Dynasty Ru kiln double-eared jar can be approximated as two truncated cones joined together. Let the upper truncated cone have upper base radius {len_r1} and lower base radius {len_r2}; the lower truncated cone have upper base radius {len_r2} and lower base radius {len_r3}; the height ratio of the two truncated cones be {len_ratio1}:{len_ratio2}, and the total height be {len_height}. Find the lateral surface area of the jar.",
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
    f.write(json.dumps({json_data["id"]: f"area1_4_1({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
