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
point_A, point_B, point_C, point_M, point_D, point_Q, point_P = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
def calculate(len_a, param_lambda):
    """
    计算几何体 {point_Q}-{point_A}{point_B}{point_P} 的体积 V

    参数:
        len_a (float): 特征长度参数 a（与几何体尺寸直接相关的长度量）
        param_lambda (float): 比例参数 λ（通常满足 0 ≤ λ ≤ 1）

    返回:
        float: 几何体的体积计算结果

    公式:
        V = (len_a³ / 6) × λ × (1 - λ)
    """
    return (len_a ** 3) / 6 * param_lambda * (1 - param_lambda)


len_a = 3.0
param_lambda = 2/3
# volume = calculate(len_a, param_lambda)
#
#
# print(f"体积 V = {volume:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, param_lambda)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_12_2",
    "type": 8,
    "level": 3,
    "cn_problem": f"在平行四边形 {point_A}{point_B}{point_C}{point_M} 中，{point_A}{point_B}={point_A}{point_C}={len_a}（{len_a}>0），∠{point_A}{point_C}{point_M}=90°。以对角线 {point_A}{point_C} 为折痕，把 \\triangle {point_A}{point_C}{point_M} 向空间翻折，使点 {point_M} 转到点 {point_D}，且满足 {point_A}{point_B}⊥{point_D}{point_A}。设点 {point_Q} 在棱 {point_A}{point_D} 上，点 {point_P} 在棱 {point_B}{point_C} 上；给定比例 {param_lambda}∈(0,1)，使 {point_B}{point_P}={point_D}{point_Q}={param_lambda}·{point_D}{point_A}。求三棱锥 {point_Q}-{point_A}{point_B}{point_P} 的体积。",
    "en_problem": f"In parallelogram {point_A}{point_B}{point_C}{point_M}, {point_A}{point_B}={point_A}{point_C}={len_a} ({len_a}>0) and ∠{point_A}{point_C}{point_M}=90°. Using diagonal {point_A}{point_C} as the crease, fold \\triangle {point_A}{point_C}{point_M} into space so that point {point_M} moves to point {point_D}, satisfying {point_A}{point_B}⊥{point_D}{point_A}. Let point {point_Q} lie on edge {point_A}{point_D} and point {point_P} lie on edge {point_B}{point_C}. Given ratio {param_lambda}∈(0,1) such that {point_B}{point_P}={point_D}{point_Q}={param_lambda}·{point_D}{point_A}, find the volume of triangular pyramid {point_Q}-{point_A}{point_B}{point_P}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_12_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_M}', '{point_D}', '{point_Q}', '{point_P}')"}, ensure_ascii=False) + "\n")
