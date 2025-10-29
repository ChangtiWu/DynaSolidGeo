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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D, point_E = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
def calculate(len_t: float) -> float:
    """计算 len_m 的表达式值（len_m = (1 - len_t)/len_t）"""
    return (1 - len_t) / len_t


len_t = 0.5

# result = calculate(len_t)
# print(f"len_m = {result:.6f}")
# Generate random lengths
len_t = round(len_scaling_factor * float(len_t), 2)

# Calculate the result
result = calculate(len_t)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_2_2",
    "type": 7,
    "level": 2,
    "cn_problem": f"在正三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中，设点 {point_D} $\\in$ {point_B}{point_C}，$\\frac{{ {point_B}{point_D} }}{{ {point_D}{point_C} }}={len_t}:(1-{len_t})$，$0<{len_t}<1$，点 {point_E} $\\in$ {point_A}{point_A1}，$\\frac{{ {point_A}{point_E} }}{{ {point_E}{point_A1} }}=len_m>0$。若直线 {point_A}{point_D} 与平面 {point_B1}{point_C}{point_E} 平行，求len_m。",
    "en_problem": f"In a regular triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, let point {point_D} $\\in$ {point_B}{point_C} with $\\frac{{ {point_B}{point_D} }}{{ {point_D}{point_C} }}={len_t}:(1-{len_t})$, $0<{len_t}<1$, and point {point_E} $\\in$ {point_A}{point_A1} with $\\frac{{ {point_A}{point_E} }}{{ {point_E}{point_A1} }}=len_m>0$. If line {point_A}{point_D} is parallel to plane {point_B1}{point_C}{point_E}, find len_m.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_2_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
