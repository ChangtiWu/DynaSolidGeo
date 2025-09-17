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
point_P, point_A, point_B, point_C, point_D, point_M = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_a: float, len_b: float, len_c: float) -> float:
    """
    计算线段比例 (point_A point_M)/(point_A point_P) 的值，基于给定的几何条件。

    参数:
        len_a: 公式中变量 len_a 的值（浮点数，长度量）
        len_b: 公式中变量 len_b 的值（浮点数，长度量）
        len_c: 公式中变量 len_c 的值（浮点数，长度量）

    返回:
        比例值 (point_A point_M)/(point_A point_P) 的计算结果（浮点数）

    异常:
        ValueError: 当不满足存在条件时抛出（len_c² ≤ len_b²/4 或 len_a² > 4len_c² - len_b²）
    """
    # 检查存在条件1：len_c² > len_b²/4（保证根号内非负）
    if len_c ** 2 <= (len_b ** 2) / 4:
        raise ValueError(f"不满足存在条件：len_c² ({len_c ** 2}) 必须大于 len_b²/4 ({(len_b ** 2) / 4})")

    # 检查存在条件2：len_a² ≤ 4len_c² - len_b²（保证比例有意义）
    if len_a ** 2 > 4 * len_c ** 2 - len_b ** 2:
        raise ValueError(
            f"不满足存在条件：len_a² ({len_a ** 2}) 必须 ≤ 4len_c² - len_b² ({4 * len_c ** 2 - len_b ** 2})")

    # 计算分母部分：2√(len_c² - len_b²/4)
    denominator = 2 * math.sqrt(len_c ** 2 - (len_b ** 2) / 4)

    # 计算并返回比例值
    return len_a / denominator


len_a = 1.0
len_b = 2.0
len_c = math.sqrt(5)


# result = calculate(len_a, len_b, len_c)
# print(f"结果为 {result:.4f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_28_3",
    "type": 3,
    "level": 3,
    "cn_problem": f"设四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 满足\n- 底面 {point_A}{point_B}{point_C}{point_D} 为一般平行四边形，取\n  {point_A}{point_B} = {len_a} (>0),  {point_A}{point_D} = {len_b} (>0)，且 {point_A}{point_B} ⟂ {point_A}{point_D};\n- 设 {point_A}{point_C} = {point_C}{point_D} = {len_c} (> {len_b}/2)，使下底成为等腰风筝形；\n- 顶点 {point_P} 使平面 {point_P}{point_A}{point_D} ⟂ 底面，且 {point_P}{point_A} = {point_P}{point_D}.\n\n在棱 {point_P}{point_A} 上取点 {point_M}，若能使直线 {point_B}{point_M} ∥ 平面 {point_P}{point_C}{point_D}，求分比\n\\(\\displaystyle \\frac{{{point_A}{point_M}}}{{{point_A}{point_P}}}\\) 。",
    "en_problem": f"Let a four‑sided pyramid {point_P}-{point_A}{point_B}{point_C}{point_D} satisfy\n- The base {point_A}{point_B}{point_C}{point_D} is a parallelogram with\n  {point_A}{point_B} = {len_a} (>0), {point_A}{point_D} = {len_b} (>0) and {point_A}{point_B} ⟂ {point_A}{point_D};\n- The edges {point_A}{point_C} = {point_C}{point_D} = {len_c} (> {len_b}/2), so the base is an isosceles kite;\n- Vertex {point_P} obeys: plane {point_P}{point_A}{point_D} ⟂ plane {point_A}{point_B}{point_C}{point_D}, and {point_P}{point_A} = {point_P}{point_D}.\n\nDetermine whether there exists a point {point_M} on edge {point_P}{point_A} such that line {point_B}{point_M} is parallel to plane {point_P}{point_C}{point_D}. If it exists, find the ratio\n\\(\\displaystyle \\frac{{{point_A}{point_M}}}{{{point_A}{point_P}}}\\) .",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_28_3({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}')"}, ensure_ascii=False) + "\n")
