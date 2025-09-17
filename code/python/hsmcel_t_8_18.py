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
point_P, point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_a, len_c):
    """
    计算四棱锥 P-ABCD 中，比例系数 K = PA/AB 的取值下限

    参数:
    len_a (float): AB 边长
    len_c (float): AD = CD 边长

    返回:
    float: K 的下限
    """
    return (math.sqrt(3) * len_c) / (3 * math.sqrt(len_a**2 + len_c**2))


# 题干给定的数值
len_a = 1.0   # AB
len_c = 2.0   # AD = CD

# 验证输出
# K_min = calculate(len_a, len_c)
# print(f"K 的下限: {K_min:.6f}")

# Generate random lengths
len_c = round(len_scaling_factor * float(len_c), 2)
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_8_18",
    "type": 3,
    "level": 2,
    "cn_problem": f"在四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}中，{point_P}{point_A} ⊥ 底面{point_A}{point_B}{point_C}{point_D}，∠{point_B}{point_A}{point_D} = 90°，{point_A}{point_B} ∥ {point_C}{point_D}，{point_A}{point_D} = {point_C}{point_D} = {len_c}（{len_c} > 0），{point_E}、{point_F}分别为{point_P}{point_C}、{point_C}{point_D}的中点。设{point_P}{point_A} =  len_t  · {point_A}{point_B}（{point_A}{point_B} = {len_a}，{len_a} > 0， len_t 为比例系数），且二面角{point_E}-{point_B}{point_D}-{point_C}的平面角大于30°，求 len_t 的最小值。",
    "en_problem": f"In pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, {point_P}{point_A} ⊥ base {point_A}{point_B}{point_C}{point_D}, ∠{point_B}{point_A}{point_D} = 90°, {point_A}{point_B} ∥ {point_C}{point_D}, {point_A}{point_D} = {point_C}{point_D} = {len_c} ({len_c} > 0), and {point_E}, {point_F} are midpoints of {point_P}{point_C}, {point_C}{point_D} respectively. Let {point_P}{point_A} =  len_t  · {point_A}{point_B} (where {point_A}{point_B} = {len_a}, {len_a} > 0,  len_t  is a proportion coefficient), and the dihedral angle {point_E}-{point_B}{point_D}-{point_C} has planar angle greater than 30°. Find the minimum value of  len_t .",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_8_18({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
