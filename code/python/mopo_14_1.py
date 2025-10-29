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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_P = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_h, len_a, arg_theta):
    """计算len_d_min关于len_h、len_a和arg_theta的表达式"""
    # 计算各基础项
    len_h_sq = len_h ** 2
    len_a_sq = len_a ** 2
    sum_len_sq = len_h_sq + len_a_sq  # len_h² + len_a²

    # 计算第一部分：len_h²
    part1 = len_h_sq

    # 计算第二部分：2*len_a²*(1 - cos(arg_theta))
    cos_arg_theta = math.cos(arg_theta)
    part2 = 2 * len_a_sq * (1 - cos_arg_theta)

    # 计算第三部分的中间项：sqrt(2*(1 - cos(arg_theta)))
    sqrt_term = math.sqrt(2 * (1 - cos_arg_theta))

    # 计算反三角函数项：arcsin(len_a / sqrt(sum_len_sq))
    asin_arg = len_a / math.sqrt(sum_len_sq)
    arcsin_term = math.asin(asin_arg)

    # 计算反余弦函数的分子和分母
    acos_numerator = len_a * sqrt_term
    acos_denominator = 2 * math.sqrt(sum_len_sq)
    acos_arg = acos_numerator / acos_denominator
    arccos_term = math.acos(acos_arg)

    # 计算余弦项的参数和结果
    cos_arg = arcsin_term + arccos_term
    cos_result = math.cos(cos_arg)

    # 计算第三部分整体：2*len_h*len_a*sqrt_term*cos_result
    part3 = 2 * len_h * len_a * sqrt_term * cos_result

    # 计算根号内的总和并开方
    total = part1 + part2 - part3
    return math.sqrt(total)


# 测试示例
len_h = 1.0
len_a = math.sqrt(3)
arg_theta = math.acos(1 / 3)

# print(calculate(len_h, len_a, arg_theta))
# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_h, len_a, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_14_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"在直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，侧棱 ${point_A}{point_A1} = {len_h}$，底面 $\\\\triangle {point_A}{point_B}{point_C}$ 中 ${point_A}{point_B} = {point_B}{point_C} = {len_a}$，$\\\\cos\\\\angle {point_A}{point_B}{point_C} = \\\\cos {arg_theta}$。点 {point_P} 是 ${point_A1}{point_B}$ 上的动点，求 ${point_A}{point_P} + {point_P}{point_C1}$ 的最小值。",
    "en_problem": f"In a right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} where lateral edge ${point_A}{point_A1} = {len_h}$, base triangle has ${point_A}{point_B} = {point_B}{point_C} = {len_a}$, and $\\\\cos\\\\angle {point_A}{point_B}{point_C} = \\\\cos {arg_theta}$. Point {point_P} is a moving point on ${point_A1}{point_B}$. Find the minimum value of ${point_A}{point_P} + {point_P}{point_C1}$.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_14_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_P}')"}, ensure_ascii=False) + "\n")
