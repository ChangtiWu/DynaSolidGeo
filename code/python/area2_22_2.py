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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M, point_AC, point_BM, point_N = random.sample(string.ascii_uppercase, 12)

# Add result calculation code
import math

def calculate():
    """
    计算平面 BB1M 与 NMD 所成夹角的余弦值

    返回:
    float: 夹角余弦
    """
    # 根据题解公式 cos = sqrt(33) / 11
    return math.sqrt(33) / 11


# 定义题干中用到的长度参数（即使没直接用在计算里也定义）
len_a = 1.0  # 题中 AB 边长
# len_AD = math.sqrt(2) * len_a  # AA1 = AD = √2 * AB
# len_AA1 = math.sqrt(2) * len_a
# 这里的 M、N 点坐标等不需要定义

# 验证计算结果
# result = calculate()
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)


# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_22_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在长方体 {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1} 中，{point_A}{point_A1} = {point_A}{point_D} = \\sqrt{{2}}{{{point_A}{point_B}}} ({point_A}{point_B}={len_a})，点 {point_M} 在棱 {point_A1}{point_D1} 上，且 {point_A}{point_C} ⊥ {point_B}{point_M}。点 {point_N} 满足 \\(\\overrightarrow{{{point_C}{point_N}}} = \\overrightarrow{{{point_N}{point_C1}}}\\)，求平面 {point_B}{point_B1}{point_M} 与 {point_N}{point_D}{point_M} 所成夹角的余弦值。",
    "en_problem": f"In the cuboid {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1}, {point_A}{point_A1} = {point_A}{point_D} = \\sqrt{{2}}{{{point_A}{point_B}}} ({point_A}{point_B}={len_a}), point {point_M} is on edge {point_A1}{point_D1}, and {point_A}{point_C} ⊥ {point_B}{point_M}. Point {point_N} satisfies \\(\\overrightarrow{{{point_C}{point_N}}} = \\overrightarrow{{{point_N}{point_C1}}}\\). Find the cosine of the angle between plane {point_B}{point_B1}{point_M} and {point_N}{point_D}{point_M}.",
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
    f.write(json.dumps({json_data["id"]: f"area2_22_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_M}', '{point_AC}', '{point_BM}', '{point_N}')"}, ensure_ascii=False) + "\n")
