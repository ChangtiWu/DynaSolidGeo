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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
def calculate(len_a):
    """
    计算平面将正方体分割后两部分体积之比 V1/V2

    参数:
    len_a (float): 正方体棱长

    返回:
    float: 体积比 V1 / V2
    """
    # 根据题解公式，V1/V2 = 7/17
    return 7 / 17


# 定义题干中的参数
len_a = 4.0  # 正方体棱长

# 验证计算结果
# result = calculate(len_a)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)


# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_17_2",
    "type": 4,
    "level": 2,
    "cn_problem": f"设正方体 {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1} 的棱长为 {len_a}，{point_E} 为 {point_C}{point_C1} 的中点。过 {point_A}、{point_D1}、{point_E} 三点的平面 plain_alpha 将正方体分成两部分，求这两部分的体积之比 \\(\\frac{{volume_V1}}{{volume_V2}}\\)（其中 volume_V1 ≤ volume_V2）。",
    "en_problem": f"Let {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1} be a cube with edge length {len_a}, and let {point_E} be the midpoint of {point_C}{point_C1}. The plane plain_alpha passing through {point_A}, {point_D1}, and {point_E} divides the cube into two parts. Find the ratio of their volumes \\(\\frac{{volume_V1}}{{volume_V2}}\\) (where volume_V1 ≤ volume_V2).",
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
    f.write(json.dumps({json_data["id"]: f"area2_17_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}')"}, ensure_ascii=False) + "\n")
