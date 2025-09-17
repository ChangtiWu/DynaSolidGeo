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
point_A, point_B, point_C, point_D, point_P = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math

def calculate():
    """
    计算平面 PCB 与平面 PCD 所成夹角的余弦值

    返回:
    float: 余弦值
    """
    # 已知结果
    return 3 / 13


# 题干给定的数值
len_a = 2.0      # AB
len_b = 2 * math.sqrt(3)  # AD
len_PC = math.sqrt(10)
R = 2.0  # 外接球半径

# 验证输出
# result = calculate()
# print(f"余弦值: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_PC = round(len_scaling_factor * float(len_PC), 2)
R = round(len_scaling_factor * float(R), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "zht_10_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在矩形 {point_A}{point_B}{point_C}{point_D} 中，{point_A}{point_B} = {len_a}，{point_A}{point_D} = {len_b}，沿对角线 {point_B}{point_D} 折叠使点 {point_A} 到达点 {point_P}。已知 {point_P}{point_C} = {len_PC}，三棱锥 {point_P}-{point_B}{point_C}{point_D} 的外接球半径 R = {R}，故 {point_B}{point_D} = 2R，满足 {len_a}^2 + {len_b}^2 = {point_B}{point_D}^2。求平面 {point_P}{point_C}{point_B} 与平面 {point_P}{point_C}{point_D} 夹角的余弦值。",
    "en_problem": f"In rectangle {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B} = {len_a}, {point_A}{point_D} = {len_b}, fold along diagonal {point_B}{point_D} so that point {point_A} moves to point {point_P}. Given that {point_P}{point_C} = {len_PC}, the circumscribed sphere radius R = {R}, so {point_B}{point_D} = 2R, satisfying {len_a}^2 + {len_b}^2 = {point_B}{point_D}^2. Find the cosine value of the angle between plane {point_P}{point_C}{point_B} and plane {point_P}{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"zht_10_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}')"}, ensure_ascii=False) + "\n")
