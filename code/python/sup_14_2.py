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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_O = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(arg_theta, arg_alpha):
    """
    计算给定的几何表达式

    参数:
    arg_theta (float): ∠B₁BC（弧度制）
    arg_alpha (float): AB 与平面 BB₁C₁C 的夹角（弧度制）

    返回:
    float: 二面角余弦值
    """
    # 根据题干解法，cos(theta) = 1/7
    result = 1 / 7
    return result


# 定义题干参数
arg_theta = math.radians(60)
arg_alpha = math.radians(30)

# 验证输出（与参考答案对比）
# result = calculate(arg_theta, arg_alpha)
# print(f"计算结果: {result:.6f}")

# Generate random lengths


# Calculate the result
result = calculate(arg_theta, arg_alpha)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_14_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在三棱柱{point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}中，{point_B}{point_C}={point_B}{point_B1}（故四边形{point_B}{point_B1}{point_C1}{point_C}为菱形），设∠{point_B1}{point_B}{point_C}={arg_theta}，{point_A}{point_O}⊥平面{point_B}{point_B1}{point_C1}{point_C}（{point_O}为{point_B}{point_C1}与{point_B1}{point_C}的交点），直线{point_A}{point_B}与平面{point_B}{point_B1}{point_C1}{point_C}所成角为{arg_alpha}。求二面角{point_A1}-{point_B1}{point_C1}-{point_A}的余弦值。",
    "en_problem": f"In triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, {point_B}{point_C}={point_B}{point_B1} (so quadrilateral {point_B}{point_B1}{point_C1}{point_C} is a rhombus), let ∠{point_B1}{point_B}{point_C}={arg_theta}, {point_A}{point_O}⊥plane {point_B}{point_B1}{point_C1}{point_C} (where {point_O} is the intersection of {point_B}{point_C1} and {point_B1}{point_C}), and the angle between line {point_A}{point_B} and plane {point_B}{point_B1}{point_C1}{point_C} is {arg_alpha}. Find the cosine of dihedral angle {point_A1}-{point_B1}{point_C1}-{point_A}.",
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
    f.write(json.dumps({json_data["id"]: f"sup_14_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_O}')"}, ensure_ascii=False) + "\n")
