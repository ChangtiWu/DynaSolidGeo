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
point_A, point_B, point_C, point_D, point_E, point_F, point_M, point_N = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate():
    r"""
    计算固定正弦值 $\sin\theta = \frac{5\sqrt{7}}{14}$。

    返回:
    float: 固定正弦值（约0.8452）
    """
    # 计算分子：5 * √7
    numerator = 5 * math.sqrt(7)
    # 计算分母：14
    denominator = 14
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
    "id": "ncee_b_6_6_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"设两直角梯形 {point_A}{point_B}{point_C}{point_D} 与 {point_C}{point_D}{point_E}{point_F} 满足比例 {point_A}{point_B}:{point_D}{point_C}:{point_E}{point_F} = 5:3:1，且 {point_A}{point_B} ∥ {point_D}{point_C} ∥ {point_E}{point_F}。已知 ∠{point_B}{point_A}{point_D} = ∠{point_C}{point_D}{point_E} = 60°，二面角 ({point_F}‑{point_D}{point_C}‑{point_B}) 的平面角为 60°。令整体缩放系数 {len_k}>0，使\n{point_A}{point_B}=5*{len_k},\n{point_D}{point_C}=3*{len_k},\n{point_E}{point_F}={len_k}。\n记 {point_M}、{point_N} 分别为 {point_A}{point_E}、{point_B}{point_C} 的中点。设 θ 为直线 {point_B}{point_M} 与平面 {point_A}{point_D}{point_E} 所成的锐角。求 sin θ。",
    "en_problem": f"The right‑angled trapezoids {point_A}{point_B}{point_C}{point_D} and {point_C}{point_D}{point_E}{point_F} satisfy {point_A}{point_B}:{point_D}{point_C}:{point_E}{point_F} = 5:3:1 with {point_A}{point_B} ∥ {point_D}{point_C} ∥ {point_E}{point_F}. Given ∠{point_B}{point_A}{point_D} = ∠{point_C}{point_D}{point_E} = 60° and the dihedral angle between planes ({point_F}‑{point_D}{point_C}) and ({point_B}‑{point_D}{point_B}) equals 60°. Introduce a global scale {len_k}>0 so that\n{point_A}{point_B} = 5*{len_k}, {point_D}{point_C} = 3*{len_k}, {point_E}{point_F} = {len_k}. Let {point_M} and {point_N} be the mid‑points of {point_A}{point_E} and {point_B}{point_C}, respectively. Let θ be the acute angle between line {point_B}{point_M} and plane {point_A}{point_D}{point_E}. Find sin θ (note: the value is independent of {len_k}).",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_6_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
