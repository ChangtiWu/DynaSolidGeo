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
point_P, point_A, point_B, point_C, point_O = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(volume_sphere):
    """
    计算给定的几何表达式（三棱锥的表面积）

    参数:
    volume_sphere (float): 三棱锥外接球的体积

    返回:
    float: 计算结果
    """
    return ((2 * volume_sphere) / (math.sqrt(3) * math.pi)) ** (2 / 3) * (1 + math.sqrt(2))


# 定义题干中的变量
len_m = 3  # 题干提到，但计算公式里没用到，仍需定义
volume_sphere = (27 * math.sqrt(3) / 2) * math.pi

# result = calculate(volume_sphere)
# print(f"计算结果: {result:.6f}")

 
# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)

# Calculate the result
result = calculate(volume_sphere)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area1_5_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"在三棱锥 {point_P} - {point_A}{point_B}{point_C} 中，{point_O} 为 {point_A}{point_C} 的中点，设 {point_P}{point_A} = {point_P}{point_B} = {point_B}{point_C} = {len_m}，满足 {point_P}{point_A} ⊥ {point_P}{point_B}，{point_A}{point_B} ⊥ {point_B}{point_C}，且平面 {point_P}{point_A}{point_B} ⊥ 平面 {point_P}{point_B}{point_C}。若三棱锥外接球的体积为 {volume_sphere}，求该三棱锥的表面积。",
    "en_problem": f"In tetrahedron {point_P} - {point_A}{point_B}{point_C}, {point_O} is the midpoint of {point_A}{point_C}. Let {point_P}{point_A} = {point_P}{point_B} = {point_B}{point_C} = {len_m}, with {point_P}{point_A} ⊥ {point_P}{point_B}, {point_A}{point_B} ⊥ {point_B}{point_C}, and plane {point_P}{point_A}{point_B} ⊥ plane {point_P}{point_B}{point_C}. If the volume of the circumscribed sphere is {volume_sphere}, find the surface area of the tetrahedron.",
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
    f.write(json.dumps({json_data["id"]: f"area1_5_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_O}')"}, ensure_ascii=False) + "\n")
