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
point_A, point_B, point_C, point_A1, point_B1, point_C1 = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(volume_V, area_S):
    """计算体积与面积的比值（d = volume_V / area_S）"""
    return volume_V / area_S


# 测试示例
volume_V = 4.0
area_S = 2 * math.sqrt(2)

# print(calculate(volume_V, area_S))
# Generate random lengths
volume_V = round(len_scaling_factor * float(volume_V), 2)
area_S = round(len_scaling_factor * float(area_S), 2)

# Calculate the result
result = calculate(volume_V, area_S)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_3_4_1",
    "type": 3,
    "level": 1,
    "cn_problem": f"如图，已知直三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}，其中底面 △{point_A}{point_B}{point_C} 与顶面 △{point_A1}{point_B1}{point_C1} 平行且对应顶点连线均垂直于底面。棱柱体积为 {volume_V}>0，异面三角形 △{point_A1}{point_B}{point_C} 的面积为 {area_S}>0。求底面顶点 {point_A} 到平面 {point_A1}{point_B}{point_C} 的距离。",
    "en_problem": f"As shown, given a right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} where the base triangle {point_A}{point_B}{point_C} is parallel to the top triangle {point_A1}{point_B1}{point_C1} and corresponding vertex connections are perpendicular to the base. The prism volume is {volume_V}>0, and the area of triangle {point_A1}{point_B}{point_C} is {area_S}>0. Find the distance d from base vertex {point_A} to plane {point_A1}{point_B}{point_C}, and express the result as a function of {volume_V} and {area_S}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_3_4_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}')"}, ensure_ascii=False) + "\n")
