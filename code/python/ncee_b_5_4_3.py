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
point_P, point_A, point_B, point_C, point_D, point_E, point_F, point_G = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_p, len_c, len_a, len_b):
    """
    计算余弦值 cosθ，基于给定的公式：
    cosθ = len_p / √(len_c² + (len_b - len_a)²)

    参数:
    len_p (float): 分子参数（代表实际长度或其他正数）
    len_c (float): 分母中平方项的参数（代表实际长度或其他正数）
    len_a (float): 分母中差的平方项的第一个参数（代表实际长度或其他数值）
    len_b (float): 分母中差的平方项的第二个参数（代表实际长度或其他数值）

    返回:
    float: 计算得到的 cosθ 值
    """
    # 计算分母中的差平方项：(len_b - len_a)²
    diff_square = (len_b - len_a) ** 2
    # 计算分母的平方根部分：√(len_c² + 差平方项)
    denominator = math.sqrt(len_c ** 2 + diff_square)
    # 计算 cosθ
    cos_theta = len_p / denominator
    return cos_theta

len_p = 4.0
len_c = 4.0
len_a = 6.0
len_b = 3.0
# result1 = calculate(len_p, len_c, len_a, len_b)
# print(f"当 len_p={len_p}, len_c={len_c}, len_a={len_a}, len_b={len_b} 时，cosθ≈{result1:.4f}")  # 输出 0.7500

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_p = round(len_scaling_factor * float(len_p), 2)

# Calculate the result
result = calculate(len_p, len_c, len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_5_4_3",
    "type": 2,
    "level": 2,
    "cn_problem": f"在四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 中：\n- 底面 {point_A}{point_B}{point_C}{point_D} 为长方形，长 {point_A}{point_B} = {len_a}，宽 {point_B}{point_C} = {len_b}，其中 {len_b} > 0；\n- 侧棱 {point_P}{point_D} = {point_P}{point_C} = {len_p}（0 < {len_p} < {len_a}）；\n- 平面 {point_P}{point_D}{point_C} ⟂ 底面，且 {point_A}{point_D} ∥ {point_B}{point_C}，{point_P}{point_D} ⟂ {point_P}{point_B}（从而 {point_P}{point_D} ⟂ 平面 {point_P}{point_B}{point_C}）；\n- 点 {point_E} 为 {point_C}{point_D} 的中点；\n- 点 {point_F} 在 {point_A}{point_B} 上满足 {point_A}{point_F} : {point_F}{point_B} = 2 : 1；\n- 点 {point_G} 在 {point_B}{point_C} 上满足 {point_C}{point_G} : {point_G}{point_B} = 2 : 1（因此 {point_F}{point_G} ∥ {point_A}{point_C}）。\n求直线 {point_P}{point_A} 与直线 {point_F}{point_G} 所成锐角 θ 的余弦值。",
    "en_problem": f"In tetrahedron {point_P}-{point_A}{point_B}{point_C}{point_D}:\n- The base {point_A}{point_B}{point_C}{point_D} is a rectangle with {point_A}{point_B} = {len_a} and {point_B}{point_C} = {len_b} ({len_b} > 0);\n- The lateral edges satisfy {point_P}{point_D} = {point_P}{point_C} = {len_p} with 0 < {len_p} < {len_a};\n- Plane {point_P}{point_D}{point_C} is perpendicular to the base, {point_A}{point_D} ∥ {point_B}{point_C}, and {point_P}{point_D} ⟂ {point_P}{point_B} (hence {point_P}{point_D} ⟂ plane {point_P}{point_B}{point_C});\n- Point {point_E} is the midpoint of {point_C}{point_D};\n- Point {point_F} lies on {point_A}{point_B} with {point_A}{point_F} : {point_F}{point_B} = 2 : 1;\n- Point {point_G} lies on {point_B}{point_C} with {point_C}{point_G} : {point_G}{point_B} = 2 : 1, so {point_F}{point_G} ∥ {point_A}{point_C}.\nFind cos θ, where θ is the acute angle between lines {point_P}{point_A} and {point_F}{point_G}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_5_4_3({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_G}')"}, ensure_ascii=False) + "\n")
