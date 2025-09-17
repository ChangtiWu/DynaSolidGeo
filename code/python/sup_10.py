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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_P, point_Q = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math


def calculate(len_a, len_b, len_c):
    """
    计算给定的几何表达式

    参数:
    len_a (float): AB 的长度
    len_b (float): AD 的长度
    len_c (float): AA₁ 的长度

    返回:
    float: 计算结果
    """
    # 根据题干解法，最小值 = (len_a * len_b) / sqrt(len_b^2 + len_c^2) + len_c
    result = (len_a * len_b) / math.sqrt(len_b ** 2 + len_c ** 2) + len_c
    return result


# 定义题干参数
len_a = 2.0
len_b = 3.0
len_c = math.sqrt(3)

# 验证输出（与参考答案对比）
#result = calculate(len_a, len_b, len_c)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_10",
    "type": 7,
    "level": 2,
    "cn_problem": f"已知长方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}中，{point_A}{point_B}={len_a}，{point_A}{point_D}={len_b}，{point_A}{point_A1}={len_c}。点{point_P}在线段{point_B}{point_C1}上，{point_Q}是线段{point_B}{point_C}上的动点，求|{point_P}{point_D1}|+|{point_P}{point_Q}|的最小值。",
    "en_problem": f"In rectangular parallelepiped {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, {point_A}{point_B}={len_a}, {point_A}{point_D}={len_b}, {point_A}{point_A1}={len_c}. Point {point_P} is on segment {point_B}{point_C1}, {point_Q} is a moving point on segment {point_B}{point_C}. Find the minimum value of |{point_P}{point_D1}|+|{point_P}{point_Q}|.",
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
    f.write(json.dumps({json_data["id"]: f"sup_10({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_P}', '{point_Q}')"}, ensure_ascii=False) + "\n")
