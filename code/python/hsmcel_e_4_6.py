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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_P, point_Q, point_R = random.sample(string.ascii_uppercase, 12)

# Add result calculation code
import math

def calculate(len_a, len_b, len_h):
    """
    计算正四棱台中特定三角形的面积

    参数:
    len_a (float): 上底边长
    len_b (float): 下底边长
    len_h (float): 棱台的高

    返回:
    float: 三角形的面积
    """
    # 计算分子部分: - (len_b - len_a)**2 * t**2 + (len_b**2 - len_a**2) / 2 * t
    # 由于t = 1时，得到最大面积公式: (len_b + len_a)**2 / 16
    numerator = (len_b + len_a)**2

    # 计算分母部分: 16
    denominator = 16

    # 返回三角形的面积
    return numerator / denominator

# 示例值
len_a = 2.0  # 上底边长
len_b = 4.0  # 下底边长
len_h = math.sqrt(6)  # 棱台的高
#
# # 调用函数计算面积
# result = calculate(len_a, len_b, len_h)
#
# # 输出结果
# print(f"三角形的面积为: {result:.6f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_b, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_4_6",
    "type": 7,
    "level": 3,
    "cn_problem": f"在正四棱台{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}中，上底边长{point_A1}{point_B1} = {len_a}，下底边长{point_A}{point_B} = {len_b}（{len_b} > {len_a} > 0），高为{len_h}，{point_E}为下底{point_B}{point_C}的中点。作平行于底面的截面，与线段{point_A}{point_D1}、{point_A}{point_B1}、{point_C1}{point_E}分别交于{point_P}、{point_Q}、{point_R}，求△{point_P}{point_Q}{point_R}面积的最大值。",
    "en_problem": f"In a regular quadrangular frustum {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, the upper base edge length {point_A1}{point_B1} = {len_a}, the lower base edge length {point_A}{point_B} = {len_b} ({len_b} > {len_a} > 0), the height is {len_h}, and {point_E} is the midpoint of the lower base {point_B}{point_C}. A cross-section parallel to the base is made, intersecting line segments {point_A}{point_D1}, {point_A}{point_B1}, and {point_C1}{point_E} at points {point_P}, {point_Q}, and {point_R} respectively. Find the max value of the area of triangle {point_P}{point_Q}{point_R}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_4_6({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_P}', '{point_Q}', '{point_R}')"}, ensure_ascii=False) + "\n")
