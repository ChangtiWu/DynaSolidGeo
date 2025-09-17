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
point_P, point_A, point_B, point_C, point_D, point_O, point_E = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_b, len_c):
    """
    计算四棱锥 P-ABCD 的平面 PEC 截外接球的截面面积

    参数:
    len_b (float): 底面正方形边长的一半
    len_c (float): PO 长度的一半

    返回:
    float: 截面面积 πr^2
    """
    # 直接根据题解公式
    numerator = 9 * len_b**8 + 320 * len_c**6 + 608 * len_b**2 * len_c**4 + 260 * len_b**4 * len_c**2 - 9 * len_b**6
    denominator = 16 * len_c**2 * (20 * len_c**2 + 9 * len_b**2)
    return math.pi * numerator / denominator


# 定义题干中的参数变量
len_b = 1.0  # AB/2
len_c = 1.0  # PO/2

# 验证计算结果
#result = calculate(len_b, len_c)
#print(f"截面面积: {result:.6f}")

# Generate random lengths
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_24_3",
    "type": 4,
    "level": 2,
    "cn_problem": f"在四棱锥 {point_P} - {point_A}{point_B}{point_C}{point_D} 中，底面为正方形，设 {point_A}{point_B} = 2*{len_b}（{len_b} > 0），{point_O} 为 {point_A}{point_D} 的中点，{point_P}{point_O} = 2*{len_c}（{len_c} > 0），{point_E} 为线段 {point_A}{point_B} 的中点。四棱锥 {point_P} - {point_A}{point_B}{point_C}{point_D} 的外接球记为球 M，求平面 {point_P}{point_E}{point_C} 截球 M 所得的截面面积。",
    "en_problem": f"In the quadrilateral pyramid {point_P} - {point_A}{point_B}{point_C}{point_D}, the base is a square with {point_A}{point_B} = 2*{len_b} ({len_b} > 0). Let {point_O} be the midpoint of {point_A}{point_D}, {point_P}{point_O} = 2*{len_c} ({len_c} > 0), and {point_E} be the midpoint of {point_A}{point_B}. The circumsphere of the pyramid is M. Find the area of the section formed when plane {point_P}{point_E}{point_C} intersects sphere M.",
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
    f.write(json.dumps({json_data["id"]: f"area2_24_3({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}', '{point_E}', 'M')"}, ensure_ascii=False) + "\n")
