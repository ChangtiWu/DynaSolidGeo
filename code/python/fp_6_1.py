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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_M = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math

def calculate(len_edge):
    """
    计算正方体表面最短路径

    参数:
    len_edge (float): 正方体的棱长

    返回:
    float: 从 A 到 M 的最短路径长度
    """
    # 公式: shortest = (edge * sqrt(13)) / 2
    return (len_edge * math.sqrt(13)) / 2


# 题干给定的数值
len_edge = 2.0

# 验证输出
#result = calculate(len_edge)
#print(f"计算结果: {result:.6f}")


# Generate random lengths
len_edge = round(len_scaling_factor * float(len_edge), 2)

# Calculate the result
result = calculate(len_edge)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fp_6_1",
    "type": 3,
    "level": 1,
    "cn_problem": f"设正方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 的棱长为 {len_edge}，点 {point_M} 是棱 {point_C}{point_C1} 的中点（即  len_CM  = \\frac{{{len_edge}}}{{2}}），求沿正方体表面从点 {point_A} 到点 {point_M} 的最短路程。",
    "en_problem": f"Let the edge length of cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} be {len_edge}, and point {point_M} is the midpoint of edge {point_C}{point_C1} (i.e.,  len_CM  = \\frac{{{len_edge}}}{{2}}). Find the shortest distance along the cube's surface from point {point_A} to point {point_M}.",
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
    f.write(json.dumps({json_data["id"]: f"fp_6_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_M}')"}, ensure_ascii=False) + "\n")
