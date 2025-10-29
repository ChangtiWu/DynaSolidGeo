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
point_P, point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_a, len_b, lam):
    """
    计算给定的几何表达式

    参数:
    len_a (float): PA = AB = BC 的长度
    len_b (float): AD 的长度
    lam (float): λ，0 < λ < 1

    返回:
    float: 计算结果
    """
    # 根据题干解法，d = len_b * (1 - λ) / sqrt(2 + (len_b^2)/(len_a^2))
    result = len_b * (1 - lam) / math.sqrt(2 + (len_b ** 2) / (len_a ** 2))
    return result


# 定义题干参数
len_a = 2.0
len_b = 4.0
lam = 1/4

# 验证输出（与参考答案对比）
# result = calculate(len_a, len_b, lam)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b, lam)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_16_2",
    "type": 3,
    "level": 2,
    "cn_problem": f"在四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}中，{point_P}{point_A}⊥底面{point_A}{point_B}{point_C}{point_D}，{point_A}{point_B}⊥{point_A}{point_D}，{point_B}{point_C}∥{point_A}{point_D}，{point_P}{point_A}={point_A}{point_B}={point_B}{point_C}={len_a}，{point_A}{point_D}={len_b}，{point_E}为棱{point_P}{point_D}的中点，{point_P}{point_F}=λ{point_P}{point_C}（λ=0.25为常数且0<λ<1）。求点{point_F}到平面{point_A}{point_E}{point_C}的距离。",
    "en_problem": f"In quadrilateral pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, {point_P}{point_A}⊥base {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B}⊥{point_A}{point_D}, {point_B}{point_C}∥{point_A}{point_D}, {point_P}{point_A}={point_A}{point_B}={point_B}{point_C}={len_a}, {point_A}{point_D}={len_b}, {point_E} is the midpoint of edge {point_P}{point_D}, {point_P}{point_F}=λ{point_P}{point_C} (where λ=0.25 is a constant with 0<λ<1). Find the distance from point {point_F} to plane {point_A}{point_E}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"sup_16_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
