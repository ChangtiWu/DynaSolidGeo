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
point_A, point_B, point_C, point_D, point_E = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math

def calculate():
    """
    计算直线 AC 与平面 BCDE 所成角的正切值

    无参数输入（数值全在题干里固定）

    返回:
    float: 正切值
    """
    # 根据题干给出的解答公式: sqrt(7)/7
    return math.sqrt(7) / 7


# 题干中涉及的数值参数
len_k = 1.0  # 题干里的基本长度单位


# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate()
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_k = round(len_scaling_factor * float(len_k), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_15_3",
    "type": 8,
    "level": 2,
    "cn_problem": f"在五边形{point_A}{point_B}{point_C}{point_D}{point_E}中，设{point_A}{point_B} = √5*{len_k}，{point_B}{point_C} = {point_C}{point_D} = {len_k}（{len_k} > 0为参数），∠{point_B}{point_C}{point_D} = ∠{point_C}{point_D}{point_E} = 2π/3，{point_B}{point_E} = 2√3*{len_k}，△{point_A}{point_B}{point_E}的面积为√6*{len_k}^2。将五边形{point_A}{point_B}{point_C}{point_D}{point_E}沿{point_B}{point_E}向内翻折得到四棱锥{point_A}-{point_B}{point_C}{point_D}{point_E}，当二面角{point_A}-{point_B}{point_E}-{point_C}的大小为135°时，求直线{point_A}{point_C}与平面{point_B}{point_C}{point_D}{point_E}所成角的正切值。",
    "en_problem": f"In pentagon {point_A}{point_B}{point_C}{point_D}{point_E}, let {point_A}{point_B} = √5*{len_k}, {point_B}{point_C} = {point_C}{point_D} = {len_k} ({len_k} > 0 as parameter), ∠{point_B}{point_C}{point_D} = ∠{point_C}{point_D}{point_E} = 2π/3, {point_B}{point_E} = 2√3*{len_k}, area of triangle {point_A}{point_B}{point_E} is √6*{len_k}^2. Fold pentagon {point_A}{point_B}{point_C}{point_D}{point_E} inward along {point_B}{point_E} to form pyramid {point_A}-{point_B}{point_C}{point_D}{point_E}. When the dihedral angle {point_A}-{point_B}{point_E}-{point_C} is 135°, find the tangent of the angle between line {point_A}{point_C} and plane {point_B}{point_C}{point_D}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_15_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
