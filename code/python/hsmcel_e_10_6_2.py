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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1 = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a):
    """计算体积V关于len_a的表达式"""
    return 2 * math.sqrt(2) * (len_a ** 3)


# 测试示例
len_a = 1

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_10_6_2",
    "type": 5,
    "level": 3,
    "cn_problem": f"在平行六面体 ${point_A}{point_B}{point_C}{point_D}$-${point_A1}{point_B1}{point_C1}{point_D1}$ 中，取顶点 ${point_A}$ 的三条相邻棱长分别为 $|{point_A}{point_B}| = |{point_A}{point_D}| = 2*{len_a}$，$|{point_A}{point_A1}| = {len_a}$（${len_a} > 0$），且三条棱两两所成夹角均为 $60°$。设三个向量 $\\vec{{u}} = \\overrightarrow{{{point_A}{point_B}}}$，$\\vec{{v}} = \\overrightarrow{{{point_A}{point_D}}}$，$\\vec{{w}} = \\overrightarrow{{{point_A}{point_A1}}}$ 为该平行六面体的生成元。求：该平行六面体的体积 $volume_V$。",
    "en_problem": f"In parallelepiped ${point_A}{point_B}{point_C}{point_D}$-${point_A1}{point_B1}{point_C1}{point_D1}$, take three adjacent edges from vertex ${point_A}$ with lengths $|{point_A}{point_B}| = |{point_A}{point_D}| = 2*{len_a}$, $|{point_A}{point_A1}| = {len_a}$ (${len_a} > 0$), and the angles between any two of these three edges are all $60°$. Let the three vectors $\\vec{{u}} = \\overrightarrow{{{point_A}{point_B}}}$, $\\vec{{v}} = \\overrightarrow{{{point_A}{point_D}}}$, $\\vec{{w}} = \\overrightarrow{{{point_A}{point_A1}}}$ be the generating elements of this parallelepiped. Find: The volume $volume_V$ of this parallelepiped.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_10_6_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}')"}, ensure_ascii=False) + "\n")
