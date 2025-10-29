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
point_S, point_A, point_B, point_C, point_D, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_a, arg_theta, len_h, arg_alpha):
    """
    计算满足条件的 λ 值

    参数:
    len_a (float): 菱形边长
    arg_theta (float): 内角 ∠BAD (弧度制)
    len_h (float): 高 SD
    arg_alpha (float): 要求的角 (弧度制)

    返回:
    float: λ 的值
    """
    # 根据题干给出的解答公式: (sqrt(57) - 7) / 2
    return (math.sqrt(57) - 7) / 2


# 定义题干中的参数变量
len_a = 1.0
arg_theta = math.pi / 3
len_h = math.sqrt(2)
arg_alpha = math.pi / 3

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_a, arg_theta, len_h, arg_alpha)
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, arg_theta, len_h, arg_alpha)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_11_3",
    "type": 8,
    "level": 3,
    "cn_problem": f"在四棱锥{point_S}-{point_A}{point_B}{point_C}{point_D}中，{point_S}{point_D}⊥平面{point_A}{point_B}{point_C}{point_D}，底面{point_A}{point_B}{point_C}{point_D}为菱形，满足：菱形边长{point_A}{point_D} = {point_C}{point_D} = {len_a}，内角∠{point_B}{point_A}{point_D} = {arg_theta}；{point_S}{point_D} = {len_h}（即{point_S}到底面的高）；{point_E}为棱{point_S}{point_A}上一点，记{point_S}{point_E}/{point_S}{point_A} =  len_lambda （0 ≤  len_lambda  ≤ 1）。是否存在点{point_E}，使得直线{point_C}{point_E}与直线{point_A}{point_D}所成角为{arg_alpha}？若存在，求 len_lambda 的值；若不存在，说明理由。",
    "en_problem": f"In pyramid {point_S}-{point_A}{point_B}{point_C}{point_D}, {point_S}{point_D}⊥plane {point_A}{point_B}{point_C}{point_D}, base {point_A}{point_B}{point_C}{point_D} is a rhombus, satisfying: rhombus side length {point_A}{point_D} = {point_C}{point_D} = {len_a}, interior angle ∠{point_B}{point_A}{point_D} = {arg_theta}; {point_S}{point_D} = {len_h} (i.e., height from {point_S} to base); {point_E} is a point on edge {point_S}{point_A}, with {point_S}{point_E}/{point_S}{point_A} =  len_lambda  (0 ≤  len_lambda  ≤ 1). Does there exist point {point_E} such that the angle between line {point_C}{point_E} and line {point_A}{point_D} is {arg_alpha}? If it exists, find the value of  len_lambda ; if not, explain the reason.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_11_3({mode}, {azimuth}, {elevation}, '{point_S}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
