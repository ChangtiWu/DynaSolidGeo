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
point_A, point_B, point_C, point_D, point_S = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_mu: float, len_lambda: float) -> float:
    """计算 cos(arg_theta) 的值（公式：cos(arg_theta) = len_mu / √[len_mu²((len_lambda-1)²+1) + len_lambda²]）"""
    numerator = len_mu
    denominator = math.sqrt(
        len_mu ** 2 * ((len_lambda - 1) ** 2 + 1) + len_lambda ** 2
    )
    return numerator / denominator


len_a = 1.0
len_mu = 1.0
len_lambda = 0.5

# result = calculate(len_mu, len_lambda)
# print(f"cos_arg_theta = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_mu, len_lambda)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_s_6_2_3",
    "type": 2,
    "level": 3,
    "cn_problem": f"设 ${point_A}{point_B}{point_C}{point_D}$ 为直角梯形，满足 $\\angle {point_A}{point_B}{point_C}=\\angle {point_B}{point_A}{point_D}=90^{{\\circ}}$，${point_A}{point_B}={point_B}{point_C}={len_a}>0$，${point_A}{point_D}={len_lambda}{len_a}$（$0<{len_lambda}<+\\infty$）。取点 {point_S} 使 ${point_S}{point_A}\\perp$(平面${point_A}{point_B}{point_C}{point_D}$)，${point_S}{point_A}={len_mu}*{len_a}$（${len_mu}>0$）。求平面 ${point_S}{point_A}{point_B}$ 与平面 ${point_S}{point_C}{point_D}$ 所成锐二面角 ${{arg_theta}}$ 的余弦值 $\\cos{{arg_theta}}$。",
    "en_problem": f"Let ${point_A}{point_B}{point_C}{point_D}$ be a right trapezoid satisfying $\\angle {point_A}{point_B}{point_C}=\\angle {point_B}{point_A}{point_D}=90^{{\\circ}}$, ${point_A}{point_B}={point_B}{point_C}={len_a}>0$, ${point_A}{point_D}={len_lambda}{len_a}$ ($0<{len_lambda}<+\\infty$). Take point {point_S} such that ${point_S}{point_A}\\perp$(plane ${point_A}{point_B}{point_C}{point_D}$) and ${point_S}{point_A}={len_mu}*{len_a}$ (${len_mu}>0$). Find the cosine of the acute dihedral angle ${{arg_theta}}$ between plane ${point_S}{point_A}{point_B}$ and plane ${point_S}{point_C}{point_D}$: $\\cos{{arg_theta}}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_s_6_2_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_S}')"}, ensure_ascii=False) + "\n")
