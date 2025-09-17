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
point_S, point_A, point_B, point_C, point_D, point_M, point_N = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
def calculate(len_lambda: float) -> float:
    """计算 cos_phi 的值（公式：cos_phi = (len_lambda² - 3)/(len_lambda² + 2)）"""
    numerator = len_lambda ** 2 - 3
    denominator = len_lambda ** 2 + 2
    return numerator / denominator


# len_a = a # 原题中的正方形的边长a
len_a = 10
len_lambda = 2.0

# result = calculate(len_lambda)
# print(f"cos_phi = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_lambda = round(round(random.uniform(1, 5), 1) * float(len_lambda), 2)

# Calculate the result
result = calculate(len_lambda)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_6_4",
    "type": 2,
    "level": 3,
    "cn_problem": f"设 ${point_S}\\!-\\!{point_A}{point_B}{point_C}{point_D}$ 是正棱锥，其底面 {point_A}{point_B}{point_C}{point_D} 为边长 ${len_a}>0$ 的正方形，顶点 {point_S} 与四个底面顶点等距，侧棱长度为 $|{point_S}{point_A}| = |{point_S}{point_B}| = |{point_S}{point_C}| = |{point_S}{point_D}| = {len_lambda}{len_a}$，其中 ${len_lambda}>\\frac{{\\sqrt{2}}}{{2}}$。记 {point_M}、{point_N} 分别为侧棱 ${point_S}{point_A}$、${point_S}{point_C}$ 的中点。求异面直线 ${point_D}{point_M}$ 与 ${point_B}{point_N}$ 所成角的余弦值。",
    "en_problem": f"Let ${point_S}\\!-\\!{point_A}{point_B}{point_C}{point_D}$ be a regular pyramid with square base {point_A}{point_B}{point_C}{point_D} of side length ${len_a}>0$, where vertex {point_S} is equidistant from all four base vertices. The lateral edge lengths are $|{point_S}{point_A}| = |{point_S}{point_B}| = |{point_S}{point_C}| = |{point_S}{point_D}| = {len_lambda}{len_a}$, where ${len_lambda}>\\frac{{\\sqrt{2}}}{{2}}$. Let {point_M} and {point_N} be the midpoints of lateral edges ${point_S}{point_A}$ and ${point_S}{point_C}$ respectively. Find the cosine of the angle between skew lines ${point_D}{point_M}$ and ${point_B}{point_N}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_6_4({mode}, {azimuth}, {elevation}, '{point_S}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
