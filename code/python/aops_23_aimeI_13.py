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

# Add result calculation code
import math


def calculate(param_a: float, param_b: float) -> float:
    """计算函数 f(param_a, param_b) 的值"""
    # 计算分子和分母的多项式部分（简化后形式）
    numerator_poly = 3 * param_b ** 2 + 2 * param_a * param_b - param_a ** 2
    denominator_poly = 3 * param_a ** 2 + 2 * param_a * param_b - param_b ** 2

    # 计算平方根部分和整体比例
    sqrt_term = math.sqrt(numerator_poly / denominator_poly)
    return (param_a / param_b) * sqrt_term


param_a = 21
param_b = 31

# result = calculate(param_a, param_b)
# print(f"f(2, 3) = {result:.6f}")
# Generate random lengths
param_a = round(len_scaling_factor * float(param_a), 2)
param_b = round(len_scaling_factor * float(param_b), 2)

# Calculate the result
result = calculate(param_a, param_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_23_aimeI_13",
    "type": 5,
    "level": 3,
    "cn_problem": f"设 ${param_a}$、${param_b}$ 为满足 $0<{param_a}<{param_b}<3*{param_a}$ 的正实数。已知有两个不全等的平行六面体，它们的每一个面都是同一个菱形。该菱形两条对角线的长度分别为 $\\sqrt{{param_a}}$ 与 $\\sqrt{{param_b}}$。因为第三条棱可以取两种不同的倾斜方向，所以可得到体积不同的两种平行六面体。记体积较大的为 $V_{{\\max}}$，较小的为 $V_{{\\min}}$。求体积比 $\\frac{{V_{{\\\max}}}}{{V_{{\\\min}}}}$ 。",
    "en_problem": f"Let ${param_a}$ and ${param_b}$ be positive real numbers satisfying $0<{param_a}<{param_b}<3*{param_a}$. There are two non-congruent parallelepipeds, each face of which is the same rhombus. The lengths of the two diagonals of this rhombus are $\\sqrt{{param_a}}$ and $\\sqrt{{param_b}}$ respectively. Since the third edge can take two different inclination directions, we can obtain two parallelepipeds with different volumes. Let $V_{{\\max}}$ be the larger volume and $V_{{\\min}}$ be the smaller one. Find the volume ratio $\\frac{{V_{{\\\max}}}}{{V_{{\\\min}}}}$.",
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
    f.write(json.dumps({json_data["id"]: f"aops_23_aimeI_13({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
