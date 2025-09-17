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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1 = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math

def calculate(len_d, len_l):
    """
    计算正四棱柱 ABCD-A1B1C1D1 的体积

    参数:
    len_d (float): 底面正方形的对角线长度
    len_l (float): 侧棱长度（大于对角线）

    返回:
    float: 正四棱柱体积
    """
    return (len_d**2 / 2) * math.sqrt(len_l**2 - len_d**2)


# 题干给定的数值
len_d = 4 * math.sqrt(2)  # BD
len_l = 9                  # DB1

# 验证输出
#volume = calculate(len_d, len_l)
#print(f"正四棱柱体积: {volume:.6f}")

# Generate random lengths
len_d = round(len_scaling_factor * float(len_d), 2)
len_l = round(len_scaling_factor * float(len_l), 2)

# Calculate the result
result = calculate(len_d, len_l)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee25_3_1",
    "type": 5,
    "level": 1,
    "cn_problem": f"在正四棱柱 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 中，底面正方形的对角线 {len_d}，线段 {len_l}（其中 {len_l}>{len_d}），求该正四棱柱的体积。",
    "en_problem": f"In the right square prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, the diagonal of the base square is {len_d}, and the segment {len_l} (where {len_l}>{len_d}). Find the volume of the prism.",
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
    f.write(json.dumps({json_data["id"]: f"ncee25_3_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}')"}, ensure_ascii=False) + "\n")
