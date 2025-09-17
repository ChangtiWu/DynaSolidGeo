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
point_Q, point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_u, len_a, len_v):
    """计算param_cos的值（两个分数相等的结果，需满足约束条件：len_u > len_a/2，len_v²=len_u²+len_a²）"""
    # 计算第一个分数：√(4len_u² - len_a²) / √(8len_u² - len_a²)
    numerator1 = math.sqrt(4 * (len_u ** 2) - (len_a ** 2))
    denominator1 = math.sqrt(8 * (len_u ** 2) - (len_a ** 2))
    fraction1 = numerator1 / denominator1

    return fraction1


# 测试示例（满足约束条件：len_u=2 > 2/2=1，len_v²=2²+2²=8）
len_u = math.sqrt(5)
len_a = 2
len_v = 3.0

# print(calculate(len_u, len_a, len_v))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_u = round(len_scaling_factor * float(len_u), 2)
len_v = round(len_scaling_factor * float(len_v), 2)

# Calculate the result
result = calculate(len_u, len_a, len_v)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_12_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"如图，在四棱锥 {point_Q}-{point_A}{point_B}{point_C}{point_D} 中，底面 {point_A}{point_B}{point_C}{point_D} 为边长 {len_a}>0 的正方形；设 {point_Q}{point_D}={len_u}>0，{point_Q}{point_C}={len_v}>{len_u}；并满足 {len_v}^2={len_u}^2+{len_a}^2（可由已知边长推出）。求二面角 {point_B}-{point_Q}{point_D}-{point_A} 的余弦值。",
    "en_problem": f"As shown, in quadrilateral pyramid {point_Q}-{point_A}{point_B}{point_C}{point_D}, the base {point_A}{point_B}{point_C}{point_D} is a square with side length {len_a}>0; let {point_Q}{point_D}={len_u}>0, {point_Q}{point_C}={len_v}>{len_u}; and satisfy {len_v}^2={len_u}^2+{len_a}^2 (derivable from given edge lengths). Find the cosine of dihedral angle {point_B}-{point_Q}{point_D}-{point_A}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_12_2({mode}, {azimuth}, {elevation}, '{point_Q}', '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
