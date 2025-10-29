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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_P, point_Q = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算正方体上底面内切圆周上一点与过顶点A、B、C1、D1的圆周上一点之间的最小距离。

    参数:
    len_a (float): 正方体的棱长。

    返回:
    float: 两点之间的最小距离。
    """
    # 上底面内切圆半径
    r1 = len_a *(math.sqrt(3)-math.sqrt(2))

    min_distance = r1/2

    return min_distance

# 示例输入
len_a = 1
# result = calculate(len_a)
# print(f"计算结果: {result:.6f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_s_12_1",
    "type": 7,
    "level": 3,
    "cn_problem": f"设正方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}的棱长为{len_a}，求上底面{point_A}{point_B}{point_C}{point_D}的内切圆周上的点{point_P}与过顶点{point_A}、{point_B}、{point_C1}、{point_D1}的圆周上的点{point_Q}之间的最小距离。",
    "en_problem": f"Let cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} have edge length {len_a}. Find the minimum distance between point {point_P} on the incircle of the upper base {point_A}{point_B}{point_C}{point_D} and point {point_Q} on the circle passing through vertices {point_A}, {point_B}, {point_C1}, {point_D1}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_s_12_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_P}', '{point_Q}')"}, ensure_ascii=False) + "\n")
