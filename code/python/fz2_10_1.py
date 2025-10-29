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
point_A, point_B, point_C, point_D, point_O = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math

def calculate(len_m):
    """
    计算当四面体 B-ACD 体积最大时，
    外接球球心 O 到平面 ABD 的距离

    参数:
    len_m (float): AD = CD 的长度

    返回:
    float: 距离
    """
    # 根据题干给出的解答公式: (len_m * sqrt(42)) / 21
    return (len_m * math.sqrt(42)) / 21


# 定义题干中的参数变量
len_m = math.sqrt(2)  # AD = CD = √2

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_m)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)

# Calculate the result
result = calculate(len_m)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz2_10_1",
    "type": 8,
    "level": 2,
    "cn_problem": f"在平面四边形{point_A}{point_B}{point_C}{point_D}中，三角形{point_A}{point_B}{point_C}为正三角形，{point_A}{point_D} ⊥ {point_C}{point_D}，{point_A}{point_D} = {point_C}{point_D} = {len_m}。将四边形沿{point_A}{point_C}折起，得到四面体{point_B} - {point_A}{point_C}{point_D}。当四面体{point_B} - {point_A}{point_C}{point_D}的体积最大时，其外接球的球心为{point_O}，求点{point_O}到平面{point_A}{point_B}{point_D}的距离。",
    "en_problem": f"In planar quadrilateral {point_A}{point_B}{point_C}{point_D}, triangle {point_A}{point_B}{point_C} is equilateral, {point_A}{point_D} ⊥ {point_C}{point_D}, and {point_A}{point_D} = {point_C}{point_D} = {len_m}. The quadrilateral is folded along {point_A}{point_C} to form tetrahedron {point_B} - {point_A}{point_C}{point_D}. When the volume of tetrahedron {point_B} - {point_A}{point_C}{point_D} is maximized, its circumsphere has center {point_O}. Find the distance from point {point_O} to plane {point_A}{point_B}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"fz2_10_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}')"}, ensure_ascii=False) + "\n")
