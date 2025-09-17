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
point_P, point_A, point_B, point_C = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math


def calculate(arg_theta: float) -> float:
    """计算 cos_phi 的值（公式：cos_phi = cos(arg_theta)·√(2/(1+cos(arg_theta)))）"""
    cos_arg = math.cos(arg_theta)
    denominator = 1 + cos_arg

    if denominator == 0:
        raise ValueError("分母1+cos(arg_theta)不能为0（当arg_theta=π时触发）")

    sqrt_term = math.sqrt(2 / denominator)
    return cos_arg * sqrt_term


arg_theta = math.pi / 3

# result = calculate(arg_theta)
# print(f"cos_phi = {result:.6f}")
# Generate random lengths

arg_theta = round(random.uniform(math.pi / 4, math.pi * 2 / 5), 2)


# Calculate the result
result = calculate(arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_6_3",
    "type": 2,
    "level": 2,
    "cn_problem": f"设从同一点 {point_P} 出发的三条射线 ${point_P}{point_A}$、${point_P}{point_B}$、${point_P}{point_C}$ 满足 $\\angle({point_A}{point_P},{point_B}{point_P})=\\angle({point_B}{point_P},{point_C}{point_P})=\\angle({point_C}{point_P},{point_A}{point_P})={arg_theta}$，其中 $0<{arg_theta}<\\arccos(-\\frac{1}{2})$。求直线 ${point_P}{point_C}$ 与平面 ${point_P}{point_A}{point_B}$ 所成锐角的余弦值。",
    "en_problem": f"Let three rays ${point_P}{point_A}$, ${point_P}{point_B}$, ${point_P}{point_C}$ emanate from the same point {point_P} such that $\\angle({point_A}{point_P},{point_B}{point_P})=\\angle({point_B}{point_P},{point_C}{point_P})=\\angle({point_C}{point_P},{point_A}{point_P})={arg_theta}$, where $0<{arg_theta}<\\arccos(-\\frac{1}{2})$ (approximately $120°$). Find the cosine of the acute angle between line ${point_P}{point_C}$ and plane ${point_P}{point_A}{point_B}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_6_3({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}')"}, ensure_ascii=False) + "\n")
