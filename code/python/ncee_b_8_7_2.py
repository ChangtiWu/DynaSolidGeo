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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M, point_N = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math


def calculate(len_a, len_b, len_c, len_d):
    """计算sin(theta)的值（公式：[len_c*(len_a + √(len_d² - len_b²/4))] / [√(len_c² + len_d² - len_b²/4) * √(len_c² + len_a²)]）"""
    # 计算分子中的根号部分
    sqrt_part = math.sqrt(len_d ** 2 - (len_b ** 2) / 4)
    numerator = len_c * (len_a + sqrt_part)

    # 计算分母的两个根号部分
    denominator1 = math.sqrt(len_c ** 2 + len_d ** 2 - (len_b ** 2) / 4)
    denominator2 = math.sqrt(len_c ** 2 + len_a ** 2)
    denominator = denominator1 * denominator2

    return numerator / denominator


# 测试示例（选择使根号内为整数的参数）
len_a = 1
len_b = 2
len_c = 2.0
len_d = math.sqrt(5)

# print(calculate(len_a, len_b, len_c, len_d))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)
len_d = round(len_scaling_factor * float(len_d), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c, len_d)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_8_7_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在四棱柱{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}中，侧棱{point_A}{point_A1}⊥底面{point_A}{point_B}{point_C}{point_D}，{point_A}{point_B}⊥{point_A}{point_C}。设{point_A}{point_B}={len_a}，{point_A}{point_C}={len_b}，{point_A}{point_A1}={len_c}，{point_A}{point_D}={point_C}{point_D}={len_d}，且点{point_M}和{point_N}分别为{point_B1}{point_C}和{point_D1}{point_D}的中点。求二面角{point_D1}-{point_A}{point_C}-{point_B1}的正弦值。",
    "en_problem": f"In quadrilateral prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, lateral edge {point_A}{point_A1}⊥base {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B}⊥{point_A}{point_C}. Let {point_A}{point_B}={len_a}, {point_A}{point_C}={len_b}, {point_A}{point_A1}={len_c}, {point_A}{point_D}={point_C}{point_D}={len_d}, and points {point_M} and {point_N} are midpoints of {point_B1}{point_C} and {point_D1}{point_D} respectively. Find the sine value of dihedral angle {point_D1}-{point_A}{point_C}-{point_B1}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_8_7_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
