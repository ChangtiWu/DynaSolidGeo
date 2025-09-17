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
point_P, point_A, point_B, point_C, point_D, point_T, point_M = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_m, len_n, lambda_):
    """
    计算四棱锥中直线 CD 与平面 ABM 所成角的正弦值

    参数:
    len_m (float): AB 和 BC 的长度
    len_n (float): AD / 2 的长度
    lambda_ (float): 点 M 在线段 PT 上的比例系数 λ

    返回:
    float: 线面角的正弦值
    """
    # 分子
    numerator = abs(len_m * (2 * len_n - len_m) * (1 - lambda_))

    # 分母
    denom_line = math.sqrt(len_m**2 + (2 * len_n - len_m)**2)
    denom_plane = math.sqrt((len_m * (1 - lambda_))**2 + (lambda_ * (len_m + 2 * len_n) / 2)**2)
    denominator = denom_line * denom_plane

    return numerator / denominator


# 定义题干中的参数
len_m = 1.0   # AB = BC = PA
len_n = 1.0   # AD / 2
len_d = (3 * math.sqrt(13)) / 13
lambda_ = 0.5 # 示例 λ 值，可替换为题目给定数值

# 验证计算结果
#result = calculate(len_m, len_n, lambda_)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)
len_n = round(len_scaling_factor * float(len_n), 2)
len_d = round(len_scaling_factor * float(len_d), 2)

# Calculate the result
result = calculate(len_m, len_n, lambda_)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_16_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在四棱锥 {point_P} - {point_A}{point_B}{point_C}{point_D} 中，四边形 {point_A}{point_B}{point_C}{point_D} 是梯形，{point_A}{point_D} ⊥ {point_A}{point_B}，{point_B}{point_C} ∥ {point_A}{point_D}，{point_P}{point_A} ⊥ {point_A}{point_B}，平面 {point_P}{point_A}{point_C} ⊥ 平面 {point_A}{point_B}{point_C}{point_D}。设 {point_A}{point_B} = {len_m}，{point_B}{point_C} = {len_m}，{point_A}{point_D} = 2*{len_n}，{point_P}{point_A} = {len_m}；点 {point_T} 是 {point_C}{point_D} 的中点，点 {point_M} 在线段 {point_P}{point_T} 上且满足 $\\overrightarrow{{{point_P}{point_M}}} = \\lambda \\overrightarrow{{{point_P}{point_T}}}$（0 ≤ λ=0.5 ≤ 1），已知点 {point_P} 到平面 {point_A}{point_B}{point_M} 的距离为 {len_d}。求直线 {point_C}{point_D} 与平面 {point_A}{point_B}{point_M} 所成角的正弦值。",
    "en_problem": f"In pyramid {point_P} - {point_A}{point_B}{point_C}{point_D}, quadrilateral {point_A}{point_B}{point_C}{point_D} is a trapezoid with {point_A}{point_D} ⊥ {point_A}{point_B}, {point_B}{point_C} ∥ {point_A}{point_D}, {point_P}{point_A} ⊥ {point_A}{point_B}, and plane {point_P}{point_A}{point_C} ⊥ plane {point_A}{point_B}{point_C}{point_D}. Let {point_A}{point_B} = {len_m}, {point_B}{point_C} = {len_m}, {point_A}{point_D} = 2*{len_n}, {point_P}{point_A} = {len_m}; point {point_T} is the midpoint of {point_C}{point_D}, point {point_M} is on segment {point_P}{point_T} satisfying $\\overrightarrow{{{point_P}{point_M}}} = \\lambda \\overrightarrow{{{point_P}{point_T}}}$ (0 ≤ λ=0.5 ≤ 1), and the distance from point {point_P} to plane {point_A}{point_B}{point_M} is {len_d}. Find the sine of the angle between line {point_C}{point_D} and plane {point_A}{point_B}{point_M}.",
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
    f.write(json.dumps({json_data["id"]: f"area2_16_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_T}', '{point_M}')"}, ensure_ascii=False) + "\n")
