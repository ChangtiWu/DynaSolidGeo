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
point_A, point_B, point_C, point_D, point_E = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_a):
    """
    计算给定的几何表达式

    参数:
    len_a (float): 题干给定的长度单位

    返回:
    float: 计算结果
    """
    # 根据题干解法，sin(theta) = sqrt(3) / 3
    result = math.sqrt(3) / 3
    return result


# 定义题干参数
len_a = 1.0

# 验证输出（与参考答案对比）
# result = calculate(len_a)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_18_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在梯形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_D}∥{point_B}{point_C}且{point_A}{point_D}⊥{point_C}{point_D}，线段{point_A}{point_D}上一点{point_E}满足：{point_C}{point_D}={point_D}{point_E}={len_a}，{point_A}{point_E}={point_B}{point_C}=2*{len_a}。将△{point_A}{point_B}{point_E}、△{point_C}{point_D}{point_E}分别沿{point_B}{point_E}、{point_C}{point_E}折起，使{point_A}{point_D}=√5*{len_a}，{point_B}{point_D}=√3*{len_a}，得到空间几何体。求直线{point_B}{point_D}与平面{point_A}{point_D}{point_E}所成角的正弦值。",
    "en_problem": f"In trapezoid {point_A}{point_B}{point_C}{point_D}, {point_A}{point_D}∥{point_B}{point_C} and {point_A}{point_D}⊥{point_C}{point_D}, point {point_E} on segment {point_A}{point_D} satisfies: {point_C}{point_D}={point_D}{point_E}={len_a}, {point_A}{point_E}={point_B}{point_C}=2*{len_a}. Fold △{point_A}{point_B}{point_E} and △{point_C}{point_D}{point_E} along {point_B}{point_E} and {point_C}{point_E} respectively, so that {point_A}{point_D}=√5*{len_a}, {point_B}{point_D}=√3*{len_a}, forming a spatial geometric body. Find the sine of the angle between line {point_B}{point_D} and plane {point_A}{point_D}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"sup_18_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
