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
point_A, point_B, point_C, point_F, point_E, point_D = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_a: float, len_b: float, len_k: float) -> float:
    """
    计算 cosθ 的值，基于给定的公式：
    cosθ = (len_b * √len_k) / √(len_a³ + len_a²·len_k + len_b²·len_k)

    参数:
        len_a: 公式中变量 len_a 的值（浮点数）
        len_b: 公式中变量 len_b 的值（浮点数）
        len_k: 公式中变量 len_k 的值（需非负，否则平方根无意义）

    返回:
        cosθ 的计算结果（浮点数）
    """
    # 计算分子部分：len_b * √len_k
    numerator = len_b * math.sqrt(len_k)

    # 计算分母中被开方的整体表达式：len_a³ + len_a²·len_k + len_b²·len_k
    denominator_inside = len_a ** 3 + (len_a ** 2 * len_k) + (len_b ** 2 * len_k)

    # 计算分母：√(denominator_inside)
    denominator = math.sqrt(denominator_inside)

    # 计算并返回 cosθ 的值
    return numerator / denominator


len_a = 2.0
len_b = 3.0
len_k = 1.0

# # 调用函数计算
# result = calculate(len_a, len_b, len_k)
#
# # 输出结果（保留4位小数）
# print(f"当 len_a={len_a}, len_b={len_b}, len_k={len_k} 时，cosθ = {result:.4f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_k = round(len_scaling_factor * float(len_k), 2)

# Calculate the result
result = calculate(len_a, len_b, len_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_25_2",
    "type": 2,
    "level": 3,
    "cn_problem": f"设底面直角三角形 {point_A}{point_B}{point_C} 满足 ∠{point_A}{point_C}{point_B} = 90°，并给定\n  {point_B}{point_C} = {len_a} (>0),\n  {point_A}{point_C} = {len_b} (>0);\n- 在侧面 {point_B}{point_C}{point_F}{point_E} 内取\n  {point_B}{point_E} = {point_E}{point_F} = {point_F}{point_C} = {len_k} (>0)，且 {point_E}{point_F} ∥ {point_B}{point_C}；同时平面 {point_B}{point_C}{point_F}{point_E} ⟂ 底面 {point_A}{point_B}{point_C};\n- 由相似关系得 {point_A}{point_D} = 2*{len_k}，{point_D}{point_C} = {len_k} 并保持 {point_B}{point_C} ∥ {point_A}{point_D},\n  {point_D}{point_C} ⟂ {point_A}{point_D}。\n令 θ 为直线 {point_B}{point_D} 与平面 {point_A}{point_C}{point_F}{point_D} 所成的锐角。求\n\\(\\cosθ\\) 。",
    "en_problem": f"The base right triangle {point_A}{point_B}{point_C} has right angle at C with\n  {point_B}{point_C} = {len_a} (>0)  and {point_A}{point_C} = {len_b} (>0);\n- In lateral face {point_B}{point_C}{point_F}{point_E}, take\n  {point_B}{point_E} = {point_E}{point_F} = {point_F}{point_C} = {len_k} (>0) with {point_E}{point_F} ∥ {point_B}{point_C}; the rectangle B C F E is perpendicular to the base;\n- Similarity forces {point_A}{point_D} = 2*{len_k}, {point_D}{point_C} = {len_k} and keeps {point_B}{point_C} ∥ {point_A}{point_D}, {point_D}{point_C} ⟂ {point_A}{point_D}.\nLet θ be the acute angle between line {point_B}{point_D} and plane {point_A}{point_C}{point_F}{point_D}. Find \\(\\cosθ\\).",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_25_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_F}', '{point_E}', '{point_D}')"}, ensure_ascii=False) + "\n")
