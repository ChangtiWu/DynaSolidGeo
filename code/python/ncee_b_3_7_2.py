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
point_P, point_A, point_B, point_C, point_O, point_M = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_m, param_lambda):
    """
    计算 d = (len_m * param_lambda) / sqrt(2*(1 + param_lambda^2))

    参数:
    len_m -- 长度参数
    param_lambda -- 波长参数

    返回:
    d -- 计算结果
    """
    denominator = math.sqrt(2 * (1 + param_lambda ** 2))
    d = (len_m * param_lambda) / denominator
    return d

len_m=2 * math.sqrt(2)
param_lambda=2
len_s = 4
# result = calculate(len_m, param_lambda)
# print(result)
# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)
len_s = round(len_scaling_factor * float(len_s), 2)
param_lambda = round(len_scaling_factor * float(param_lambda), 2)

# Calculate the result
result = calculate(len_m, param_lambda)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_3_7_2",
    "type": 3,
    "level": 2,
    "cn_problem": f"在四面体 {point_P}{point_A}{point_B}{point_C} 中，底面 \\triangle {point_A}{point_B}{point_C} 是直角等腰三角形，直角顶点在 {point_B}，有 {point_A}{point_B} = {point_B}{point_C} = {len_m}，{point_A}{point_C} = {len_m}\\sqrt{2}。顶点 {point_P} 到三底点距离相等，{point_P}{point_A} = {point_P}{point_B} = {point_P}{point_C} = {len_s}（{len_s} > {len_m}/\\sqrt{2}）。点 {point_O} 是棱 {point_A}{point_C} 的中点。在棱 {point_B}{point_C} 上取点 {point_M}，令 {point_C}{point_M} = {param_lambda}\\,{point_M}{point_B}（{param_lambda} > 0）。求点 {point_C} 到平面 {point_P}{point_O}{point_M} 的距离。",
    "en_problem": f"In tetrahedron {point_P}{point_A}{point_B}{point_C}, the base \\triangle {point_A}{point_B}{point_C} is a right isosceles triangle with right angle at {point_B}, where {point_A}{point_B} = {point_B}{point_C} = {len_m} and {point_A}{point_C} = {len_m}\\sqrt{2}. The vertex {point_P} is equidistant from the three base points: {point_P}{point_A} = {point_P}{point_B} = {point_P}{point_C} = {len_s} (where {len_s} > {len_m}/\\sqrt{2}). Point {point_O} is the midpoint of edge {point_A}{point_C}. On edge {point_B}{point_C}, take point {point_M} such that {point_C}{point_M} = {param_lambda}\\,{point_M}{point_B} ({param_lambda} > 0). Find the distance from point {point_C} to plane {point_P}{point_O}{point_M}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_3_7_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_O}', '{point_M}')"}, ensure_ascii=False) + "\n")
