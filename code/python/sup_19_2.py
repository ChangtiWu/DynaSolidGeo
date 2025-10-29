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


def calculate(arg_theta):
    """
    计算给定的几何表达式

    参数:
    arg_theta (float): 直线与平面夹角（弧度制）

    返回:
    float: 二面角的余弦值
    """
    # 根据题干解法，cos φ = tan(arg_theta) / sqrt(5 * tan^2(arg_theta) + 1)
    tan_theta = math.tan(arg_theta)
    result = tan_theta / math.sqrt(5 * (tan_theta ** 2) + 1)
    return result


# 定义题干参数
arg_theta = math.radians(60)
len_a = 1
len_b = 2
# 验证输出（与参考答案对比）
# result = calculate(arg_theta)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_b = round(len_scaling_factor * float(len_b), 2)
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_19_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"已知多面体{point_A}{point_B}{point_C}{point_D}{point_E}中，{point_D}{point_E}∥{point_A}{point_B}，{point_A}{point_C}⊥{point_B}{point_C}，{point_B}{point_C}=2*{point_A}{point_C}={len_b}（即{point_A}{point_C}={len_a}，{point_B}{point_C}=2*{len_a}），{point_A}{point_B}=2*{point_D}{point_E}，{point_D}{point_A}={point_D}{point_C}且平面{point_D}{point_A}{point_C}⊥平面{point_A}{point_B}{point_C}。直线{point_B}{point_E}与平面{point_A}{point_B}{point_C}所成的角为{arg_theta}，求二面角{point_B}-{point_A}{point_D}-{point_C}的余弦值。",
    "en_problem": f"In polyhedron {point_A}{point_B}{point_C}{point_D}{point_E}, {point_D}{point_E}∥{point_A}{point_B}, {point_A}{point_C}⊥{point_B}{point_C}, {point_B}{point_C}=2*{point_A}{point_C}={len_b} (i.e., {point_A}{point_C}={len_a}, {point_B}{point_C}=2*{len_a}), {point_A}{point_B}=2*{point_D}{point_E}, {point_D}{point_A}={point_D}{point_C} and plane {point_D}{point_A}{point_C}⊥plane {point_A}{point_B}{point_C}. The angle between line {point_B}{point_E} and plane {point_A}{point_B}{point_C} is {arg_theta}. Find the cosine of dihedral angle {point_B}-{point_A}{point_D}-{point_C}.",
    "solution": f"{result}",
    "image": f"images/{os.path.splitext(os.path.basename(__file__))[0]}.png"
}

# video mode
if args.mode == 1:
    json_data["image"] = f"videos/{os.path.splitext(os.path.basename(__file__))[0]}.mp4"



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
    f.write(json.dumps({json_data["id"]: f"sup_19_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
