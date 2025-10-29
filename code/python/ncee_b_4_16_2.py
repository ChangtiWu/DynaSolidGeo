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


def calculate(param_k):
    """
    计算给定param_k对应的V值。

    参数:
        param_k (float): 输入参数，用于计算V。

    返回:
        float: 计算得到的V值。
    """
    return (math.sqrt(6) * (param_k ** (3 / 2))) / (7 ** (3 / 4))


param_k = 2 * math.sqrt(7)
# result = calculate(param_k)
# print(f"当param_k={param_k}时，V的值为: {result:.4f}")
# Generate random lengths
param_k = round(len_scaling_factor * float(param_k), 2)

# Calculate the result
result = calculate(param_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_16_2",
    "type": 5,
    "level": 3,
    "cn_problem": f"在四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 中，已知：底面 {point_A}{point_B}{point_C}{point_D} 满足 {point_A}{point_B}⊥{point_B}{point_C}，{point_A}{point_B}⊥{point_A}{point_D}，∠{point_B}{point_A}{point_D}=∠{point_A}{point_B}{point_C}=90°；边长关系为 {point_A}{point_B}={point_B}{point_C}= len_b ，{point_A}{point_D}=2* len_b （ len_b >0）；侧面 {point_P}{point_A}{point_D} 为等边三角形且其所在平面与底面 {point_A}{point_B}{point_C}{point_D} 垂直，从而 {point_P}{point_A}={point_P}{point_D}={point_A}{point_D}=2* len_b 。已知三角形 {point_P}{point_C}{point_D} 的面积为 S_{{{point_P}{point_C}{point_D}}}={param_k}（{param_k}>0），求四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 的体积 V_{{{point_P}-{point_A}{point_B}{point_C}{point_D}}}。",
    "en_problem": f"In pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, the following conditions hold: the base {point_A}{point_B}{point_C}{point_D} satisfies {point_A}{point_B}⊥{point_B}{point_C}, {point_A}{point_B}⊥{point_A}{point_D}, ∠{point_B}{point_A}{point_D}=∠{point_A}{point_B}{point_C}=90°; edge relationships are {point_A}{point_B}={point_B}{point_C}= len_b , {point_A}{point_D}=2* len_b  (where  len_b >0); lateral face {point_P}{point_A}{point_D} is an equilateral triangle perpendicular to base {point_A}{point_B}{point_C}{point_D}, so {point_P}{point_A}={point_P}{point_D}={point_A}{point_D}=2* len_b . Given that triangle {point_P}{point_C}{point_D} has area S_{{{point_P}{point_C}{point_D}}}={param_k} ({param_k}>0), find the volume V_{{{point_P}-{point_A}{point_B}{point_C}{point_D}}} of pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_16_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
