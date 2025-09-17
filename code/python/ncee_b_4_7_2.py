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


def calculate(len_a, len_h):
    """
    计算点 P 到四面体 ABCD 的体积 V_{P-ABCD}

    参数:
        len_a (float): 底面边长 a
        len_h (float): 高度 h

    返回:
        float: 体积计算结果

    公式:
        V = (√2/3) × len_a² × len_h
    """
    return (math.sqrt(2) / 3) * (len_a ** 2) * len_h

# 当底面边长为 5，高度为 8 时的体积计算
len_a = 1.0
len_h = 1.0
# volume = calculate(len_a, len_h)
#
# print(f"体积 V = {volume:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_7_2",
    "type": 5,
    "level": 2,
    "cn_problem": f"已知四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 的底面 {point_A}{point_B}{point_C}{point_D} 为矩形，满足 {point_D}{point_C}={len_a}（{len_a}>0），{point_D}{point_A}={len_a}\\sqrt{{2}}。顶点 {point_P} 到底面 {point_A}{point_B}{point_C}{point_D} 的距离为 {len_h}（{len_h}>0），即 {point_P}{point_D}⊥平面 {point_A}{point_B}{point_C}{point_D} 且 {point_P}{point_D}={len_h}。设 {point_M} 为棱 {point_B}{point_C} 的中点，且 {point_P}{point_B}⊥{point_A}{point_M}。求四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 的体积。",
    "en_problem": f"Given pyramid {point_P}-{point_A}{point_B}{point_C}{point_D} with rectangular base {point_A}{point_B}{point_C}{point_D}, where {point_D}{point_C}={len_a} ({len_a}>0) and {point_D}{point_A}={len_a}\\sqrt{{2}}. The distance from vertex {point_P} to base {point_A}{point_B}{point_C}{point_D} is {len_h} ({len_h}>0), i.e., {point_P}{point_D}⊥plane {point_A}{point_B}{point_C}{point_D} and {point_P}{point_D}={len_h}. Let {point_M} be the midpoint of edge {point_B}{point_C}, with {point_P}{point_B}⊥{point_A}{point_M}. Find the volume of pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_7_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}')"}, ensure_ascii=False) + "\n")
