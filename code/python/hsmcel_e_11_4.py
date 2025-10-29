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


def calculate(len_a, len_b):
    """
    计算折叠后 B、D 两点间的距离

    参数:
    len_a (float): 长方形的长
    len_b (float): 长方形的宽

    返回:
    float: B、D 两点间的距离
    """
    # 计算对角线长度
    diagonal = math.sqrt(len_a ** 2 + len_b ** 2)
    # 计算 B 到对角线的垂线长度 BE
    BE = (len_a * len_b) / diagonal
    # 计算 A 到 E 的距离 AE
    AE = (len_b ** 2) / diagonal
    # 计算 D 到对角线的垂线长度 DF
    DF = (len_a * len_b) / diagonal
    # 计算 A 到 F 的距离 AF
    AF = (len_a ** 2) / diagonal
    # 计算 EF 的长度
    EF = abs(AE - AF)
    # 计算 ED 的长度
    ED_squared = EF ** 2 + (len_b ** 2 * len_a ** 2) / (len_a ** 2 + len_b ** 2)
    ED = math.sqrt(ED_squared)
    # 计算 BD 的长度
    BD_squared = BE ** 2 + ED ** 2
    BD = math.sqrt(BD_squared)

    return BD


# 示例参数
len_a = 4
len_b = 3
#
# # 调用函数计算结果
# result = calculate(len_a, len_b)
#
# # 输出结果
# print(f"计算结果: {result:.6f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_11_4",
    "type": 8,
    "level": 3,
    "cn_problem": f"设长方形{point_A}{point_B}{point_C}{point_D}的长为{len_a}（即{point_A}{point_D} = {len_a}），宽为{len_b}（即{point_A}{point_B} = {len_b}），沿对角线{point_A}{point_C}折叠成直二面角（面{point_A}{point_B}{point_C} ⊥ 面{point_A}{point_C}{point_D}），求折叠后{point_B}、{point_D}两点间的距离。",
    "en_problem": f"Let rectangle {point_A}{point_B}{point_C}{point_D} have length {len_a} (i.e., {point_A}{point_D} = {len_a}) and width {len_b} (i.e., {point_A}{point_B} = {len_b}). Fold along diagonal {point_A}{point_C} to form a right dihedral angle (face {point_A}{point_B}{point_C} ⊥ face {point_A}{point_C}{point_D}). Find the distance between points {point_B} and {point_D} after folding.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_11_4({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
