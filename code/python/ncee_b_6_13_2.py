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


def calculate(len_a, len_h):
    r"""
    计算最大正弦值 $\sin\theta_{\max} = \frac{\sqrt{{len_a}^{2}+{len_h}^{2}}}{\sqrt{2{len_a}^{2}+{len_h}^{2}}}$。

    参数:
    len_a (float): 长度参数（代表实际长度，建议为正数）
    len_h (float): 高度参数（代表实际长度，建议为正数）

    返回:
    float: 计算得到的 $\sin\theta_{\max}$ 值
    """
    # 计算分子：√(len_a² + len_h²)
    numerator = math.sqrt(len_a ** 2 + len_h ** 2)
    # 计算分母：√(2len_a² + len_h²)
    denominator = math.sqrt(2 * len_a ** 2 + len_h ** 2)
    # 计算正弦值
    sin_theta_max = numerator / denominator
    return sin_theta_max


len_a = 1.0
len_h = 1.0

# result1 = calculate(len_a, len_h)
# print(f"当 len_a={len_a}，len_h={len_h} 时，sinθ_max≈{result1:.4f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_13_2",
    "type": 2,
    "level": 3,
    "cn_problem": f"参数化设置：\n- 底面 {point_A}{point_B}{point_C}{point_D} 为边长 {len_a} (>0) 的正方形；\n- 侧棱 {point_P}{point_D} ⟂ 底面，且 {point_P}{point_D} = {len_h} (>0)，同时设 {point_A}{point_D} = {len_a}；\n- 交线 l = 平面 {point_P}{point_A}{point_D} ∩ 平面 {point_P}{point_B}{point_C}；取任意点 {point_Q}(m,0,{len_h})∈l；\n- 设 θ 为直线 {point_P}{point_B} 与平面 {point_Q}{point_C}{point_D} 所成锐角。\n求 sin θ 的最大值。",
    "en_problem": f"Parameterised version:\n- The base square {point_A}{point_B}{point_C}{point_D} has side {len_a} (>0);\n- Edge {point_P}{point_D} is perpendicular to the base with length {len_h} (>0) and {point_A}{point_D} = {len_a};\n- The intersection l of planes {point_P}{point_A}{point_D} and {point_P}{point_B}{point_C} is the set of points (m,0,{len_h}). Pick {point_Q} on l;\n- Let θ be the acute angle between line {point_P}{point_B} and plane {point_Q}{point_C}{point_D}.\nFind the maximum value of sin θ.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_13_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}', '{point_Q}')"}, ensure_ascii=False) + "\n")
