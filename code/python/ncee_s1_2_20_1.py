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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
def calculate(volume_total):
    """计算金字塔体积（总体积除以12）"""
    return volume_total / 12


# 测试示例
len_a = 6.0
len_b = 5.0
len_c = 4.0
volume_total = 120

# print(calculate(volume_total))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)
volume_total = round(len_scaling_factor * float(volume_total), 2)

# Calculate the result
result = calculate(volume_total)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_s1_2_20_1",
    "type": 5,
    "level": 1,
    "cn_problem": f"长方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}的长、宽、高分别为{len_a}、{len_b}、{len_c}（即{point_A}{point_B}={len_a}，{point_B}{point_C}={len_b}，{point_C}{point_C1}={len_c}），其体积为{volume_total}。点{point_E}为{point_C}{point_C1}的中点，求三棱锥{point_E}-{point_B}{point_C}{point_D}的体积。",
    "en_problem": f"A rectangular prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} has length, width, and height of {len_a}, {len_b}, {len_c} respectively (i.e., {point_A}{point_B}={len_a}, {point_B}{point_C}={len_b}, {point_C}{point_C1}={len_c}), with total volume {volume_total}. Point {point_E} is the midpoint of {point_C}{point_C1}. Find the volume of triangular pyramid {point_E}-{point_B}{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_s1_2_20_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}')"}, ensure_ascii=False) + "\n")
