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
point_A, point_B, point_C, point_P, point_E, point_D = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_k: float) -> float:
    """计算 cos(phi) 的值（公式：cos(phi) = 2*len_k / √(len_k⁶ + len_k⁴ + 8*len_k² + 4)）"""
    numerator = 2 * len_k
    denominator = math.sqrt(len_k ** 6 + len_k ** 4 + 8 * len_k ** 2 + 4)
    return numerator / denominator


# len_a = a  # 对应原题中AB边的长度参数
len_a = 10
len_k = math.sqrt(2)

# result = calculate(len_k)
# print(f"cos_phi = {result:.6f}")

# Generate random lengths

len_a = round(len_scaling_factor * float(len_a), 2)
len_k = round(random.uniform(1.0, 10.0) * float(len_k), 2)

# Calculate the result
result = calculate(len_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_6_5",
    "type": 2,
    "level": 3,
    "cn_problem": f"设 $\\triangle {point_A}{point_B}{point_C}$ 为直角三角形，$\\angle {point_A}{point_B}{point_C}=90^{{\\circ}}$。取 ${point_A}{point_B}={len_a}>0$，${point_B}{point_C}={len_k}{len_a}$（${len_k}>0$），并令 {point_P} 为空间中一点，使得 ${point_P}{point_A}\\perp$(平面${point_A}{point_B}{point_C}$)，${point_P}{point_A}={point_A}{point_B}={len_a}$。设 {point_E} 为线段 ${point_P}{point_C}$ 的中点；直线 ${point_D}{point_E}$ 为 ${point_P}{point_C}$ 的垂直平分线，并与 ${point_A}{point_C}$ 交于点 {point_D}；以公共棱 ${point_B}{point_D}$ 为棱，记平面 ${point_B}{point_D}{point_E}$ 与平面 ${point_B}{point_D}{point_C}$ 所成的二面角为 $arg_phi$（取锐角）。求 $\\cos arg_phi$。",
    "en_problem": f"Let $\\triangle {point_A}{point_B}{point_C}$ be a right triangle with $\\angle {point_A}{point_B}{point_C}=90^{{\\circ}}$. Set ${point_A}{point_B}={len_a}>0$, ${point_B}{point_C}={len_k}{len_a}$ (${len_k}>0$), and let {point_P} be a point in space such that ${point_P}{point_A}\\perp$(plane ${point_A}{point_B}{point_C}$) and ${point_P}{point_A}={point_A}{point_B}={len_a}$. Let {point_E} be the midpoint of segment ${point_P}{point_C}$; line ${point_D}{point_E}$ is the perpendicular bisector of ${point_P}{point_C}$ and intersects ${point_A}{point_C}$ at point {point_D}; with common edge ${point_B}{point_D}$, let the dihedral angle between plane ${point_B}{point_D}{point_E}$ and plane ${point_B}{point_D}{point_C}$ be $arg_phi$ (acute angle). Find $\\cos arg_phi$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_6_5({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_P}', '{point_E}', '{point_D}')"}, ensure_ascii=False) + "\n")
