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
point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate():
    r"""
    计算固定正弦值 $\sin\theta = \frac{\sqrt{3}}{3}$。

    返回:
    float: 固定正弦值（约0.5774）
    """
    # 计算分子：√3
    numerator = math.sqrt(3)
    # 计算分母：3
    denominator = 3
    # 计算正弦值
    sin_theta = numerator / denominator
    return sin_theta


len_b = 1.0  # 原题中BC的长度，任意正数

# result = calculate()
# print(f"sin_theta的值为：{result:.4f}")

# Generate random lengths
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_12_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在三棱台 {point_A}{point_B}{point_C}-{point_D}{point_E}{point_F} 中，引入一个统一缩放参数 {len_b} (>0)：\n- 设 {point_B}{point_C} = {len_b}，{point_D}{point_C} = 2*{len_b}；\n- 保持 ∠{point_A}{point_C}{point_B} = ∠{point_A}{point_C}{point_D} = 45°，且平面 {point_A}{point_C}{point_F}{point_D} ⟂ 平面 {point_A}{point_B}{point_C}；\n- 其它比例、垂直、平行关系与原题一致（特别地，{point_A}{point_B}{point_C}{point_D} 为同顶点外接的平行四边形）。\n设 θ 为直线 {point_D}{point_F} 与平面 {point_D}{point_B}{point_C} 所成的锐角。求 sin θ。",
    "en_problem": f"In the truncated triangular pyramid {point_A}{point_B}{point_C}-{point_D}{point_E}{point_F}, introduce a global scale {len_b} (>0):\n- Let {point_B}{point_C} = {len_b} and {point_D}{point_C} = 2*{len_b};\n- Keep ∠{point_A}{point_C}{point_B} = ∠{point_A}{point_C}{point_D} = 45°, with plane {point_A}{point_C}{point_F}{point_D} perpendicular to the base plane {point_A}{point_B}{point_C};\n- All other geometric relations (parallelism, perpendicularity) remain as in the original statement.\nLet θ be the acute angle between line {point_D}{point_F} and plane {point_D}{point_B}{point_C}. Find sin θ .",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_12_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
