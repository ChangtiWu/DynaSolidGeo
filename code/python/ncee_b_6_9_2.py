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
point_A, point_B, point_C, point_D, point_P, point_Q = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate():
    r"""
    计算固定正弦值 $\sin\theta = \frac{\sqrt{6}}{3}$。

    返回:
    float: 固定正弦值（约0.8165）
    """
    # 计算分子：√6
    numerator = math.sqrt(6)
    # 计算分母：3
    denominator = 3
    # 计算正弦值
    sin_theta = numerator / denominator
    return sin_theta

len_k = 1.0

# result = calculate()
# print(f"sin_theta的值为：{result:.4f}")
# Generate random lengths
len_k = round(len_scaling_factor * float(len_k), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_9_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"把原题的全部度量统一放大/缩小一个比例系数 k (>0)：\n- 设底面正方形 {point_A}{point_B}{point_C}{point_D} 边长 {len_k}；\n- 侧棱 {point_P}{point_D} = {point_A}{point_D} = {len_k}，且 {point_P}{point_D} ⟂ 底面；\n- 平面 {point_P}{point_A}{point_D} 与平面 {point_P}{point_B}{point_C} 的交线记作 l；\n- 点 {point_Q} 在 l 上，满足 {point_Q}{point_B} = √2·{len_k}。\n设 θ 为直线 {point_P}{point_B} 与平面 {point_Q}{point_C}{point_D} 所成的锐角。求 sin θ。",
    "en_problem": f"Uniformly scale the original figure by a positive factor k (>0):\n- The base square {point_A}{point_B}{point_C}{point_D} has side {len_k};\n- Edges {point_P}{point_D} and {point_A}{point_D} both equal {len_k}, with {point_P}{point_D} ⟂ base ABCD;\n- Let l be the intersection of planes {point_P}{point_A}{point_D} and {point_P}{point_B}{point_C};\n- A point {point_Q} on l satisfies {point_Q}{point_B} = √2 {len_k}.\nLet θ be the acute angle between line {point_P}{point_B} and plane {point_Q}{point_C}{point_D}. Find sin θ.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_9_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}', '{point_Q}')"}, ensure_ascii=False) + "\n")
