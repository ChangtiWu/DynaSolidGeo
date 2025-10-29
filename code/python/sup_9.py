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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_P = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math


def calculate(len_a, len_h):
    """
    计算给定的几何表达式

    参数:
    len_a (float): 底面正方形的边长
    len_h (float): 侧棱的高

    返回:
    float: 计算结果
    """
    # 根据题干解法，tanθ_max = sqrt(len_a^2 + len_h^2) / len_a
    result = math.sqrt((len_a ** 2) + (len_h ** 2)) / len_a
    return result


# 定义题干参数
len_a = 3.0
len_h = 4.0

# 验证输出（与参考答案对比）
#result = calculate(len_a, len_h)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_9",
    "type": 7,
    "level": 2,
    "cn_problem": f"在正四棱柱{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}中，底面正方形边长为{len_a}，侧棱高为{len_h}。点{point_P}是侧面{point_B}{point_C}{point_C1}{point_B1}内的动点，且{point_A}{point_P}⊥{point_B}{point_D1}，记{point_A}{point_P}与平面{point_B}{point_C}{point_C1}{point_B1}所成的角为 arg_theta ，求tan arg_theta 的最大值。",
    "en_problem": f"In a regular square prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, the base square has side length {len_a} and lateral edge height {len_h}. Point {point_P} is a moving point on lateral face {point_B}{point_C}{point_C1}{point_B1}, with {point_A}{point_P}⊥{point_B}{point_D1}. Let  arg_theta  be the angle between {point_A}{point_P} and plane {point_B}{point_C}{point_C1}{point_B1}. Find the maximum value of tan arg_theta .",
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
    f.write(json.dumps({json_data["id"]: f"sup_9({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_P}')"}, ensure_ascii=False) + "\n")
