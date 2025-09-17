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
point_P, point_A, point_B, point_C, point_D, point_O = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
def calculate(len_a):
    """
    计算四棱锥 P-ABCD 的最大体积

    参数:
    len_a (float): PO + AB 的和

    返回:
    float: 最大体积 V_max
    """
    # 根据题目解法公式 V_max = 4 * len_a^3 / 81
    return 4 * (len_a ** 3) / 81


# 定义题干中的参数
len_a = 4.0  # PO + AB

# 验证计算结果
# result = calculate(len_a)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_24_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"在四棱锥 {point_P} - {point_A}{point_B}{point_C}{point_D} 中，底面 {point_A}{point_B}{point_C}{point_D} 为正方形，{point_P}{point_A} = {point_P}{point_D}，{point_O} 为 {point_A}{point_D} 中点，{point_P}{point_O} ⊥ 平面 {point_A}{point_B}{point_C}{point_D}，且 {point_P}{point_O} + {point_A}{point_B} = {len_a}（{len_a} > 0）。求四棱锥体积的最大值。",
    "en_problem": f"In the quadrilateral pyramid {point_P} - {point_A}{point_B}{point_C}{point_D}, the base {point_A}{point_B}{point_C}{point_D} is a square, {point_P}{point_A} = {point_P}{point_D}, {point_O} is the midpoint of {point_A}{point_D}, {point_P}{point_O} ⊥ plane {point_A}{point_B}{point_C}{point_D}, and {point_P}{point_O} + {point_A}{point_B} = {len_a} ({len_a} > 0). Find the maximum volume of the pyramid.",
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
    f.write(json.dumps({json_data["id"]: f"area2_24_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}')"}, ensure_ascii=False) + "\n")
