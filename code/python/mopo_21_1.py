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
point_A, point_B, point_C, point_D, point_E, point_F, point_N, point_M = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a):
    """计算len_L关于len_a的表达式（结果为π乘以len_a的一半）"""
    return (math.pi * len_a) / 2


# 测试示例
len_a = 2

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_21_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"两个正方形框架 {point_A}{point_B}{point_C}{point_D}、{point_A}{point_B}{point_E}{point_F} 的边长均为 ${len_a}$，且它们所在的平面互相垂直。长度为 ${len_a}$ 的金属杆端点 {point_N} 在对角线 ${point_B}{point_F}$ 上移动，另一端点 {point_M} 在正方形 {point_A}{point_B}{point_C}{point_D} 内（含边界）移动，且始终保持 ${point_M}{point_N} \\\\perp {point_A}{point_B}$，求端点 {point_M} 的轨迹长度。",
    "en_problem": f"Two square frames {point_A}{point_B}{point_C}{point_D} and {point_A}{point_B}{point_E}{point_F} have side length ${len_a}$ each, and their planes are mutually perpendicular. A metal rod of length ${len_a}$ has endpoint {point_N} moving on diagonal ${point_B}{point_F}$, and the other endpoint {point_M} moves within square {point_A}{point_B}{point_C}{point_D} (including boundary), always maintaining ${point_M}{point_N} \\\\perp {point_A}{point_B}$. Find the trajectory length of endpoint {point_M}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_21_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_N}', '{point_M}')"}, ensure_ascii=False) + "\n")
