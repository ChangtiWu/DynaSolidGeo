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
point_A, point_B, point_C, point_M, point_N, point_A1, point_H = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_b):
    """
    计算 A₁M 与平面 BCMN 所成角的正弦值最大值

    参数:
    len_b (float): 基本长度单位 b

    返回:
    float: 正弦值最大值
    """
    # 根据题干给出的解答公式: 2√2 / 5
    return (2 * math.sqrt(2)) / 5


# 定义题干中的参数变量
len_b = 1.0  # 题干里作为参数的 b

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_b)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_1_1",
    "type": 8,
    "level": 2,
    "cn_problem": f"在△{point_A}{point_B}{point_C}中，{point_A}{point_C} = 2*{len_b}√2，{point_B}{point_C} = 6*{len_b}（{len_b} > 0为参数），∠{point_C} = π/4，过{point_A}{point_C}的中点{point_M}的动直线l与线段{point_A}{point_B}交于点{point_N}，将△{point_A}{point_M}{point_N}沿直线l向上翻折至△{point_A1}{point_M}{point_N}，使得点{point_A1}在平面{point_B}{point_C}{point_M}{point_N}内的射影{point_H}落在线段{point_B}{point_C}上，则斜线{point_A1}{point_M}与平面{point_B}{point_C}{point_M}{point_N}所成角的正弦值的最大值为多少？",
    "en_problem": f"In triangle {point_A}{point_B}{point_C}, {point_A}{point_C} = 2*{len_b}√2, {point_B}{point_C} = 6*{len_b} ({len_b} > 0 is a parameter), ∠{point_C} = π/4, a moving line l through the midpoint {point_M} of {point_A}{point_C} intersects segment {point_A}{point_B} at point {point_N}. Triangle {point_A}{point_M}{point_N} is folded upward along line l to triangle {point_A1}{point_M}{point_N}, such that the projection {point_H} of point {point_A1} onto plane {point_B}{point_C}{point_M}{point_N} lies on segment {point_B}{point_C}. What is the maximum value of the sine of the angle between line {point_A1}{point_M} and plane {point_B}{point_C}{point_M}{point_N}?",
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
    f.write(json.dumps({json_data["id"]: f"fz1_1_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_M}', '{point_N}', '{point_A1}', '{point_H}')"}, ensure_ascii=False) + "\n")
