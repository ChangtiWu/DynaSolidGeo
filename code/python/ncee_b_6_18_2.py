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
point_A, point_B, point_C, point_A1, point_C1, point_B1 = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate():
    r"""
    计算固定正弦值 $\sin\theta = \frac{\sqrt{39}}{13}$。

    返回:
    float: 固定正弦值（约0.4804）
    """
    # 计算分子：√39
    numerator = math.sqrt(39)
    # 计算分母：13
    denominator = 13
    # 计算正弦值
    sin_theta = numerator / denominator
    return sin_theta


len_k = 1.0

# result = calculate()
# print(f"sin_theta的值为：{result:.4f}")

# Generate random lengths
len_k = round(len_scaling_factor * float(len_k), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_18_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"把所有长度统一乘以缩放系数 {len_k} (>0)：\n- 底面 △{point_A}{point_B}{point_C} 仍满足 ∠{point_A}{point_B}{point_C} = 120°，并取\n  {point_A}{point_B} = {point_B}{point_C} = 2*{len_k};\n- 三条侧棱垂直底面：{point_A1}{point_A} = 4*{len_k},\n  {point_C1}{point_C} = {len_k},\n  {point_B1}{point_B} = 2*{len_k};\n- 其它平行、对称关系与原题保持一致。\n设 θ 为直线 {point_A}{point_C} 与平面 {point_A}{point_B}{point_B1} 所成的锐角。求\n\\(\\sinθ\\) 。",
    "en_problem": f"Scale all lengths by a common factor {len_k} (>0):\n- Base triangle {point_A}{point_B}{point_C} still has ∠{point_A}{point_B}{point_C} = 120°, with\n  {point_A}{point_B} = {point_B}{point_C} = 2*{len_k};\n- Three lateral edges are perpendicular to the base:\n  {point_A1}{point_A} = 4*{len_k}, {point_C1}{point_C} = {len_k}, {point_B1}{point_B} = 2*{len_k};\n- All parallel / perpendicular relations remain as in the original statement.\nLet θ be the acute angle between line {point_A}{point_C} and plane {point_A}{point_B}{point_B1}. Find\n\\(\\sinθ\\) and \\(\\cosθ\\) .",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_18_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_C1}', '{point_B1}')"}, ensure_ascii=False) + "\n")
