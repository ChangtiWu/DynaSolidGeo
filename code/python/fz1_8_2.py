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
point_A, point_A1, point_B1, point_B, point_C, point_M, point_C1, point_D = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math

def calculate(len_a, len_b, len_c):
    """
    计算平面 ABB₁M 与平面 B₁CD 所成锐二面角的余弦值

    参数:
    len_a (float): AC 的长度
    len_b (float): CB 的长度
    len_c (float): AA₁ 的长度

    返回:
    float: 二面角的余弦值
    """
    numerator = abs(len_b ** 2 - len_a ** 2) * len_c
    denominator = math.sqrt(len_a ** 2 + len_b ** 2) * math.sqrt(len_c ** 2 * (len_a ** 2 + len_b ** 2) + (len_a ** 2) * (len_b ** 2))
    return numerator / denominator


# 定义题干中的参数变量
len_a = 2.0  # AC 的长度
len_b = 4.0  # CB 的长度
len_c = 4.0  # AA₁ 的长度
len_d = 2.0  # A₁M 的长度
# 验证计算结果（确认与参考答案一致后注释掉）
#result = calculate(len_a, len_b, len_c)
#print(f"计算结果: {result:.6f}")


# Generate random lengths
len_c = round(len_scaling_factor * float(len_c), 2)
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_d = round(len_scaling_factor * float(len_d), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_8_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在矩形{point_A}{point_A1}{point_B1}{point_B}中，设{point_A}{point_A1} = {len_c}，{point_A}{point_B} = {len_a} + {len_b}（其中{point_A}{point_C} = {len_a}，{point_C}{point_B} = {len_b}），点{point_M}, {point_C1}分别在{point_A}{point_A1}, {point_A1}{point_B1}上，且{point_A1}{point_M} = {len_d}，{point_A1}{point_C1} = {len_a}。过{point_C1}作{point_C1}{point_C}⊥{point_A}{point_B}于{point_C}，将△{point_A1}{point_M}{point_C1}剪掉后，把四边形{point_A}{point_C}{point_C1}{point_M}沿{point_C1}{point_C}折叠，使{point_A}{point_C}⊥{point_B}{point_C}。连接{point_A}{point_B}，取{point_A}{point_B}中点{point_D}，连接{point_C}{point_D}, {point_B1}{point_C}, {point_B1}{point_D}, {point_B1}{point_M}。求平面{point_A}{point_B}{point_B1}{point_M}与平面{point_B1}{point_C}{point_D}所成锐二面角的余弦值。",
    "en_problem": f"In rectangle {point_A}{point_A1}{point_B1}{point_B}, let {point_A}{point_A1} = {len_c}, {point_A}{point_B} = {len_a} + {len_b} (where {point_A}{point_C} = {len_a}, {point_C}{point_B} = {len_b}), points {point_M}, {point_C1} are on {point_A}{point_A1}, {point_A1}{point_B1} respectively, with {point_A1}{point_M} = {len_d}, {point_A1}{point_C1} = {len_a}. Through {point_C1}, draw {point_C1}{point_C}⊥{point_A}{point_B} at {point_C}, cut away triangle {point_A1}{point_M}{point_C1}, then fold quadrilateral {point_A}{point_C}{point_C1}{point_M} along {point_C1}{point_C} so that {point_A}{point_C}⊥{point_B}{point_C}. Connect {point_A}{point_B}, take midpoint {point_D} of {point_A}{point_B}, connect {point_C}{point_D}, {point_B1}{point_C}, {point_B1}{point_D}, {point_B1}{point_M}. Find the cosine of the acute dihedral angle between plane {point_A}{point_B}{point_B1}{point_M} and plane {point_B1}{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_8_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_A1}', '{point_B1}', '{point_B}', '{point_C}', '{point_M}', '{point_C1}', '{point_D}')"}, ensure_ascii=False) + "\n")
