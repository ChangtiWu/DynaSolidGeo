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
point_P, point_A, point_B, point_C, point_D, point_M = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_b):
    """计算len_x的值（表达式为√2乘以len_b）"""
    return math.sqrt(2) * len_b


# 测试示例
len_b = 1.0
len_h = 1.0

# print(calculate(len_b))

# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_3_5_1",
    "type": 3,
    "level": 1,
    "cn_problem": f"如图，已知四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 的底面 {point_A}{point_B}{point_C}{point_D} 为矩形，满足：(1) {point_P}{point_D} ⊥ 平面 {point_A}{point_B}{point_C}{point_D}；(2) {point_P}{point_D} = {len_h} > 0；(3) {point_D}{point_C} = {len_b} > 0；(4) {point_M} 为 {point_B}{point_C} 的中点；(5) {point_P}{point_B} ⊥ {point_A}{point_M}。求{point_B}{point_C}。",
    "en_problem": f"As shown, given a quadrilateral pyramid {point_P}-{point_A}{point_B}{point_C}{point_D} where the base {point_A}{point_B}{point_C}{point_D} is a rectangle satisfying: (1) {point_P}{point_D} ⊥ plane {point_A}{point_B}{point_C}{point_D}; (2) {point_P}{point_D} = {len_h} > 0; (3) {point_D}{point_C} = {len_b} > 0; (4) {point_M} is the midpoint of {point_B}{point_C}; (5) {point_P}{point_B} ⊥ {point_A}{point_M}. Find {point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_3_5_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}')"}, ensure_ascii=False) + "\n")
