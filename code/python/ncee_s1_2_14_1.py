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
point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
def calculate(len_b, len_c):
    """计算体积比volume_3/volume_1（表达式为(len_b + len_c)/len_b）"""
    return (len_b + len_c) / len_b


# 测试示例
len_a = 2.0
len_b = 2.0
len_c = 1.0
volume_1 = 1.0
volume_1 = 1.0

# print(calculate(len_b, len_c))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_s1_2_14_1",
    "type": 5,
    "level": 2,
    "cn_problem": f"如图，四边形{point_A}{point_B}{point_C}{point_D}为正方形，{point_E}{point_D}⊥平面{point_A}{point_B}{point_C}{point_D}，{point_F}{point_B}//{point_E}{point_D}。设{point_A}{point_B}={len_a}，{point_E}{point_D}={len_b}，{point_F}{point_B}={len_c}，其中{len_a}={len_b}。记三棱锥{point_E}-{point_A}{point_C}{point_D}、{point_F}-{point_A}{point_B}{point_C}、{point_F}-{point_A}{point_C}{point_E}的体积分别为volume_1、volume_2、volume_3。求volume_3与volume_1的比值。",
    "en_problem": f"As shown in the figure, quadrilateral {point_A}{point_B}{point_C}{point_D} is a square, {point_E}{point_D}⊥plane {point_A}{point_B}{point_C}{point_D}, {point_F}{point_B}//{point_E}{point_D}. Given {point_A}{point_B}={len_a}, {point_E}{point_D}={len_b}, {point_F}{point_B}={len_c}, where {len_a}={len_b}. Let the volumes of triangular pyramids {point_E}-{point_A}{point_C}{point_D}, {point_F}-{point_A}{point_B}{point_C}, {point_F}-{point_A}{point_C}{point_E} be volume_1, volume_2, volume_3 respectively. Find the ratio of volume_3 to volume_1.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_s1_2_14_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
