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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_M, point_N = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math

def calculate():
    """
    计算经过 A、M、N 三点的平面将直三棱柱 ABC-A1B1C1 分成两部分时，
    较小部分体积与三棱柱总体积的比值

    返回:
    float: 体积比
    """
    # 已知结果
    return 13 / 36


# 题干给定的数值
# 底面积 S，侧棱高 h，总体积 V = S * h
area_S = 1.0  # 任意单位
len_h = 1.0   # 任意单位

# 验证输出
# ratio = calculate()
# print(f"体积比: {ratio:.6f}")

# Generate random lengths
area_S = round(len_scaling_factor * float(area_S), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_10_1",
    "type": 5,
    "level": 2,
    "cn_problem": f"在直三棱柱{point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}中，设{point_M}是棱{point_B}{point_B1}的中点（即{point_B}{point_M} = {point_M}{point_B1}），{point_N}是棱{point_B1}{point_C1}的中点（即{point_B1}{point_N} = {point_N}{point_C1}）。记三棱柱的底面积为{area_S}，高（侧棱长）为{len_h}。经过{point_A}、{point_M}、{point_N}三点的平面将三棱柱分成体积不同的两部分，求较小部分的体积与三棱柱体积的比值。",
    "en_problem": f"In a right triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}, let {point_M} be the midpoint of edge {point_B}{point_B1} (i.e., {point_B}{point_M} = {point_M}{point_B1}), and {point_N} be the midpoint of edge {point_B1}{point_C1} (i.e., {point_B1}{point_N} = {point_N}{point_C1}). Let the base area of the triangular prism be {area_S} and the height (lateral edge length) be {len_h}. A plane passing through points {point_A}, {point_M}, {point_N} divides the triangular prism into two parts with different volumes. Find the ratio of the smaller part's volume to the triangular prism's volume.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_10_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
