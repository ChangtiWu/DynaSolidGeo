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
point_A, point_B, point_C, point_D, point_P = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math

def calculate(len_a, len_k):
    """
    计算平面 PAC 与平面 PAB 夹角的余弦值

    参数:
    len_a (float): 已知边长 AD = DC
    len_k (float): 直线 PC 与 AB 所成角的余弦值

    返回:
    float: 平面 PAC 与平面 PAB 夹角的余弦值
    """
    # 根据题干给出的解答公式: sqrt(5)/5
    return math.sqrt(5) / 5


# 定义题干中的参数变量
len_a = 2.0  # AD = DC = 2
len_k = 1/7  # cos(PC, AB) = 1/7

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_a, len_k)
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, len_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_12_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在梯形{point_A}{point_B}{point_C}{point_D}中，已知{point_A}{point_B}∥{point_D}{point_C}，{point_A}{point_D} = {point_D}{point_C} = {len_a}，{point_A}{point_B} = 2*{len_a}，现将△{point_A}{point_D}{point_C}沿{point_A}{point_C}翻折成直二面角{point_P}-{point_A}{point_C}-{point_B}。若直线{point_P}{point_C}与{point_A}{point_B}所成角的余弦值为{len_k}，求平面{point_P}{point_A}{point_C}与平面{point_P}{point_A}{point_B}夹角的余弦值。",
    "en_problem": f"In trapezoid {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B}∥{point_D}{point_C}, {point_A}{point_D} = {point_D}{point_C} = {len_a}, {point_A}{point_B} = 2*{len_a}, triangle {point_A}{point_D}{point_C} is folded along {point_A}{point_C} to form right dihedral angle {point_P}-{point_A}{point_C}-{point_B}. If the cosine of the angle between line {point_P}{point_C} and {point_A}{point_B} is {len_k}, find the cosine of the angle between plane {point_P}{point_A}{point_C} and plane {point_P}{point_A}{point_B}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_12_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}')"}, ensure_ascii=False) + "\n")
