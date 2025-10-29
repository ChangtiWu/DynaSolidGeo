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
point_P, point_A, point_B, point_C, point_E, point_O = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_r, len_h):
    """
    计算 V_{P-AOC} 的值，公式为 V_{P-AOC} = (1/6) * len_r² * len_h
    
    参数:
        len_r (float/int): 长度参数 r（通常表示半径或类似长度）
        len_h (float/int): 长度参数 h（通常表示高度或类似长度）
    
    返回:
        float: 计算结果 V_{P-AOC}
    """
    return (1/6) * (len_r ** 2) * len_h

len_r = 1
len_h = 2

# print(calculate(len_r, len_h))
# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)
len_r = round(len_scaling_factor * float(len_r), 2)

# Calculate the result
result = calculate(len_r, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_5_6_1",
    "type": 5,
    "level": 2,
    "cn_problem": f"如图，圆锥的顶点为{point_P}，底面的一条直径为{point_A}{point_B}，{point_C}为半圆弧{point_A}{point_B}的中点，{point_E}为劣弧{point_C}{point_B}的中点。已知圆锥的高{point_P}{point_O} = {len_h}，底面半径{point_O}{point_A} = {len_r}，求三棱锥{point_P}-{point_A}{point_O}{point_C}的体积。",
    "en_problem": f"As shown in the figure, the vertex of the cone is {point_P}, a diameter of the base is {point_A}{point_B}, {point_C} is the midpoint of the semicircle arc {point_A}{point_B}, {point_E} is the midpoint of the minor arc {point_C}{point_B}. Given the height of the cone {point_P}{point_O} = {len_h}, the base radius {point_O}{point_A} = {len_r}, find the volume of the triangular pyramid {point_P}-{point_A}{point_O}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_5_6_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_E}', '{point_O}')"}, ensure_ascii=False) + "\n")
