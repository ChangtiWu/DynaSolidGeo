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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math

def caculate(len_a, arg_theta):
    """
    计算给定公式的体积值
    
    参数:
    len_a (float): 长度参数
    arg_theta (float): 角度参数（弧度制）
    
    返回:
    float: 计算结果V
    """
    # 计算常数系数部分
    constant = (1/3) * (1/2) * math.sqrt(2)
    # 计算len_a的平方
    len_a_sq = len_a ** 2
    # 计算tan(arg_theta)
    tan_theta = math.tan(arg_theta)
    # 计算 len_a / tan(theta)
    term1 = len_a / tan_theta
    # 计算括号内的部分：2*len_a - (len_a/(2*tan(theta)))
    term2 = 2 * len_a - (len_a / (2 * tan_theta))
    # 组合所有部分计算V
    V = constant * len_a_sq * term1 * term2
    
    return V

# 测试示例
len_a = 2.0
arg_theta = math.pi / 4
# print(caculate(len_a, arg_theta))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = caculate(len_a, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_s_10_1",
    "type": 5,
    "level": 3,
    "cn_problem": f"在正四棱柱{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}中，底面边长为{len_a}，{point_E}是侧棱{point_D}{point_D1}上一点，截面{point_E}{point_A}{point_C}//{point_B}{point_D1}，且截面{point_E}{point_A}{point_C}与底面{point_A}{point_B}{point_C}{point_D}所成的角为{arg_theta}，求三棱锥{point_B1}-{point_E}{point_A}{point_C}的体积。",
    "en_problem": f"In a regular quadrangular prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} with base side length {len_a}, point {point_E} is on lateral edge {point_D}{point_D1}. The cross-section {point_E}{point_A}{point_C} is parallel to {point_B}{point_D1}, and the angle between plane {point_E}{point_A}{point_C} and base {point_A}{point_B}{point_C}{point_D} is {arg_theta}. Find the volume of tetrahedron {point_B1}-{point_E}{point_A}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_s_10_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}')"}, ensure_ascii=False) + "\n")
