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
point_A, point_B, point_C, point_D, point_N, point_M, point_E = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_a, len_h, arg_alpha):
    """
    计算给定的几何表达式

    参数:
    len_a (float): 菱形边长
    len_h (float): AM 的长度
    arg_alpha (float): ∠DAB 的角度（弧度制）

    返回:
    float: 计算结果
    """
    numerator = len_a * len_h * math.sin(arg_alpha)
    denominator = math.sqrt((len_a ** 2 + 4 * (len_h ** 2)) * (len_h ** 2 + (len_a ** 2) * (math.sin(arg_alpha) ** 2)))
    result = numerator / denominator
    return result


# 定义题干参数
len_a = 4.0
len_h = 2.0
arg_alpha = math.pi / 3

# 验证输出（与参考答案对比）
# result = calculate(len_a, len_h, arg_alpha)
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h, arg_alpha)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_12_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"设菱形{point_A}{point_B}{point_C}{point_D}的边长为{len_a}，∠{point_D}{point_A}{point_B}={arg_alpha}，矩形{point_A}{point_D}{point_N}{point_M}中{point_A}{point_M}={len_h}（故{point_D}{point_N}={len_h}，且{point_A}{point_M}⊥平面{point_A}{point_B}{point_C}{point_D}，因平面{point_A}{point_D}{point_N}{point_M}⊥平面{point_A}{point_B}{point_C}{point_D}，交线为{point_A}{point_D}），{point_E}为{point_A}{point_B}中点。求{point_M}{point_E}与平面{point_M}{point_B}{point_C}所成角的正弦值。",
    "en_problem": f"Let rhombus {point_A}{point_B}{point_C}{point_D} have side length {len_a}, ∠{point_D}{point_A}{point_B}={arg_alpha}, and in rectangle {point_A}{point_D}{point_N}{point_M}, {point_A}{point_M}={len_h} (so {point_D}{point_N}={len_h}, and {point_A}{point_M}⊥plane {point_A}{point_B}{point_C}{point_D}, since plane {point_A}{point_D}{point_N}{point_M}⊥plane {point_A}{point_B}{point_C}{point_D} with intersection line {point_A}{point_D}), {point_E} is the midpoint of {point_A}{point_B}. Find the sine of the angle between {point_M}{point_E} and plane {point_M}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"sup_12_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_N}', '{point_M}', '{point_E}')"}, ensure_ascii=False) + "\n")
