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
point_A, point_B, point_C, point_D, point_O, point_P, point_E = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_a, len_b):
    """
    计算点 E 到直线 PC 的最小距离

    参数:
    len_a (float): OA = OB
    len_b (float): OC = OD

    返回:
    float: 最小距离
    """
    # 根据题干给出的解答公式: (len_a * len_b) / sqrt(len_a^2 + len_b^2)
    return (len_a * len_b) / math.sqrt(len_a ** 2 + len_b ** 2)


# 定义题干中的参数变量
len_a = 1.0  # OA = OB = 1
len_b = 2.0  # OC = OD = 2

# 验证计算结果（确认与参考答案一致后注释掉）
#result = calculate(len_a, len_b)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz2_3_1",
    "type": 8,
    "level": 1,
    "cn_problem": f"平面四边形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_C} ⊥ {point_B}{point_D}，垂足为{point_O}，且{point_O}{point_A} = {point_O}{point_B} = {len_a}，{point_O}{point_C} = {point_O}{point_D} = {len_b}（其中{len_a} > 0，{len_b} > 0）。将三角形{point_A}{point_B}{point_D}沿{point_B}{point_D}翻折至三角形{point_P}{point_B}{point_D}，使得平面{point_P}{point_B}{point_D} ⊥ 平面{point_B}{point_C}{point_D}。若点{point_E}为线段{point_B}{point_D}上的动点，求点{point_E}到直线{point_P}{point_C}距离的最小值。",
    "en_problem": f"In planar quadrilateral {point_A}{point_B}{point_C}{point_D}, {point_A}{point_C} ⊥ {point_B}{point_D} with foot {point_O}, and {point_O}{point_A} = {point_O}{point_B} = {len_a}, {point_O}{point_C} = {point_O}{point_D} = {len_b} (where {len_a} > 0, {len_b} > 0). Triangle {point_A}{point_B}{point_D} is folded along {point_B}{point_D} to triangle {point_P}{point_B}{point_D}, such that plane {point_P}{point_B}{point_D} ⊥ plane {point_B}{point_C}{point_D}. If point {point_E} is a moving point on segment {point_B}{point_D}, find the minimum distance from point {point_E} to line {point_P}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"fz2_3_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}', '{point_P}', '{point_E}')"}, ensure_ascii=False) + "\n")
