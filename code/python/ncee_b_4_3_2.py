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
point_A, point_B, point_C, point_D, point_E, point_F, point_G, point_H = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a):
    """
    计算体积 V

    参数:
        len_a (float): 边长 a 的长度

    返回:
        float: 体积 V 的计算结果

    公式:
        V = (5√3/12) * len_a³
    """
    # 计算常数系数
    constant = 5 * math.sqrt(3) / 12

    # 返回最终结果
    return constant * (len_a ** 3)

# 计算当边长为 2 时的体积
len_a = 8.0
# volume = calculate(len_a)
#
# print(f"体积 V = {volume:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_3_2",
    "type": 5,
    "level": 2,
    "cn_problem": f"在平面直角坐标系中，正方形 {point_A}{point_B}{point_C}{point_D} 的顶点坐标为 {point_A}(0,0,0)，{point_B}({len_a},0,0)，{point_C,}({len_a}{len_a},0)，{point_D}(0,{len_a},0)。以 {point_A}{point_B}，{point_B}{point_C}，{point_C}{point_D}，{point_D}{point_A} 为底边，在与 xy 平面垂直的平面内各作一个边长为 {len_a} 的正三角形 \\triangle {point_E}{point_A}{point_B}，\\triangle {point_F}{point_B}{point_C}，\\triangle {point_G}{point_C}{point_D}，\\triangle {point_H}{point_D}{point_A}，其顶点分别记为 {point_E}，{point_F}，{point_G}，{point_H}。连接 {point_E}-{point_F}-{point_G}-{point_H}-{point_E} 形成上底面，得到一个封闭多面体。求该包装盒的体积。",
    "en_problem": f"In the Cartesian coordinate system, square {point_A}{point_B}{point_C}{point_D} has vertices {point_A}(0,0,0), {point_B}({len_a},0,0), {point_C}({len_a},{len_a},0), {point_D}(0,{len_a},0). Using {point_A}{point_B}, {point_B}{point_C}, {point_C}{point_D}, {point_D}{point_A} as bases, construct equilateral triangles \\triangle {point_E}{point_A}{point_B}, \\triangle {point_F}{point_B}{point_C}, \\triangle {point_G}{point_C}{point_D}, \\triangle {point_H}{point_D}{point_A} with side length {len_a} in planes perpendicular to the xy-plane, with vertices {point_E}, {point_F}, {point_G}, {point_H} respectively. Connect {point_E}-{point_F}-{point_G}-{point_H}-{point_E} to form the upper base, creating a closed polyhedron. Find the volume of this packaging box.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_3_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_G}', '{point_H}')"}, ensure_ascii=False) + "\n")
