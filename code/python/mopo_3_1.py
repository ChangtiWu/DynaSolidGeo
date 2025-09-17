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
point_A, point_B, point_C, point_D, point_P = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_a, len_b, len_c):
    """计算len_L关于len_a、len_b、len_c的表达式"""
    # 计算第一部分：(len_a * len_b) / sqrt(len_a² + len_b²)
    part1 = (len_a * len_b) / math.sqrt(len_a ** 2 + len_b ** 2)

    # 计算反余弦函数的参数
    arccos_arg = (len_c - len_b) / (len_a ** 2 + len_b * len_c)
    # 计算π/2 - arccos(arccos_arg)
    part2 = math.pi / 2 - math.acos(arccos_arg)

    # 计算最终结果
    return part1 * part2


# 测试示例
len_a = 1.0
len_b = 1.0
len_c = 3.0

# print(calculate(len_a, len_b, len_c))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_3_1",
    "type": 8,
    "level": 2,
    "cn_problem": f"在 $\\triangle {point_A}{point_B}{point_C}$ 中，${point_A}{point_B} \\perp {point_B}{point_C}$，设 ${point_A}{point_B} = {len_a}$，${point_B}{point_D} = {len_b}$（{point_D} 为 ${point_B}{point_C}$ 上一点），${point_B}{point_C} = {len_c}$ 且 ${len_c} > {len_b}$。将 $\\triangle {point_A}{point_B}{point_D}$ 沿 ${point_A}{point_D}$ 翻折，使点 {point_B} 与点 {point_P} 重合，若点 {point_P} 在平面 ${point_A}{point_D}{point_C}$ 上的射影位于 $\\triangle {point_A}{point_D}{point_C}$ 内部及边界上，求动点 {point_P} 的轨迹长度。",
    "en_problem": f"In $\\triangle {point_A}{point_B}{point_C}$ where ${point_A}{point_B} \\perp {point_B}{point_C}$, let ${point_A}{point_B} = {len_a}$, ${point_B}{point_D} = {len_b}$ (where {point_D} is on ${point_B}{point_C}$), ${point_B}{point_C} = {len_c}$ with ${len_c} > {len_b}$. Fold $\\triangle {point_A}{point_B}{point_D}$ along ${point_A}{point_D}$ so that point {point_B} coincides with point {point_P}. If the projection of point {point_P} onto plane ${point_A}{point_D}{point_C}$ lies within $\\triangle {point_A}{point_D}{point_C}$ (including boundary), find the trajectory length of moving point {point_P}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_3_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}')"}, ensure_ascii=False) + "\n")
