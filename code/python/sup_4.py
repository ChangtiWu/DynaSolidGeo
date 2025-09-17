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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M, point_N, point_E = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math


def calculate(len_a):
    """
    计算给定的几何表达式

    参数:
    len_a (float): 正方体的棱长

    返回:
    float: 计算结果
    """
    # 根据题干解法，d = (sqrt(2) / 4) * len_a
    result = (math.sqrt(2) / 4) * len_a
    return result


# 定义题干参数
len_a = 1.0

# 验证输出（与参考答案对比）
#result = calculate(len_a)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_4",
    "type": 3,
    "level": 1,
    "cn_problem": f"在棱长为{len_a}的正方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}中，{point_M}、{point_N}分别是棱{point_A}{point_B}、{point_C}{point_C1}的中点，{point_E}是{point_B}{point_D}的中点，求异面直线{point_D1}{point_M}与{point_E}{point_N}间的距离。",
    "en_problem": f"In a cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} with edge length {len_a}, {point_M} and {point_N} are midpoints of edges {point_A}{point_B} and {point_C}{point_C1} respectively, {point_E} is the midpoint of {point_B}{point_D}. Find the distance between skew lines {point_D1}{point_M} and {point_E}{point_N}.",
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
    f.write(json.dumps({json_data["id"]: f"sup_4({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_M}', '{point_N}', '{point_E}')"}, ensure_ascii=False) + "\n")
