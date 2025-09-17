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
point_A, point_B, point_C, point_D, point_O, point_E, point_F, point_G, point_H = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math


def calculate():
    """计算param_cos的值为√7/21"""
    return math.sqrt(7) / 21


# 测试示例
len_a = 2.0

# print(calculate())

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_26_3",
    "type": 2,
    "level": 1,
    "cn_problem": f"如图，设正方形 {point_A}{point_B}{point_C}{point_D} 的边长为 {len_a}>0，其中心为 {point_O}。在空间中作矩形 {point_O}{point_B}{point_E}{point_F}，满足：(1) 平面 {point_O}{point_B}{point_E}{point_F} ⊥ 平面 {point_A}{point_B}{point_C}{point_D}；(2) {point_B}{point_E} = {len_a}（即矩形的竖边长等于正方形的边长）；(3) 点 {point_G} 为 {point_A}{point_B} 的中点（本问未用到，但保持原题信息）；记 {point_A}(0,0,0), {point_B}({len_a},0,0), {point_C}({len_a},{len_a},0), {point_D}(0,{len_a},0), {point_O}({len_a}/2,{len_a}/2,0), {point_E}({len_a},0,{len_a}), {point_F}({len_a}/2,{len_a}/2,{len_a})。在线段 {point_A}{point_F} 上取点 {point_H}，使 {point_A}{point_H}=2/3·{point_H}{point_F}。求直线 {point_B}{point_H} 与平面 {point_C}{point_E}{point_F} 所成角的余弦值。",
    "en_problem": f"As shown, let square {point_A}{point_B}{point_C}{point_D} have side length {len_a}>0 with center {point_O}. In space, construct rectangle {point_O}{point_B}{point_E}{point_F} satisfying: (1) plane {point_O}{point_B}{point_E}{point_F} ⊥ plane {point_A}{point_B}{point_C}{point_D}; (2) {point_B}{point_E} = {len_a} (rectangle's vertical edge equals square's side length); (3) point {point_G} is the midpoint of {point_A}{point_B} (not used in this problem, but keeping original info); with coordinates {point_A}(0,0,0), {point_B}({len_a},0,0), {point_C}({len_a},{len_a},0), {point_D}(0,{len_a},0), {point_O}({len_a}/2,{len_a}/2,0), {point_E}({len_a},0,{len_a}), {point_F}({len_a}/2,{len_a}/2,{len_a}). On segment {point_A}{point_F}, take point {point_H} such that {point_A}{point_H}=2/3·{point_H}{point_F}. Find the cosine of the angle between line {point_B}{point_H} and plane {point_C}{point_E}{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_26_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}', '{point_E}', '{point_F}', '{point_G}', '{point_H}')"}, ensure_ascii=False) + "\n")
