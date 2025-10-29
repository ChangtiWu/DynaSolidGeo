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

def calculate(len_a):
    """
    计算平面 PAB 与平面 PBC 所成角的正弦值

    参数:
    len_a (float): 基本长度单位 a

    返回:
    float: 两平面所成角的正弦值
    """
    # 根据题干给出的解答公式: 4 * sqrt(2090) / 209
    return 4 * math.sqrt(2090) / 209


# 定义题干中的参数变量
len_a = 2.0  # 根据题干 BC = CD = 2 * AD = 4，则 AD = 2

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_a)
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_19_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在梯形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_D}∥{point_B}{point_C}，∠{point_A}{point_D}{point_C} = 90°，{point_B}{point_C} = {point_C}{point_D} = 2*{point_A}{point_D} = 2*{len_a}（{len_a} > 0），{point_E}是{point_C}{point_D}的中点。将△{point_A}{point_D}{point_E}沿{point_A}{point_E}折起，使点{point_D}到达点{point_P}的位置，且{point_P}{point_C} = √3*{len_a}。求平面{point_P}{point_A}{point_B}与平面{point_P}{point_B}{point_C}所成角的正弦值。",
    "en_problem": f"In trapezoid {point_A}{point_B}{point_C}{point_D}, {point_A}{point_D}∥{point_B}{point_C}, ∠{point_A}{point_D}{point_C} = 90°, {point_B}{point_C} = {point_C}{point_D} = 2*{point_A}{point_D} = 2*{len_a} ({len_a} > 0), {point_E} is the midpoint of {point_C}{point_D}. Fold triangle {point_A}{point_D}{point_E} along {point_A}{point_E} so that point {point_D} reaches position {point_P}, with {point_P}{point_C} = √3*{len_a}. Find the sine of the angle between plane {point_P}{point_A}{point_B} and plane {point_P}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_19_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_P}')"}, ensure_ascii=False) + "\n")
