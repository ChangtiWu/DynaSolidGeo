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
point_A, point_B, point_C, point_U, point_Z, point_X, point_Y, point_V, point_W = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math


def calculate(len_a, len_b, len_c):
    """计算len_h_max的值（基于三角形边长，通过海伦公式和最大边和计算）"""
    # 计算半周长param_s
    param_s = (len_a + len_b + len_c) / 2
    # 计算海伦公式面积area_K
    area_K = math.sqrt(param_s * (param_s - len_a) * (param_s - len_b) * (param_s - len_c))
    # 计算三边两两之和的最大值
    max_sum = max(len_a + len_b, len_b + len_c, len_c + len_a)
    # 计算len_h_max
    return (2 * area_K) / max_sum


# 测试示例（以边长3、4、5的直角三角形为例）
len_a = 23.0
len_b = 27.0
len_c = 30.0

# print(calculate(len_a, len_b, len_c))
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_11_aimeI_8",
    "type": 8,
    "level": 2,
    "cn_problem": f"如图，设△{point_A}{point_B}{point_C}三边长分别为 {point_B}{point_C}={len_a}，{point_C}{point_A}={len_b}，{point_A}{point_B}={len_c}（{len_a},{len_b},{len_c}>0，且满足三角不等式）。在线段 {point_A}{point_B}、{point_B}{point_C}、{point_C}{point_A} 上分别取点 {point_U},{point_Z}∈{point_A}{point_B}，{point_X},{point_Y}∈{point_B}{point_C}，{point_V},{point_W}∈{point_C}{point_A}，使得 {point_U}{point_V}∥{point_B}{point_C}，{point_W}{point_X}∥{point_A}{point_B}，{point_Y}{point_Z}∥{point_C}{point_A}。把△{point_A}{point_U}{point_V}、△{point_B}{point_Y}{point_Z}、△{point_C}{point_W}{point_X} 沿对应的底边 {point_U}{point_V}、{point_Y}{point_Z}、{point_W}{point_X} 向同侧翻折90°，形成桌腿；翻折后桌面（余下六边形）平行于水平面。求可折出的最大桌腿高度。",
    "en_problem": f"As shown, in triangle {point_A}{point_B}{point_C} with side lengths {point_B}{point_C}={len_a}, {point_C}{point_A}={len_b}, {point_A}{point_B}={len_c} ({len_a},{len_b},{len_c}>0, satisfying triangle inequality). Points {point_U},{point_Z}∈{point_A}{point_B}, {point_X},{point_Y}∈{point_B}{point_C}, {point_V},{point_W}∈{point_C}{point_A} are chosen such that {point_U}{point_V}∥{point_B}{point_C}, {point_W}{point_X}∥{point_A}{point_B}, and {point_Y}{point_Z}∥{point_C}{point_A}. Triangles △{point_A}{point_U}{point_V}, △{point_B}{point_Y}{point_Z}, △{point_C}{point_W}{point_X} are folded 90° along their respective bases {point_U}{point_V}, {point_Y}{point_Z}, {point_W}{point_X} towards the same side to form table legs; after folding, the tabletop (remaining hexagon) is parallel to the horizontal plane. Find the maximum possible table leg height.",
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
    f.write(json.dumps({json_data["id"]: f"aops_11_aimeI_8({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_U}', '{point_Z}', '{point_X}', '{point_Y}', '{point_V}', '{point_W}')"}, ensure_ascii=False) + "\n")
