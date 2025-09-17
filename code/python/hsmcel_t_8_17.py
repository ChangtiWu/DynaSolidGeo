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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D, point_F, point_E = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math

def caculate(len_n, arg_theta):
    """
    计算给定公式的数值
    
    参数:
    len_n (float): 长度参数
    arg_theta (float): 角度参数（弧度制）
    
    返回:
    float: 公式计算结果
    """
    # 计算根号内第一项的内部乘积
    term1_inner = (len_n * math.sqrt(5) / 2) * math.tan(arg_theta)
    # 第一项的平方
    term1_squared = term1_inner ** 2
    # 根号内第二项
    term2 = (len_n ** 2) / 4
    # 计算总和的平方根
    result = math.sqrt(term1_squared + term2)
    return result


# 题干给定的数值（按比例）
len_n = 2.0  # BC = BF
arg_theta = math.radians(60)  # 题目要求角为 60°

# 验证输出
#exists = check_point_exists(len_m, len_n, arg_theta)
#print(f"是否存在点E: {exists}")

# Generate random lengths
len_n = round(len_scaling_factor * float(len_n), 2)

# Calculate the result
result = caculate(len_n, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_8_17",
    "type": 3,
    "level": 2,
    "cn_problem": f"在直三棱柱{point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}中，{point_A}{point_B} = {point_A}{point_C}，{point_D}为{point_B}{point_C}的中点，{point_F}为棱{point_B}{point_B1}上一点，满足，{point_B}{point_F}: {point_F}{point_B1} = 2: 1，{point_B}{point_F} = {point_B}{point_C} = {len_n}。试问：要在{point_A}{point_D}上找到一点{point_E}，使得{point_E}{point_F}与平面{point_B}{point_B1}{point_C1}{point_C}所成的角为{arg_theta}（{arg_theta}为锐角），{point_A}{point_B}最小长度为多少？",
    "en_problem": f"In a right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, {point_A}{point_B} = {point_A}{point_C}, {point_D} is the midpoint of {point_B}{point_C}, and {point_F} is a point on edge {point_B}{point_B1} with {point_B}{point_F}: {point_F}{point_B1} = 2: 1 and {point_B}{point_F} = {point_B}{point_C} = {len_n}. What is the minimun length of {point_A}{point_B} in order for there to exist a point {point_E} on segment {point_A}{point_D} such that the angle between {point_E}{point_F} and plane {point_B}{point_B1}{point_C1}{point_C} is {arg_theta} ?",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_8_17({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}', '{point_F}', '{point_E}')"}, ensure_ascii=False) + "\n")
