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
point_P, point_A, point_B, point_C, point_D, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
def calculate(param_t):
    """
    计算 V₁/V₂ 的比值，基于给定的参数 param_t：
    V₁/V₂ = (8 * param_t) / (1 + param_t²)

    参数:
    param_t (float): 输入参数（任意实数）

    返回:
    float: V₁与V₂的比值
    """
    # 计算分子：8 * param_t
    numerator = 8 * param_t
    # 计算分母：1 + param_t²
    denominator = 1 + (param_t ** 2)
    # 计算比值
    ratio = numerator / denominator
    return ratio

len_b = 1.0
len_c = 1.0
param_t = 1.0
# result1 = calculate(param_t)
# print(f"当 param_t={param_t} 时，V₁/V₂={result1:.4f}")
# Generate random lengths
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(param_t)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_27_2",
    "type": 5,
    "level": 2,
    "cn_problem": f"在阳马四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 中：\n- 底面 {point_A}{point_B}{point_C}{point_D} 为长方形，设 {point_B}{point_C}={len_b}，{point_C}{point_D}={len_c}；\n- 侧棱 {point_P}{point_D} = {param_t}·{len_c} 且 {point_P}{point_D} ⟂ 底面；\n- 点 {point_E} 为 {point_P}{point_C} 的中点，连接 {point_D}{point_E}、{point_B}{point_D}、{point_B}{point_E}。\n设\n\\[\nV_1 = 四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}的体积,\\quad\nV_2 = 四面体{point_D}-{point_B}{point_C}{point_E}的体积.\n\\]\n求：体积比 V₁:V₂。",
    "en_problem": f"In the right truncated square pyramid (\"Yang‑ma\") {point_P}-{point_A}{point_B}{point_C}{point_D}:\n- The rectangular base {point_A}{point_B}{point_C}{point_D} has sides {len_b} = {point_B}{point_C} and {len_c} = {point_C}{point_D};\n- The lateral edge {point_P}{point_D} is perpendicular to the base with length {param_t}·{len_c} ( {param_t} > 0 );\n- Point {point_E} is the midpoint of {point_P}{point_C}; segments {point_D}{point_E}, {point_B}{point_D}, and {point_B}{point_E} are drawn.\nLet\n\\[\nV_1 = Vol. of tetrahedron {point_P}-{point_A}{point_B}{point_C}{point_D},\\quad\nV_2 = Vol. of tetrahedron {point_D}-{point_B}{point_C}{point_E}.\n\\]\nFind:\nThe ratio V₁ : V₂.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_27_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
