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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_P, point_Q = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a, len_h):
    """计算参数param_cos的值（表达式为分子绝对值部分除以两个平方根的乘积）"""
    # 计算分子部分：|len_h² - len_a²/4|
    numerator = abs(len_h ** 2 - (len_a ** 2) / 4)
    # 计算分母的两个平方根部分
    sqrt_term1 = math.sqrt(len_h ** 2 + (len_a ** 2) / 4)
    sqrt_term2 = math.sqrt(len_h ** 2 + len_a ** 2)
    # 分母为两个平方根的乘积
    denominator = sqrt_term1 * sqrt_term2
    # 返回最终结果
    return numerator / denominator


# 测试示例
len_a = 2.0
len_h = 2.0

# print(calculate(len_a, len_h))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_17_1",
    "type": 2,
    "level": 2,
    "cn_problem": f"如图，在正三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，设底面 △{point_A}{point_B}{point_C} 为边长 {len_a}>0 的正三角形，侧棱全部垂直于底面，且 {point_A}{point_A1}={point_B}{point_B1}={point_C}{point_C1}={len_h}>0；点 {point_P} 为侧棱 {point_A1}{point_B1} 的中点，点 {point_Q} 为底边 {point_B}{point_C} 的中点。设直线 {point_B}{point_P} 与对角线 {point_A}{point_C1} 所成夹角为 ang_theta，求其余弦值。",
    "en_problem": f"As shown, in regular triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, let the base △{point_A}{point_B}{point_C} be an equilateral triangle with side length {len_a}>0, all lateral edges are perpendicular to the base, and {point_A}{point_A1}={point_B}{point_B1}={point_C}{point_C1}={len_h}>0; point {point_P} is the midpoint of lateral edge {point_A1}{point_B1}, point {point_Q} is the midpoint of base edge {point_B}{point_C}. Let the angle between line {point_B}{point_P} and diagonal {point_A}{point_C1} be ang_theta, find its cosine value.",
    "solution": f"{result}",
    "image": f"images/{os.path.splitext(os.path.basename(__file__))[0]}.png"
}

# video mode
if args.mode == 1:
    json_data["image"] = f"videos/{os.path.splitext(os.path.basename(__file__))[0]}.mp4"



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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_17_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_P}', '{point_Q}')"}, ensure_ascii=False) + "\n")
