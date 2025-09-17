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
point_A, point_B, point_C, point_D, point_F = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math

def calculate():
    """
    计算平面 FAD 与平面 FBC 所成锐二面角的余弦值

    返回:
    float: 余弦值
    """
    # 已知结果
    return 1 / 3


# 题干给定的数值
len_a = 4.0   # 正方形边长及等边三角形边长
# 正方形 ABCD，等边三角形 BCF
# 折起形成四棱锥 F-ABCD
# 二面角 F-BC-A 的正切值 = √2

# 验证输出
# result = calculate()
# print(f"余弦值: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "zht_8_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"设正方形 {point_A}{point_B}{point_C}{point_D} 和等边三角形 {point_B}{point_C}{point_F} 的边长均为 {len_a}，求平面 {point_F}{point_A}{point_D} 与平面 {point_F}{point_B}{point_C} 所成锐二面角的余弦值。",
    "en_problem": f"Let the side lengths of square {point_A}{point_B}{point_C}{point_D} and equilateral triangle {point_B}{point_C}{point_F} both be {len_a}, find the cosine value of the acute dihedral angle formed by plane {point_F}{point_A}{point_D} and plane {point_F}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"zht_8_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_F}')"}, ensure_ascii=False) + "\n")
