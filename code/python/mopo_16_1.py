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
point_P, point_A, point_B, point_C, point_M = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(volume_V, len_a):
    """计算len_L_max关于volume_V和len_a的表达式"""
    return math.sqrt(3 * volume_V / len_a)


# 测试示例
volume_V = 3.0
len_a = 1.0

# print(calculate(volume_V, len_a))

# Generate random lengths
volume_V = round(len_scaling_factor * float(volume_V), 2)
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(volume_V, len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_16_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"在体积为 ${volume_V}$ 的三棱锥 {point_P}-{point_A}{point_B}{point_C} 中，${point_P}{point_A}$、${point_P}{point_B}$、${point_P}{point_C}$ 两两垂直，${point_P}{point_A} = {len_a}$。若点 {point_M} 是侧面 ${point_C}{point_B}{point_P}$ 内一动点，且满足 ${point_A}{point_M} \\\\perp {point_B}{point_C}$，求点 {point_M} 的轨迹长度的最大值。",
    "en_problem": f"In a triangular pyramid {point_P}-{point_A}{point_B}{point_C} with volume ${volume_V}$, where ${point_P}{point_A}$, ${point_P}{point_B}$, ${point_P}{point_C}$ are mutually perpendicular and ${point_P}{point_A} = {len_a}$. If point {point_M} is a moving point within lateral face ${point_C}{point_B}{point_P}$ satisfying ${point_A}{point_M} \\\\perp {point_B}{point_C}$, find the maximum value of the trajectory length of point {point_M}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_16_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_M}')"}, ensure_ascii=False) + "\n")
