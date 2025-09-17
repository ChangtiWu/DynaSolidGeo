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
point_A, point_B, point_C, point_D, point_O = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_a, len_b):
    """计算len_r关于len_a和len_b的表达式"""
    numerator = abs(len_a * len_b * (len_a + len_b) - math.sqrt(6) * (len_a * len_b) ** 1.5)
    denominator = abs(len_a ** 2 - 4 * len_a * len_b + len_b ** 2)
    return numerator / denominator


# 测试示例
len_a = 2.0
len_b = 3.0

# print(calculate(len_a, len_b))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_8_5",
    "type": 3,
    "level": 3,
    "cn_problem": f"已知空间中有4个球，其中2个球半径同为 ${len_a}>0$，记球心 {point_A},{point_B}；另外2个球半径同为 ${len_b}>0$，记球心 {point_C},{point_D}。每个球都与其余3球外切，于是 ${point_A}{point_B}=2*{len_a}$，${point_C}{point_D}=2*{len_b}$，${point_A}{point_C}={point_A}{point_D}={point_B}{point_C}={point_B}{point_D}={len_a}+{len_b}$。现有第三个小球，以 {point_O} 为心、半径 $len_r>0$，与这4个球皆外切。求 $len_r$ 。",
    "en_problem": f"Given 4 spheres in space, where 2 spheres have the same radius ${len_a}>0$ with centers {point_A},{point_B}, and the other 2 spheres have the same radius ${len_b}>0$ with centers {point_C},{point_D}. Each sphere is externally tangent to the other 3 spheres, so ${point_A}{point_B}=2*{len_a}$, ${point_C}{point_D}=2*{len_b}$, ${point_A}{point_C}={point_A}{point_D}={point_B}{point_C}={point_B}{point_D}={len_a}+{len_b}$. There is a fifth small sphere with center {point_O} and radius $len_r>0$ that is externally tangent to all 4 spheres. Find the $len_r$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_8_5({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}')"}, ensure_ascii=False) + "\n")
