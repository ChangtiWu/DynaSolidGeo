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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M, point_P = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
def calculate(len_a):
    """
    计算向量点积是否为定值

    参数:
    len_a (float): 棱长参数 AD

    返回:
    float: 点积的定值
    """
    # 根据题解，点积恒为 2 * len_a^2
    return 2 * len_a ** 2


# 定义题干中的参数
len_a = 1.0   # AD 的长度

# 验证计算结果
# result = calculate(len_a)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_23_1",
    "type": 7,
    "level": 1,
    "cn_problem": f"在长方体 {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1} 中，设 {point_A}{point_D} = {len_a}，{point_A}{point_A1} = {point_A}{point_B} = 2*{len_a}（{len_a} > 0），{point_M} 为棱 {point_D}{point_D1} 的中点。若 {point_P} 是线段 {point_B}{point_M} 上的动点，探究 \\(\\overrightarrow{{{point_A1}{point_M}}} \\cdot \\overrightarrow{{{point_A1}{point_P}}}\\) 是否为定值？若是，求出该定值；否则，请说明理由。",
    "en_problem": f"In the cuboid {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1}, let {point_A}{point_D} = {len_a}, {point_A}{point_A1} = {point_A}{point_B} = 2*{len_a} ({len_a} > 0), and {point_M} be the midpoint of edge {point_D}{point_D1}. If {point_P} is a moving point on segment {point_B}{point_M}, determine whether \\(\\overrightarrow{{{point_A1}{point_M}}} \\cdot \\overrightarrow{{{point_A1}{point_P}}}\\) is constant; if so, find its value.",
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
    f.write(json.dumps({json_data["id"]: f"area2_23_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_M}', '{point_P}')"}, ensure_ascii=False) + "\n")
