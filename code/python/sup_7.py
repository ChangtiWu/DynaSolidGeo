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
point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math


def calculate(len_a, len_b):
    """
    计算给定的几何表达式

    参数:
    len_a (float): AB 的长度
    len_b (float): AC = BC 的长度

    返回:
    float: 计算结果
    """
    # 根据题干解法，CD = sqrt(len_b^2 + (len_a^2)/2)
    result = math.sqrt((len_b ** 2) + (len_a ** 2) / 2)
    return result


# 定义题干参数
len_a = 2.0
len_b = math.sqrt(2)

# 验证输出（与参考答案对比）
#result = calculate(len_a, len_b)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_7",
    "type": 3,
    "level": 1,
    "cn_problem": f"已知空间四点{point_A}，{point_B}，{point_C}，{point_D}，在△{point_A}{point_B}{point_C}中，{point_A}{point_B}={len_a}，{point_A}{point_C}={point_B}{point_C}={len_b}，等边三角形{point_A}{point_D}{point_B}以{point_A}{point_B}为轴旋转，当平面{point_A}{point_D}{point_B}⊥平面{point_A}{point_B}{point_C}时，求线段{point_C}{point_D}的长度。",
    "en_problem": f"Given four points {point_A}, {point_B}, {point_C}, {point_D} in space, in △{point_A}{point_B}{point_C}, {point_A}{point_B}={len_a}, {point_A}{point_C}={point_B}{point_C}={len_b}, and equilateral triangle {point_A}{point_D}{point_B} rotates about axis {point_A}{point_B}. When plane {point_A}{point_D}{point_B}⊥plane {point_A}{point_B}{point_C}, find the length of segment {point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"sup_7({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
