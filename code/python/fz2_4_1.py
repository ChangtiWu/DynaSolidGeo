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
point_A, point_B, point_C, point_D, point_E, point_F, point_O = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算三棱锥 O-DEF 的外接球表面积

    参数:
    len_a (float): 正方形边长

    返回:
    float: 外接球表面积
    """
    # 根据题干给出的解答公式: (3 * π * len_a^2) / 2
    return (3 * math.pi * (len_a ** 2)) / 2


# 定义题干中的参数变量
len_a = 2.0  # 正方形边长 = 2

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_a)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz2_4_1",
    "type": 8,
    "level": 1,
    "cn_problem": f"在边长为{len_a}的正方形{point_A}{point_B}{point_C}{point_D}中，{point_E},{point_F}分别为线段{point_A}{point_B},{point_B}{point_C}的中点，连接{point_D}{point_E},{point_D}{point_F},{point_E}{point_F}，将三角形{point_A}{point_D}{point_E},三角形{point_C}{point_D}{point_F},三角形{point_B}{point_E}{point_F}分别沿{point_D}{point_E},{point_D}{point_F},{point_E}{point_F}折起，使{point_A},{point_B},{point_C}三点重合，得到三棱锥{point_O}-{point_D}{point_E}{point_F}，求该三棱锥外接球的表面积。",
    "en_problem": f"In square {point_A}{point_B}{point_C}{point_D} with side length {len_a}, {point_E} and {point_F} are midpoints of segments {point_A}{point_B} and {point_B}{point_C} respectively. Connect {point_D}{point_E}, {point_D}{point_F}, {point_E}{point_F}, then fold triangles {point_A}{point_D}{point_E}, {point_C}{point_D}{point_F}, {point_B}{point_E}{point_F} along {point_D}{point_E}, {point_D}{point_F}, {point_E}{point_F} respectively, so that points {point_A}, {point_B}, {point_C} coincide to form triangular pyramid {point_O}-{point_D}{point_E}{point_F}. Find the surface area of the circumsphere of this triangular pyramid.",
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
    f.write(json.dumps({json_data["id"]: f"fz2_4_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_O}')"}, ensure_ascii=False) + "\n")
