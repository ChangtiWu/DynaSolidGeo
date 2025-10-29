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
point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math


def calculate(len_p, len_q, len_h, arg_theta):
    """计算四面体体积（参数为异面直线长度、公垂线长度及夹角）"""
    return (1 / 6) * len_p * len_q * len_h * math.sin(arg_theta)


# 测试示例
len_p = 1.0
len_q = math.sqrt(3)
len_h = 2.0
arg_theta = math.pi / 3

# print(calculate(len_p, len_q, len_h, arg_theta))

# Generate random lengths
len_p = round(len_scaling_factor * float(len_p), 2)
len_q = round(len_scaling_factor * float(len_q), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_p, len_q, len_h, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_10_1",
    "type": 5,
    "level": 2,
    "cn_problem": f"在四面体 ${point_A}{point_B}{point_C}{point_D}$ 中，设 $|{point_A}{point_B}| = {len_p}>0$，$|{point_C}{point_D}| = {len_q}>0$，两异面直线 ${point_A}{point_B}$ 与 ${point_C}{point_D}$ 的公垂线长度（即最短距离）为 ${len_h}>0$，所成夹角为 ${arg_theta} \\in (0, \\pi)$。求四面体 ${point_A}{point_B}{point_C}{point_D}$ 的体积 $ volume_V $。",
    "en_problem": f"In tetrahedron ${point_A}{point_B}{point_C}{point_D}$, let $|{point_A}{point_B}| = {len_p}>0$ and $|{point_C}{point_D}| = {len_q}>0$. The two skew lines ${point_A}{point_B}$ and ${point_C}{point_D}$ have a common perpendicular length (i.e., shortest distance) of ${len_h}>0$ and form an angle ${arg_theta} \\in (0, \\pi)$. Find the volume $ volume_V$ of tetrahedron ${point_A}{point_B}{point_C}{point_D}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_10_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
