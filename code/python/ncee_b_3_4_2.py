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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_p, len_q, len_h):
    """
    计算余弦值 cos(theta) 的表达式

    参数:
    len_p (float): 长度参数 p
    len_q (float): 长度参数 q
    len_h (float): 高度参数 h

    返回:
    float: cos(theta) 的计算结果
    """
    # 计算分子: len_p * len_q
    numerator = len_p * len_q

    # 计算分母中的两个部分
    term1 = len_h ** 2 + len_q ** 2  # (len_h² + len_q²)
    term2 = len_h ** 2 + len_p ** 2  # (len_h² + len_p²)

    # 计算整个分母: sqrt(term1 * term2)
    denominator = math.sqrt(term1 * term2)

    # 返回分子除以分母的结果
    return numerator / denominator

# 示例调用
len_p = 2.0
len_q = 2.0
len_h = 2.0

# cos_theta = calculate(len_p, len_q, len_h)
# print(f"cos(theta) = {cos_theta:.6f}")
#
# # 验证结果范围 (余弦值应在 -1 到 1 之间)
# if abs(cos_theta) > 1:
#     print("注意：计算结果超出余弦值定义域 [-1, 1]")
# Generate random lengths
len_p = round(len_scaling_factor * float(len_p), 2)
len_q = round(len_scaling_factor * float(len_q), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_p, len_q, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_3_4_2",
    "type": 2,
    "level": 3,
    "cn_problem": f"如图，三棱柱 {point_A}{point_B}{point_C}−{point_A1}{point_B1}{point_C1} 的底面 {point_A}{point_B}{point_C} 为直角三角形，满足 ∠{point_A}{point_B}{point_C}=90°。已知\n{point_A}{point_B} = {len_p}，{point_B}{point_C} = {len_q}（{len_p},{len_q}>0），\n且侧棱 {point_A}{point_A1} ⟂ 平面 {point_A}{point_B}{point_C}，{point_A}{point_A1} = {len_h}（{len_h}>0）。\n设 {point_D} 为 {point_A}{point_C1} 的中点。\n记平面 Π₁ = {point_A}{point_B}{point_D}，平面 Π₂ = {point_B}{point_D}{point_C}，它们的锐二面角为 θ。\n求 \\(\\cos\\theta\\)。",
    "en_problem": f"In the triangular prism {point_A}{point_B}{point_C}−{point_A1}{point_B1}{point_C1}, the base {point_A}{point_B}{point_C} is right-angled at {point_B}. Let\n{point_A}{point_B} = {len_p},\n{point_B}{point_C} = {len_q}  (both positive),\nand the lateral edge {point_A}{point_A1} is perpendicular to the base plane with length {len_h} > 0.\nLet {point_D} be the midpoint of {point_A}{point_C1}.\nDefine Π₁ = {point_A}{point_B}{point_D} and Π₂ = {point_B}{point_D}{point_C}.  If θ is the acute dihedral angle between Π₁ and Π₂, find \\(\\cos\\theta\\).",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_3_4_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}')"}, ensure_ascii=False) + "\n")
