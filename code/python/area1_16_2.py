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
point_P, point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(volume_pyramid):
    """
    计算给定的几何表达式（四棱锥的侧面积）

    参数:
    volume_pyramid (float): 四棱锥的体积

    返回:
    float: 计算结果
    """
    return (3 + math.sqrt(3)) / 2 * (3 * volume_pyramid) ** (2 / 3)


# 定义题干中的变量

volume_pyramid = 8 / 3

# result = calculate(volume_pyramid)
# print(f"计算结果: {result:.6f}")
 
# Generate random lengths
volume_pyramid = round(len_scaling_factor * float(volume_pyramid), 2)

# Calculate the result
result = calculate(volume_pyramid)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area1_16_2",
    "type": 4,
    "level": 1,
    "cn_problem": f"在四棱锥 {point_P} - {point_A}{point_B}{point_C}{point_D} 中，{point_A}{point_B} ∥ {point_C}{point_D}，且 ∠{point_B}{point_A}{point_P} = ∠{point_C}{point_D}{point_P} = 90°。已知 {point_P}{point_A} = {point_P}{point_D} = {point_A}{point_B} = {point_D}{point_C} = len_edge，∠{point_A}{point_P}{point_D} = 90°，四棱锥 {point_P} - {point_A}{point_B}{point_C}{point_D} 的体积为 {volume_pyramid}，求该四棱锥的侧面积。",
    "en_problem": f"In pyramid {point_P} - {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B} ∥ {point_C}{point_D}, and ∠{point_B}{point_A}{point_P} = ∠{point_C}{point_D}{point_P} = 90°. Given that {point_P}{point_A} = {point_P}{point_D} = {point_A}{point_B} = {point_D}{point_C} = len_edge, ∠{point_A}{point_P}{point_D} = 90°, and the volume of pyramid {point_P} - {point_A}{point_B}{point_C}{point_D} is {volume_pyramid}, find the lateral surface area of the pyramid.",
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
    f.write(json.dumps({json_data["id"]: f"area1_16_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
