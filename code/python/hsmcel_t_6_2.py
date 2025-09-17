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
    计算正方体中平面 CEB1 与平面 D1FB1 所成二面角的平面角正弦值

    参数:
    len_a (float): 正方体棱长

    返回:
    float: 正弦值
    """
    return math.sqrt(3) / 2


# 题干给定的数值
len_a = 1.0  # 棱长，可按比例赋值

# 验证输出
# result = calculate(len_a)
# print(f"正弦值: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_6_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"已知正方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}的棱长为{len_a}（{len_a} > 0），{point_E}、{point_F}分别是{point_A}{point_B}、{point_A}{point_A1}的中点，则平面{point_C}{point_E}{point_B1}与平面{point_D1}{point_F}{point_B1}所成二面角的平面角的正弦值是________。",
    "en_problem": f"Given a cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} with edge length {len_a} ({len_a} > 0), where {point_E} and {point_F} are the midpoints of {point_A}{point_B} and {point_A}{point_A1} respectively, find the sine value of the dihedral angle between planes {point_C}{point_E}{point_B1} and {point_D1}{point_F}{point_B1}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_6_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
