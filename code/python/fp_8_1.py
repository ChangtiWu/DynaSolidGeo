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
point_P, point_B, point_C, point_A = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math

def calculate(len_diameter, len_height):
    """
    计算圆柱容器外壁 A 到内壁 P 的最短路程

    参数:
    len_diameter (float): 圆柱底面直径
    len_height (float): 圆柱高

    返回:
    float: 最短路径长度
    """
    # 公式: shortest = 0.5 * sqrt( (π * d)^2 + 9 * h^2 )
    return 0.5 * math.sqrt((math.pi * len_diameter) ** 2 + 9 * (len_height ** 2))


# 题干给定的数值
len_diameter = 2.0
len_height = 2.0

# 验证输出
#result = calculate(len_diameter, len_height)
#print(f"计算结果: {result:.6f}")


# Generate random lengths
len_diameter = round(len_scaling_factor * float(len_diameter), 2)
len_height = round(len_scaling_factor * float(len_height), 2)

# Calculate the result
result = calculate(len_diameter, len_height)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fp_8_1",
    "type": 3,
    "level": 1,
    "cn_problem": f"设圆柱开口容器的轴截面为长 {len_diameter}（底面直径）、宽 {len_height}（圆柱高）的矩形，点 {point_P} 是母线 {point_B}{point_C} 的中点（即  len_BP  = \\frac{{{len_height}}}{{2}}）。求外壁 {point_A} 到内壁 {point_P} 的最短路程。",
    "en_problem": f"Let the axial cross-section of an open cylindrical container be a rectangle with length {len_diameter} (base diameter) and width {len_height} (cylinder height), and point {point_P} is the midpoint of generatrix {point_B}{point_C} (i.e.,  len_BP  = \\frac{{{len_height}}}{{2}}). Find the shortest distance from outer wall {point_A} to inner wall {point_P}.",
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
    f.write(json.dumps({json_data["id"]: f"fp_8_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_B}', '{point_C}', '{point_A}')"}, ensure_ascii=False) + "\n")
