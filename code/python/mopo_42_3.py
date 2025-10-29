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
point_A, point_B, point_C, point_D, point_E, point_F, point_K, point_G = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a):
    """计算len_L关于len_a的表达式（结果为(√3/3)π乘以len_a）"""
    return (math.sqrt(3) / 3) * math.pi * len_a


# 测试示例
len_a = 2.0

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_42_3",
    "type": 7,
    "level": 2,
    "cn_problem": f"设四边形 {point_A}{point_B}{point_C}{point_D} 与 {point_B}{point_D}{point_E}{point_F} 均为菱形，$\\\\angle {point_D}{point_A}{point_B} = \\\\angle {point_D}{point_B}{point_F} = 60°$，${point_A}{point_B} = {len_a}$，且 ${point_F}{point_A} = {point_F}{point_C}$。记 ${point_E}{point_F}$ 中点为 {point_K}，{point_G} 为四边形 {point_A}{point_B}{point_C}{point_D} 内的动点（含边界）且 ${point_G}{point_K} = {point_C}{point_F}$，求动点 {point_G} 的轨迹长度。",
    "en_problem": f"Let quadrilaterals {point_A}{point_B}{point_C}{point_D} and {point_B}{point_D}{point_E}{point_F} be rhombuses with $\\\\angle {point_D}{point_A}{point_B} = \\\\angle {point_D}{point_B}{point_F} = 60°$, ${point_A}{point_B} = {len_a}$, and ${point_F}{point_A} = {point_F}{point_C}$. Let {point_K} be the midpoint of ${point_E}{point_F}$, and {point_G} be a moving point within quadrilateral {point_A}{point_B}{point_C}{point_D} (including boundary) such that ${point_G}{point_K} = {point_C}{point_F}$. Find the trajectory length of moving point {point_G}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_42_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_K}', '{point_G}')"}, ensure_ascii=False) + "\n")
