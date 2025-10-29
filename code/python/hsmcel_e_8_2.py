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
point_P, point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_k):
    """计算len_h关于len_k的表达式"""
    return (math.sqrt(5) - 1) / 2 * len_k


len_k = 1.0

# print(calculate(len_k))

# Generate random lengths
len_k = round(len_scaling_factor * float(len_k), 2)

# Calculate the result
result = calculate(len_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_8_2",
    "type": 3,
    "level": 3,
    "cn_problem": f"在四棱锥 ${point_P}\\!-\\!{point_A}{point_B}{point_C}{point_D}$ 中，四个侧面都是腰长为 ${len_k}>0$ 的等腰直角三角形，并满足 $\\angle {point_A}{point_P}{point_B}=\\angle {point_A}{point_P}{point_D}=\\angle {point_P}{point_B}{point_C}=\\angle {point_P}{point_D}{point_C}=90^{{\\circ}}$。求四棱锥的高。",
    "en_problem": f"In pyramid ${point_P}\\!-\\!{point_A}{point_B}{point_C}{point_D}$, all four lateral faces are isosceles right triangles with leg length ${len_k}>0$, satisfying $\\angle {point_A}{point_P}{point_B}=\\angle {point_A}{point_P}{point_D}=\\angle {point_P}{point_B}{point_C}=\\angle {point_P}{point_D}{point_C}=90^{{\\circ}}$. Find the height of the pyramid.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_8_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
