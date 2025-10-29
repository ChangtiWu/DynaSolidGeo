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
point_P, point_A, point_B, point_C, point_D, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_a, len_b, len_h):
    """
    计算给定的几何表达式

    参数:
    len_a (float): AD 的长度
    len_b (float): AB 的长度
    len_h (float): PA 的长度

    返回:
    float: 二面角余弦值
    """
    # 根据题干解法，cosθ = (len_b * len_h) / sqrt((len_a^2 + len_h^2) * (len_a^2 + len_b^2))
    numerator = len_b * len_h
    denominator = math.sqrt((len_a ** 2 + len_h ** 2) * (len_a ** 2 + len_b ** 2))
    result = numerator / denominator
    return result


# 定义题干参数
len_a = 2.0
len_b = 2 * math.sqrt(2)
len_h = math.sqrt(3)

# 验证输出（与参考答案对比）
# result = calculate(len_a, len_b, len_h)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_b, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_17_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"已知四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}，底面{point_A}{point_B}{point_C}{point_D}为矩形，设{point_A}{point_D}={len_a}，{point_A}{point_B}={len_b}，{point_P}{point_A}={len_h}，{point_E}为{point_C}{point_D}中点，满足：{point_P}{point_A}⊥{point_B}{point_D}；{point_A}{point_E}^2+{point_P}{point_A}^2={point_P}{point_E}^2（即{len_a}^2+(\\frac{{{len_b}}}{{2}})^2+{len_h}^2= len_m^2， len_m  为{point_P}{point_E}长度，保证{point_P}{point_A}⊥{point_A}{point_E}）。求二面角{point_D}-{point_P}{point_C}-{point_A}的余弦值。",
    "en_problem": f"Given quadrilateral pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, base {point_A}{point_B}{point_C}{point_D} is a rectangle, let {point_A}{point_D}={len_a}, {point_A}{point_B}={len_b}, {point_P}{point_A}={len_h}, {point_E} is the midpoint of {point_C}{point_D}, satisfying: {point_P}{point_A}⊥{point_B}{point_D}; {point_A}{point_E}^2+{point_P}{point_A}^2={point_P}{point_E}^2 (i.e., {len_a}^2+(\\frac{{{len_b}}}{{2}})^2+{len_h}^2= len_m^2, where  len_m   is the length of {point_P}{point_E}, ensuring {point_P}{point_A}⊥{point_A}{point_E}). Find the cosine of dihedral angle {point_D}-{point_P}{point_C}-{point_A}.",
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
    f.write(json.dumps({json_data["id"]: f"sup_17_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
