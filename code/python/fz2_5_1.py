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
point_A, point_B, point_C, point_D, point_E, point_F, point_P = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_a, len_b):
    """
    计算二面角 A - BE - P 的余弦值

    参数:
    len_a (float): 矩形边长比例参数
    len_b (float): PF 长度

    返回:
    float: 二面角余弦值
    """
    # 根据题干给出的解答公式: 1 - (len_b^2 / len_a^2)
    return 1 - (len_b ** 2) / (len_a ** 2)


# 定义题干中的参数变量
len_a = 2.0  # 由 AB = 2*BC 给出比例时可设 BC = len_a，AB = 2*len_a
len_b = 1.0  # PF = 1/2，这里可按题干设为 1.0 以便验证
len_p = 2.0
# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_a, len_b)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_p = round(len_scaling_factor * float(len_p), 2)
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz2_5_1",
    "type": 8,
    "level": 1,
    "cn_problem": f"在矩形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_B} = {len_p}{point_B}{point_C} = {len_p}*{len_a}（{len_a} > 0，{len_p} > 1），{point_E}是{point_C}{point_D}的中点，{point_F}是{point_A}{point_B}的中点。将三角形{point_B}{point_C}{point_E}沿{point_B}{point_E}翻折到三角形{point_P}{point_B}{point_E}的位置，连接{point_A}{point_P}，{point_D}{point_P}。当{point_P}{point_F} = {len_b}（{len_b} > 0，且满足{len_a}^2 > {len_b}^2）时，求二面角{point_A} - {point_B}{point_E} - {point_P}的余弦值。",
    "en_problem": f"In rectangle {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B} = {len_p}{point_B}{point_C} = {len_p}*{len_a} (where {len_a} > 0, {len_p} > 1), {point_E} is the midpoint of {point_C}{point_D}, and {point_F} is the midpoint of {point_A}{point_B}. Triangle {point_B}{point_C}{point_E} is folded along {point_B}{point_E} to the position of triangle {point_P}{point_B}{point_E}, connecting {point_A}{point_P} and {point_D}{point_P}. When {point_P}{point_F} = {len_b} (where {len_b} > 0 and {len_a}^2 > {len_b}^2), find the cosine of dihedral angle {point_A} - {point_B}{point_E} - {point_P}.",
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
    f.write(json.dumps({json_data["id"]: f"fz2_5_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_P}')"}, ensure_ascii=False) + "\n")
