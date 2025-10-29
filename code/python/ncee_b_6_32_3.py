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
point_A, point_B, point_C, point_A1, point_B1, point_E, point_F = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_a, len_b, len_h1, len_h2):
    """
    计算直线A1B1与平面BCB1所成角的正弦值

    参数:
    len_a (float): 长度参数 a，即AB和AC的长度
    len_b (float): 长度参数 b，即BC的长度
    len_h1 (float): 长度参数 h1，即AA1的长度
    len_h2 (float): 长度参数 h2，即BB1的长度

    返回:
    float: 直线A1B1与平面BCB1所成角的正弦值
    """
    # 计算AE的长度（等腰三角形ABC的高）
    ae = math.sqrt(len_a ** 2 - (len_b / 2) ** 2)

    # 计算直线A1B1与平面BCB1所成角的正弦值
    numerator = ae ** 2
    denominator = ae * math.sqrt(len_a ** 2 + (len_h2 - len_h1) ** 2)
    sin_theta = numerator / denominator
    theta_angle = math.asin(sin_theta)
    return theta_angle


# 定义参数
len_a = 3
len_b = 2 * math.sqrt(5)
len_h1 = math.sqrt(7)
len_h2 = 2 * math.sqrt(7)
#
# # 调用函数计算结果
# result = calculate(len_a, len_b, len_h1, len_h2)
# print(f"直线A1B1与平面BCB1所成角为: {result}")

len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_h1 = round(len_scaling_factor * float(len_h1), 2)
len_h2 = round(len_scaling_factor * float(len_h2), 2)

# Calculate the result
result = calculate(len_a, len_b, len_h1, len_h2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_32_3",
    "type": 2,
    "level": 2,
    "cn_problem": f"已知{point_A}{point_A1} ⊥ 平面{point_A}{point_B}{point_C}，{point_B}{point_B1} ∥ {point_A}{point_A1}，{point_A}{point_B} = {point_A}{point_C} = {len_a}，{point_B}{point_C} = {len_b}，{point_A}{point_A1} = {len_h1}，{point_B}{point_B1} = {len_h2}。点{point_E}是{point_B}{point_C}的中点，求直线{point_A1}{point_B1}与平面{point_B}{point_C}{point_B1}所成角的大小。",
    "en_problem": f"Given {point_A}{point_A1} ⊥ plane {point_A}{point_B}{point_C}, {point_B}{point_B1} ∥ {point_A}{point_A1}, {point_A}{point_B} = {point_A}{point_C} = {len_a}, {point_B}{point_C} = {len_b}, {point_A}{point_A1} = {len_h1}, {point_B}{point_B1} = {len_h2}. Point {point_E} is the midpoint of {point_B}{point_C}. Find the size of the angle between line {point_A1}{point_B1} and plane {point_B}{point_C}{point_B1}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_32_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
