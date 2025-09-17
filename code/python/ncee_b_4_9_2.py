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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_M, point_N, point_P, point_E, point_F, point_O = random.sample(string.ascii_uppercase, 12)

# Add result calculation code
import math


def calculate(len_a):
    """
    计算特定几何体的体积 V_{point_B-E B1 C1 F}

    参数:
        len_a (float): 特征长度参数 a

    返回:
        float: 几何体的体积计算结果

    公式:
        V = (len_a³) / 9
    """
    return (len_a ** 3) / 9


len_a = 6.0
ang_alpha = math.pi/3
# volume = calculate(len_a)
#
# print(f"体积 V = {volume:.6f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_9_2",
    "type": 5,
    "level": 2,
    "cn_problem": f"设直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 满足：底面 \\triangle {point_A}{point_B}{point_C} 为边长为 {len_a}（{len_a}>0）的正三角形；侧面 {point_B}{point_B1}{point_C1}{point_C} 为矩形；{point_M}、{point_N} 分别为 {point_B}{point_C}、{point_B1}{point_C1} 的中点；{point_P} 为 {point_A}{point_M} 上一点。过 {point_B1}{point_C1} 和 {point_P} 的平面交 {point_A}{point_B} 于 {point_E}，交 {point_A}{point_C} 于 {point_F}。设 {point_O} 为 \\triangle {point_A1}{point_B1}{point_C1} 的重心，满足 {point_A}{point_O}={point_A}{point_B}={len_a}，{point_A}{point_O} \\parallel 平面 {point_E}{point_B1}{point_C1}{point_F}，且 ∠{point_M}{point_P}{point_N}={ang_alpha}（0<{ang_alpha}<\\pi）。求四棱锥 {point_B}-{point_E}{point_B1}{point_C1}{point_F} 的体积。",
    "en_problem": f"Consider a right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} where: the base \\triangle {point_A}{point_B}{point_C} is an equilateral triangle with side length {len_a} ({len_a}>0); the lateral face {point_B}{point_B1}{point_C1}{point_C} is a rectangle; {point_M} and {point_N} are midpoints of {point_B}{point_C} and {point_B1}{point_C1} respectively; {point_P} lies on {point_A}{point_M}. The plane through {point_B1}{point_C1} and {point_P} intersects {point_A}{point_B} at {point_E} and {point_A}{point_C} at {point_F}. Let {point_O} be the centroid of \\triangle {point_A1}{point_B1}{point_C1}, satisfying {point_A}{point_O}={point_A}{point_B}={len_a}, {point_A}{point_O} \\parallel plane {point_E}{point_B1}{point_C1}{point_F}, and ∠{point_M}{point_P}{point_N}={ang_alpha} (0<{ang_alpha}<\\pi). Find the volume of the quadrilateral pyramid {point_B}-{point_E}{point_B1}{point_C1}{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_9_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_M}', '{point_N}', '{point_P}', '{point_E}', '{point_F}', '{point_O}')"}, ensure_ascii=False) + "\n")
