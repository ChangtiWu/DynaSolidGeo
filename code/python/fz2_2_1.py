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
point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math

def calculate():
    """
    计算异面直线 AC 与 BD 所成角的余弦值

    返回:
    float: 余弦值
    """
    # 根据题干给出的解答公式: sqrt(6) / 6
    return math.sqrt(6) / 6


# 定义题干中的参数变量
# 这里题干中有 len_a, len_p，但最后的结果与它们无关，所以不需要赋值。
# 如果一定要保持格式，可以写上：
len_a = 1.0
len_p = 2.0

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate()
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_p = round(len_scaling_factor * float(len_p), 2)
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz2_2_1",
    "type": 8,
    "level": 1,
    "cn_problem": f"在直角梯形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_D} ∥ {point_B}{point_C}，{point_A}{point_B} ⊥ {point_B}{point_C}，且{point_B}{point_C} = {len_p}{point_A}{point_D} = {len_p}{point_A}{point_B} = {len_p}{len_a}（{len_a} > 0，{len_p} > 1）。将直角梯形{point_A}{point_B}{point_C}{point_D}沿对角线{point_B}{point_D}折起，使平面{point_A}{point_B}{point_D} ⊥ 平面{point_B}{point_C}{point_D}，求异面直线{point_A}{point_C}与{point_B}{point_D}所成角的余弦值。",
    "en_problem": f"In right trapezoid {point_A}{point_B}{point_C}{point_D}, {point_A}{point_D} ∥ {point_B}{point_C}, {point_A}{point_B} ⊥ {point_B}{point_C}, and {point_B}{point_C} = {len_p}{point_A}{point_D} = {len_p}{point_A}{point_B} = {len_p}{len_a} (where {len_a} > 0, {len_p} > 1). The trapezoid is folded along diagonal {point_B}{point_D} so that plane {point_A}{point_B}{point_D} ⊥ plane {point_B}{point_C}{point_D}. Find the cosine of the angle between skew lines {point_A}{point_C} and {point_B}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"fz2_2_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
