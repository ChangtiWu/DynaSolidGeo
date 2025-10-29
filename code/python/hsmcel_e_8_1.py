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
point_S, point_A, point_B, point_C, point_O = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_p, len_h):
    """计算len_d的值"""
    return (2 * len_p ** 2 - len_h ** 2) / (4 * math.sqrt(len_p ** 2 - len_h ** 2 / 4))


len_p = 2.0
len_h = 2.0

# print(calculate(len_p, len_h))

# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)
len_p = round(len_scaling_factor * float(len_p), 2)

# Calculate the result
result = calculate(len_p, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_8_1",
    "type": 3,
    "level": 2,
    "cn_problem": f"设三棱锥 ${point_S}\\!-\\!{point_A}{point_B}{point_C}$ 满足：1. 底面 $\\triangle {point_A}{point_B}{point_C}$ 为等腰直角三角形，且以斜边 ${point_A}{point_B}$ 为斜边，则 ${point_A}{point_B}={len_h}>0$，${point_A}{point_C}={point_B}{point_C}=\\frac{{{len_h}}}{{\\sqrt{2}}}$；2. 三条侧棱等长 ${point_S}{point_A} = {point_S}{point_B} = {point_S}{point_C} = {len_p}$，${len_p}>\\frac{{{len_h}}}{{\\sqrt{2}}}$。已知四点 ${point_S},{point_A},{point_B},{point_C}$ 共躺在以 {point_O} 为球心、半径 ${len_p}$ 的同一球面上。求球心 {point_O} 到平面 ${point_A}{point_B}{point_C}$ 的距离。",
    "en_problem": f"Let triangular pyramid ${point_S}\\!-\\!{point_A}{point_B}{point_C}$ satisfy: 1. Base $\\triangle {point_A}{point_B}{point_C}$ is an isosceles right triangle with hypotenuse ${point_A}{point_B}$, so ${point_A}{point_B}={len_h}>0$, ${point_A}{point_C}={point_B}{point_C}=\\frac{{{len_h}}}{{\\sqrt{2}}}$; 2. Three lateral edges are equal: ${point_S}{point_A} = {point_S}{point_B} = {point_S}{point_C} = {len_p}$, ${len_p}>\\frac{{{len_h}}}{{\\sqrt{2}}}$. Given that four points ${point_S},{point_A},{point_B},{point_C}$ all lie on a sphere with center {point_O} and radius ${len_p}$. Find the distance from sphere center {point_O} to plane ${point_A}{point_B}{point_C}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_8_1({mode}, {azimuth}, {elevation}, '{point_S}', '{point_A}', '{point_B}', '{point_C}', '{point_O}')"}, ensure_ascii=False) + "\n")
