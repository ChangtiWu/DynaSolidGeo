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
point_A, point_B, point_C, point_D, point_A1 = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math

def calculate(len_a, len_b):
    """
    计算四面体 A'BCD 的最小体积

    参数:
    len_a (float): 长度 AB
    len_b (float): 长度 AD

    返回:
    float: 四面体体积最小值
    """
    # 根据题干给出的解答公式: (len_a^2 * sqrt(len_b^2 - len_a^2)) / 6
    return (len_a ** 2 * math.sqrt(len_b ** 2 - len_a ** 2)) / 6


# 定义题干中的参数变量
len_a = 2.0  # AB = 2
len_b = 4.0  # AD = 4

# 验证计算结果（确认与参考答案一致后注释掉）
#result = calculate(len_a, len_b)
#print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_3_1",
    "type": 8,
    "level": 2,
    "cn_problem": f"在矩形{point_A}{point_B}{point_C}{point_D}中，设{point_A}{point_B} = {len_a}，{point_A}{point_D} = {len_b}（其中{len_a} > 0，{len_b} > 0且{len_b} > {len_a}），沿{point_B}{point_D}将△{point_A}{point_B}{point_D}折起至△{point_A1}{point_B}{point_D}的位置。若点{point_A1}在平面{point_B}{point_C}{point_D}上的射影落在△{point_B}{point_C}{point_D}的内部（包含边界），求四面体{point_A1}{point_B}{point_C}{point_D}体积的最小值。",
    "en_problem": f"In rectangle {point_A}{point_B}{point_C}{point_D}, let {point_A}{point_B} = {len_a}, {point_A}{point_D} = {len_b} (where {len_a} > 0, {len_b} > 0 and {len_b} > {len_a}). Triangle {point_A}{point_B}{point_D} is folded along {point_B}{point_D} to position △{point_A1}{point_B}{point_D}. If the projection of point {point_A1} onto plane {point_B}{point_C}{point_D} falls within triangle {point_B}{point_C}{point_D} (including boundary), find the minimum volume of tetrahedron {point_A1}{point_B}{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_3_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}')"}, ensure_ascii=False) + "\n")
