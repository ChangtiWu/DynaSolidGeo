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
point_P, point_O, point_C, point_A, point_B, point_D = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_L, len_rho):
    """
    计算球被平面 PCD 截得的截面圆面积

    参数:
    len_L (float): 圆锥母线长
    len_rho (float): 球半径

    返回:
    float: 截面圆面积
    """
    return math.pi * (len_rho**2 - 3 * (len_L**2) / 28)


# ====== 示例验证 ======
len_L = 4     # 已知圆锥侧面展开半圆半径
len_rho = 2   # 球半径



# Generate random lengths
len_L = round(len_scaling_factor * float(len_L), 2)
len_rho = round(len_scaling_factor * float(len_rho), 2)

# Calculate the result
result = calculate(len_L, len_rho)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fp_7_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"圆锥侧面展开图是以点{point_P}为圆心、半径为{len_L}的半圆。记圆锥底面圆心为{point_O}，底半径为len_r，高为len_h（母线长{point_P}{point_O} = {len_L}，且{len_L}^2 = len_r^2 + len_h^2）。设点{point_C}是弧{point_A}{point_B}的中点，点{point_D}是弧{point_A}{point_C}的中点。以{point_O}为球心、半径为{len_rho}的球被平面{point_P}{point_C}{point_D}截得一个圆。求该截面面积。",
    "en_problem": f"The lateral surface development of a cone is a semicircle with center {point_P} and radius {len_L}. Let the cone's base center be {point_O}, base radius be len_r, and height be len_h (generatrix length {point_P}{point_O} = {len_L}, and {len_L}^2 = len_r^2 + len_h^2). Point {point_C} is the midpoint of arc {point_A}{point_B}, and point {point_D} is the midpoint of arc {point_A}{point_C}. A sphere with center {point_O} and radius {len_rho} is intersected by plane {point_P}{point_C}{point_D} to form a circle. Find the area of this cross-section.",
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
    f.write(json.dumps({json_data["id"]: f"fp_7_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_O}', '{point_C}', '{point_A}', '{point_B}', '{point_D}')"}, ensure_ascii=False) + "\n")
