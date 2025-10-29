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
point_A, point_E, point_F, point_D, point_B, point_C = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_a, len_b):
    """
    计算平面 AEF 与平面 CEF 的夹角正切值

    参数:
    len_a (float): BC
    len_b (float): EF
    len_c (float): AB = BE

    返回:
    float: 平面夹角的正切值
    """
    # 根据题干给出的解答公式: len_b / len_a
    return len_b / len_a


# 定义题干中的参数变量
len_a = math.sqrt(3)  # BC = √3
len_b = 2.0           # EF = 2

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_a, len_b, len_c)
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_16_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"如图，已知直角梯形{point_A}{point_E}{point_F}{point_D}中，∠{point_A} = ∠{point_D} = 90°，点{point_B}, {point_C}分别在{point_A}{point_E}, {point_D}{point_F}上，且{point_B}{point_C}⊥{point_A}{point_E}，向量{point_E}{point_F}·向量{point_C}{point_E} = 0，{point_B}{point_C} = {len_a}，{point_E}{point_F} = {len_b}。将图沿{point_B}{point_C}翻折，使平面{point_A}{point_B}{point_C}{point_D}⊥平面{point_B}{point_E}{point_F}{point_C}。当{point_A}{point_B} = {point_B}{point_E}时，求平面{point_A}{point_E}{point_F}与平面{point_C}{point_E}{point_F}的夹角的正切值。",
    "en_problem": f"In the figure, given right trapezoid {point_A}{point_E}{point_F}{point_D} where ∠{point_A} = ∠{point_D} = 90°, points {point_B}, {point_C} are on {point_A}{point_E}, {point_D}{point_F} respectively, and {point_B}{point_C}⊥{point_A}{point_E}, vector {point_E}{point_F}·vector {point_C}{point_E} = 0, {point_B}{point_C} = {len_a}, {point_E}{point_F} = {len_b}. Fold the figure along {point_B}{point_C} so that plane {point_A}{point_B}{point_C}{point_D} ⊥ plane {point_B}{point_E}{point_F}{point_C}. When {point_A}{point_B} = {point_B}{point_E}, find the tangent of the angle between plane {point_A}{point_E}{point_F} and plane {point_C}{point_E}{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_16_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_E}', '{point_F}', '{point_D}', '{point_B}', '{point_C}')"}, ensure_ascii=False) + "\n")
