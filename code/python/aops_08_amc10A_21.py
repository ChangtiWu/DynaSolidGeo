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
point_A, point_C, point_B, point_D = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math

def calculate(len_a: float) -> float:
    """计算面积函数值（area_function = (√6/2)·len_a²）"""
    return (math.sqrt(6) / 2) * (len_a ** 2)


len_a = 1.0


# result = calculate(len_a)
# print(f"area_function = {result:.6f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_08_amc10A_21",
    "type": 4,
    "level": 1,
    "cn_problem": f"设一正方体，棱长为 ${len_a}>0$。取其一条空间对角线的两个端点 ${point_A}(0,0,0), {point_C}({len_a},{len_a},{len_a})$，以及与该对角线平行且互为对边的两条棱的中点 ${point_B}\\!\\left(0,{len_a},\\frac{{len_a}}{2}\\right), {point_D}\\!\\left({len_a},0,\\frac{{len_a}}{2}\\right)$。过四点 ${point_A},{point_B},{point_C},{point_D}$ 作平面，与正方体相交所得四边形仍记为 ${point_A}{point_B}{point_C}{point_D}$。求其面积。",
    "en_problem": f"Consider a cube with edge length ${len_a}>0$. Take the two endpoints of one space diagonal: ${point_A}(0,0,0), {point_C}({len_a},{len_a},{len_a}), and the midpoints of two opposite edges parallel to this diagonal: ${point_B}\\!\\left(0,{len_a},\\frac{{len_a}}{2}\\right), {point_D}\\!\\left({len_a},0,\\frac{{len_a}}{2}\\right)$. A plane is made through the four points ${point_A},{point_B},{point_C},{point_D}$, intersecting the cube to form quadrilateral ${point_A}{point_B}{point_C}{point_D}$. Find its area.",
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
    f.write(json.dumps({json_data["id"]: f"aops_08_amc10A_21({mode}, {azimuth}, {elevation}, '{point_A}', '{point_C}', '{point_B}', '{point_D}')"}, ensure_ascii=False) + "\n")
