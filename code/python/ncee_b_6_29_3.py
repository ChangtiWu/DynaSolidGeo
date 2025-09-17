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
point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_AD, len_AB, len_DE, len_AE):
    """计算param_sin的值（公式：(len_AD/len_AB) * √[1 - ((len_AD²+len_DE²-len_AE²)/(2len_AD len_DE))²]）"""
    # 计算分数部分的分子和分母
    fraction_numerator = len_AD ** 2 + len_DE ** 2 - len_AE ** 2
    fraction_denominator = 2 * len_AD * len_DE
    # 计算分数值的平方
    fraction_squared = (fraction_numerator / fraction_denominator) ** 2
    # 计算平方根内的部分
    sqrt_inner = 1 - fraction_squared
    # 计算平方根项
    sqrt_term = math.sqrt(sqrt_inner)
    # 计算最终结果
    return (len_AD / len_AB) * sqrt_term


# 测试示例
len_AD = 1.0
len_AB = 2.0
len_DE = 3.0
len_AE = math.sqrt(6)
len_EF = 1.0
# print(calculate(len_AD, len_AB, len_DE, len_AE))

# Generate random lengths
len_AB = round(len_scaling_factor * float(len_AB), 2)
len_AD = round(len_scaling_factor * float(len_AD), 2)

len_AE = round(len_scaling_factor * float(len_AE), 2)
len_DE = round(len_scaling_factor * float(len_DE), 2)
len_EF = round(len_scaling_factor * float(len_EF), 2)


# Calculate the result
result = calculate(len_AD, len_AB, len_DE, len_AE)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_29_3",
    "type": 2,
    "level": 2,
    "cn_problem": f"如图，在平行四边形 {point_A}{point_B}{point_C}{point_D} 中，设 {point_A}{point_B}={len_AB}>0，{point_A}{point_D}={len_AD}>0，且 ∠{point_B}{point_A}{point_D}=60°；取平面 {point_A}{point_E}{point_D}，满足平面 {point_A}{point_E}{point_D} ⊥ 平面 {point_A}{point_B}{point_C}{point_D}；已知 {point_A}{point_E}={len_AE}>0，{point_D}{point_E}={len_DE}>0；在平面 {point_A}{point_E}{point_D} 外取点 {point_F}，使 {point_E}{point_F} ∥ {point_A}{point_B}（记 {point_E}{point_F}={len_EF}>0）。求直线 {point_E}{point_F} 与平面 {point_B}{point_E}{point_D} 所成角的正弦值。",
    "en_problem": f"As shown, in parallelogram {point_A}{point_B}{point_C}{point_D}, let {point_A}{point_B}={len_AB}>0, {point_A}{point_D}={len_AD}>0, and ∠{point_B}{point_A}{point_D}=60°; take plane {point_A}{point_E}{point_D} such that plane {point_A}{point_E}{point_D} ⊥ plane {point_A}{point_B}{point_C}{point_D}; given {point_A}{point_E}={len_AE}>0, {point_D}{point_E}={len_DE}>0; outside plane {point_A}{point_E}{point_D}, take point {point_F} such that {point_E}{point_F} ∥ {point_A}{point_B} (denote {point_E}{point_F}={len_EF}>0). Find the sine of the angle between line {point_E}{point_F} and plane {point_B}{point_E}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_29_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
