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
point_A, point_B, point_C, point_P, point_A_prime = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_k: float) -> float:
    """计算 cos(arg_gamma) 的值（公式：cos(arg_gamma) = (3 - 8*len_k²) / [2*(3 + 4*len_k²)]）"""
    numerator = 3 - 8 * (len_k ** 2)
    denominator = 2 * (3 + 4 * (len_k ** 2))
    return numerator / denominator


len_a = 1.0
len_k = math.sqrt(6) / 4

# result = calculate(len_k)
# print(f"cos_arg_gamma = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_k = round(random.uniform(1.0, 2.0) * float(len_k), 2)

# Calculate the result
result = calculate(len_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_s_6_1",
    "type": 2,
    "level": 2,
    "cn_problem": f"设 $\\triangle {point_A}{point_B}{point_C}$ 为边长为 ${len_a}>0$ 的正三角形；点 {point_P} 满足 ${point_P}{point_A}\\perp$(平面${point_A}{point_B}{point_C}$)，且 ${point_P}{point_A} = {len_k}{len_a}$，${len_k}>0$；记点 ${point_A_prime}$ 为点 {point_A} 关于平面 ${point_P}{point_B}{point_C}$ 的对称点。求异面直线 ${point_A_prime}{point_C}$ 与 ${point_A}{point_B}$ 所成角 ${{arg_gamma}}$ 的余弦值 $\\cos{{arg_gamma}}$。",
    "en_problem": f"Let $\\triangle {point_A}{point_B}{point_C}$ be an equilateral triangle with side length ${len_a}>0$; point {point_P} satisfies ${point_P}{point_A}\\perp$(plane ${point_A}{point_B}{point_C}$) and ${point_P}{point_A} = {len_k}{len_a}$ where ${len_k}>0$; let point ${point_A_prime}$ be the reflection of point {point_A} with respect to plane ${point_P}{point_B}{point_C}$. Find the cosine of the angle ${{arg_gamma}}$ between skew lines ${point_A_prime}{point_C}$ and ${point_A}{point_B}$: $\\cos{{arg_gamma}}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_s_6_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_P}', '{point_A_prime}')"}, ensure_ascii=False) + "\n")
