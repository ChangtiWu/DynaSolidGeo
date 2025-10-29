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
point_A, point_B, point_C, point_D, point_E, point_F, point_M, point_N = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a):
    """计算体积V关于len_a的表达式"""
    return (math.sqrt(2) / 12) * (len_a ** 3)


# 测试示例
len_a = 1.0

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_11_6_2",
    "type": 8,
    "level": 3,
    "cn_problem": f"设正六边形 ${point_A}{point_B}{point_C}{point_D}{point_E}{point_F}$ 的边长为 ${len_a} > 0$。沿对角线 ${point_A}{point_D}$ 折叠，使平面在 ${point_A}{point_D}$ 处折成二面角 ${point_M}\\text{{-}}{point_A}{point_D}\\text{{-}}{point_N}$。当折后使直线 ${point_C}{point_F}$ 与 ${point_A}{point_D}$ 的夹角为 $ arg_alpha  = 45°$ 时，求三棱锥 ${point_F}\\text{{-}}{point_C}{point_D}{point_E}$ 的体积。",
    "en_problem": f"Let regular hexagon ${point_A}{point_B}{point_C}{point_D}{point_E}{point_F}$ have side length ${len_a} > 0$. Fold along diagonal ${point_A}{point_D}$ to form a dihedral angle ${point_M}\\text{{-}}{point_A}{point_D}\\text{{-}}{point_N}$ at ${point_A}{point_D}$. When the angle between line ${point_C}{point_F}$ and ${point_A}{point_D}$ after folding is $ arg_alpha  = 45°$, find the volume of tetrahedron ${point_F}\\text{{-}}{point_C}{point_D}{point_E}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_11_6_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
