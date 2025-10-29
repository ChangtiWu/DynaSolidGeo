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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1 = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(ang_theta, len_a, len_h):
    """计算param_sin的值（公式：[sinθ·√(len_a²+len_h²)] / √[len_a²sin²θ + 2len_h²(1-cosθ)]）"""
    # 计算分子部分：sin(ang_theta) * √(len_a² + len_h²)
    sin_theta = math.sin(ang_theta)
    sqrt_term_numerator = math.sqrt(len_a ** 2 + len_h ** 2)
    numerator = sin_theta * sqrt_term_numerator

    # 计算分母部分：√[len_a²sin²θ + 2len_h²(1 - cosθ)]
    sin_sq_theta = sin_theta ** 2
    cos_theta = math.cos(ang_theta)
    term1 = len_a ** 2 * sin_sq_theta
    term2 = 2 * len_h ** 2 * (1 - cos_theta)
    sqrt_term_denominator = math.sqrt(term1 + term2)

    # 计算最终结果
    return numerator / sqrt_term_denominator


# 测试示例
ang_theta = math.pi / 3 * 2
len_a = 2.0
len_h = math.sqrt(3)

# print(calculate(ang_theta, len_a, len_h))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)


# Calculate the result
result = calculate(ang_theta, len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_29_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"如图，已知平行六面体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 满足：(1) 底面 {point_A}{point_B}{point_C}{point_D} 为菱形，且 {point_A}{point_B}={point_A}{point_D}={len_a}>0，∠{point_B}{point_A}{point_D}={ang_theta}（0<{ang_theta}<π）；(2) 侧棱 {point_A}{point_A1} 垂直于底面 {point_A}{point_B}{point_C}{point_D}，且 {point_A}{point_A1}={len_h}>0。求二面角 {point_B}-{point_A1}{point_D}-{point_A}（以棱 {point_A1}{point_D} 为棱线、夹在平面 {point_B}{point_A1}{point_D} 与平面 {point_A}{point_A1}{point_D} 之间）的正弦值。",
    "en_problem": f"As shown, given a parallelepiped {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} satisfying: (1) the base {point_A}{point_B}{point_C}{point_D} is a rhombus with {point_A}{point_B}={point_A}{point_D}={len_a}>0 and ∠{point_B}{point_A}{point_D}={ang_theta} (0<{ang_theta}<π); (2) the lateral edge {point_A}{point_A1} is perpendicular to the base {point_A}{point_B}{point_C}{point_D} with {point_A}{point_A1}={len_h}>0. Find the sine of dihedral angle {point_B}-{point_A1}{point_D}-{point_A} (with edge {point_A1}{point_D} as the common edge, between planes {point_B}{point_A1}{point_D} and {point_A}{point_A1}{point_D}).",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_29_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}')"}, ensure_ascii=False) + "\n")
