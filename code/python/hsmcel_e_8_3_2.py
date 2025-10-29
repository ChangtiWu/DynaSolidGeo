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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_s, arg_beta):
    """计算总面积"""
    term1 = (3 * len_s ** 2) / 2 * math.tan(arg_beta)
    term2 = (3 * len_s ** 2) / (4 * math.cos(arg_beta))
    term3 = (math.sqrt(3) / 2) * len_s ** 2
    return term1 + term2 + term3


len_s = 2
arg_beta = math.pi / 4  # 45度对应的弧度值

# print(calculate(len_s, arg_beta))

# Generate random lengths
len_s = round(len_scaling_factor * float(len_s), 2)
arg_beta = round(len_scaling_factor * float(arg_beta), 2)

# Calculate the result
result = calculate(len_s, arg_beta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_8_3_2",
    "type": 4,
    "level": 3,
    "cn_problem": f"已知斜三棱柱 ${point_A}{point_B}{point_C}\\!-\\!{point_A1}{point_B1}{point_C1}$ 的底面 $\\triangle {point_A}{point_B}{point_C}$ 为边长 ${len_s}>0$ 的正三角形，顶点 ${point_A1}$ 在底面上的射影 {point_D} 为 ${point_B}{point_C}$ 的中点，且 $\\angle {point_A1}{point_A}{point_B}=\\angle {point_A1}{point_A}{point_C}={arg_beta}$。记平移向量 $\\vec{{v}}=\\overrightarrow{{{point_A}{point_A1}}}=\\overrightarrow{{{point_B}{point_B1}}}=\\overrightarrow{{{point_C}{point_C1}}}$。求该斜三棱柱的全表面积。",
    "en_problem": f"Given oblique triangular prism ${point_A}{point_B}{point_C}\\!-\\!{point_A1}{point_B1}{point_C1}$ with base $\\triangle {point_A}{point_B}{point_C}$ being an equilateral triangle of side length ${len_s}>0$, vertex ${point_A1}$'s projection on the base is {point_D}, the midpoint of ${point_B}{point_C}$, and $\\angle {point_A1}{point_A}{point_B}=\\angle {point_A1}{point_A}{point_C}={arg_beta}$. Let translation vector $\\vec{{v}}=\\overrightarrow{{{point_A}{point_A1}}}=\\overrightarrow{{{point_B}{point_B1}}}=\\overrightarrow{{{point_C}{point_C1}}}$. Find the total surface area of the oblique triangular prism.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_8_3_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}')"}, ensure_ascii=False) + "\n")
