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
import math

def calculate(len_a, len_b):
    """
    计算线段 DE 的长度

    参数:
    len_a (float): BC = CD
    len_b (float): BE

    返回:
    float: DE 的长度
    """
    # 根据题干给出的解答公式: sqrt(len_b^2 - 3 * len_a^2)
    return math.sqrt(len_b ** 2 - 3 * len_a ** 2)


# 定义题干中的参数变量
len_a = 1.0      # BC = CD = 1
len_b = 2 * math.sqrt(3)  # BE = 2√3

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_a, len_b)
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_15_1",
    "type": 8,
    "level": 2,
    "cn_problem": f"在平面五边形{point_A}{point_B}{point_C}{point_D}{point_E}中，设{point_B}{point_C} = {point_C}{point_D} = {len_a}，∠{point_B}{point_C}{point_D} = ∠{point_C}{point_D}{point_E} = 2π/3，{point_B}{point_E} = {len_b}。延长{point_B}{point_C}、{point_E}{point_D}相交于点{point_F}，求线段{point_D}{point_E}的长度。",
    "en_problem": f"In plane pentagon {point_A}{point_B}{point_C}{point_D}{point_E}, let {point_B}{point_C} = {point_C}{point_D} = {len_a}, ∠{point_B}{point_C}{point_D} = ∠{point_C}{point_D}{point_E} = 2π/3, {point_B}{point_E} = {len_b}. Extend {point_B}{point_C} and {point_E}{point_D} to intersect at point {point_F}, find the length of segment {point_D}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_15_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
