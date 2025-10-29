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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_P = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算三棱锥 P - AA1D1 的外接球表面积

    参数:
    len_a (float): 正方体的棱长

    返回:
    float: 外接球表面积
    """
    # 根据题目给出的公式 area_sphere = (153/64) * pi * len_a^2
    return (153 / 64) * math.pi * len_a ** 2


# 定义题干中的参数
len_a = 4.0   # 正方体棱长

# 验证计算结果
#result = calculate(len_a)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_17_3",
    "type": 4,
    "level": 2,
    "cn_problem": f"在棱长为 {len_a} 的正方体 {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1} 中，{point_E} 为 {point_C}{point_C1} 的中点，平面 plain_alpha 过 {point_A}、{point_D1}、{point_E} 三点。若点 {point_P} 是侧面 {point_B}{point_C}{point_C1}{point_B1} 内的动点，且 {point_A1}{point_P} ∥ plain_alpha，当 {point_A1}{point_P} 最小时，求三棱锥 {point_P} - {point_A}{point_A1}{point_D1} 的外接球的表面积。",
    "en_problem": f"In a cube {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1} with edge length {len_a}, let {point_E} be the midpoint of {point_C}{point_C1}. The plane plain_alpha passes through {point_A}, {point_D1}, and {point_E}. Let {point_P} be a moving point on the face {point_B}{point_C}{point_C1}{point_B1}, and suppose {point_A1}{point_P} ∥ plain_alpha. When {point_A1}{point_P} is minimal, find the surface area of the circumscribed sphere of the tetrahedron {point_P} - {point_A}{point_A1}{point_D1}.",
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
    f.write(json.dumps({json_data["id"]: f"area2_17_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_P}')"}, ensure_ascii=False) + "\n")
