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
point_A, point_B, point_C, point_D, point_E, point_P = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate():
    """
    计算平面 PAE 与平面 PCE 所成角的正弦值

    返回:
    float: 平面所成角的正弦值
    """
    # 根据题干给出的解答公式: sqrt(6) / 3
    return math.sqrt(6) / 3


# 定义题干中的参数变量
len_m = 2.0  # AB = 2 * m, AD = m


# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate()
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_14_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"矩形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_B} = 2*{len_m}，{point_A}{point_D} = {len_m}，{point_E}为{point_D}{point_C}的中点。将△{point_A}{point_D}{point_E}沿{point_A}{point_E}翻折，使点{point_D}与点{point_P}重合，且{point_P}{point_B} = √3*{len_m}。求平面{point_P}{point_A}{point_E}与平面{point_P}{point_C}{point_E}所成角的正弦值。",
    "en_problem": f"In rectangle {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B} = 2*{len_m}, {point_A}{point_D} = {len_m}, {point_E} is the midpoint of {point_D}{point_C}. Fold triangle {point_A}{point_D}{point_E} along {point_A}{point_E} so that point {point_D} coincides with point {point_P}, and {point_P}{point_B} = √3*{len_m}. Find the sine of the angle between plane {point_P}{point_A}{point_E} and plane {point_P}{point_C}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_14_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_P}')"}, ensure_ascii=False) + "\n")
