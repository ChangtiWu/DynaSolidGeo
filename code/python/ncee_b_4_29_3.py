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
point_V, point_A, point_B, point_C, point_O, point_M = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_a):
    """
    计算三棱锥 V-ABC 的体积，基于给定的公式：
    V_{V-ABC} = (√6 / 12) * len_a³

    参数:
    len_a (float): 三棱锥的底面边长（或相关特征长度，需为正数）

    返回:
    float: 三棱锥的体积 V_{V-ABC}
    """
    # 计算常数系数：√6 / 12
    constant = math.sqrt(6) / 12
    # 计算 len_a 的三次方
    len_a_cubed = len_a ** 3
    # 计算体积
    volume = constant * len_a_cubed
    return volume

len_a = math.sqrt(2)
# result1 = calculate(len_a)
# print(f"当 len_a={len_a} 时，V={result1:.4f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_29_3",
    "type": 5,
    "level": 2,
    "cn_problem": f"在三棱锥 {point_V}-{point_A}{point_B}{point_C} 中：\n- 平面 {point_V}{point_A}{point_B} ⟂ 平面 {point_A}{point_B}{point_C}；\n- △{point_V}{point_A}{point_B} 为等边三角形；\n- 底面 △{point_A}{point_B}{point_C} 为等腰直角三角形，满足 {point_A}{point_C} = {point_B}{point_C} = {len_a} 且 {point_A}{point_C} ⟂ {point_B}{point_C}；\n- {point_O}、{point_M} 分别为 {point_A}{point_B} 与 {point_V}{point_A} 的中点。\n求三棱锥 {point_V}-{point_A}{point_B}{point_C} 的体积。",
    "en_problem": f"In the triangular pyramid {point_V}-{point_A}{point_B}{point_C}:\n- Plane {point_V}{point_A}{point_B} is perpendicular to plane {point_A}{point_B}{point_C};\n- △{point_V}{point_A}{point_B} is equilateral;\n- The base △{point_A}{point_B}{point_C} is an isosceles right triangle with {point_A}{point_C} = {point_B}{point_C} = {len_a} and {point_A}{point_C} ⟂ {point_B}{point_C};\n- {point_O} and {point_M} are the mid‑points of {point_A}{point_B} and {point_V}{point_A}, respectively.\nFind the volume of the pyramid {point_V}-{point_A}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_29_3({mode}, {azimuth}, {elevation}, '{point_V}', '{point_A}', '{point_B}', '{point_C}', '{point_O}', '{point_M}')"}, ensure_ascii=False) + "\n")
