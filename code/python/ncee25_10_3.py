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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_F = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算正方体中三棱锥 D-FBE 的体积

    参数:
    len_a (float): 正方体棱长

    返回:
    float: 三棱锥体积
    """
    return len_a**3 / 6


# 题干给定的数值
len_a = 4.0  # 正方体棱长

# 验证输出
# volume = calculate(len_a)
# print(f"三棱锥体积: {volume:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee25_10_3",
    "type": 5,
    "level": 2,
    "cn_problem": f"设正方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}的棱长为{len_a}，{point_E}、{point_F}分别为{point_A1}{point_D1}、{point_C1}{point_B1}的中点，求三棱锥{point_D}-{point_F}{point_B}{point_E}的体积。",
    "en_problem": f"Let the edge length of cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} be {len_a}, {point_E}, {point_F} are the midpoints of {point_A1}{point_D1}, {point_C1}{point_B1} respectively. Find the volume of tetrahedron {point_D}-{point_F}{point_B}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee25_10_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
