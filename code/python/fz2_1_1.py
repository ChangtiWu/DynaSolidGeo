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
point_A, point_B, point_C, point_D, point_P = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算翻折过程中动点 P 的轨迹长度

    参数:
    len_a (float): AB 的长度

    返回:
    float: 轨迹长度
    """
    # 根据题干给出的解答公式: (sqrt(2) * len_a * π) / 12
    return (math.sqrt(2) * len_a * math.pi) / 12


# 定义题干中的参数变量
len_a = 1.0  # AB = 1

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_a)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz2_1_1",
    "type": 8,
    "level": 1,
    "cn_problem": f"已知在三角形{point_A}{point_B}{point_C}中，{point_A}{point_B} ⊥ {point_B}{point_C}，{point_A}{point_B} = {len_a}，{point_B}{point_C} = 3*{len_a}，{point_D}是{point_B}{point_C}边上一点，且{point_B}{point_D} = {len_a}，将三角形{point_A}{point_B}{point_D}沿{point_A}{point_D}进行翻折，使得点{point_B}与点{point_P}重合。若点{point_P}在平面{point_A}{point_D}{point_C}上的射影在三角形{point_A}{point_D}{point_C}内部及边界上，求在翻折过程中，动点{point_P}的轨迹长度。",
    "en_problem": f"In triangle {point_A}{point_B}{point_C}, {point_A}{point_B} ⊥ {point_B}{point_C}, {point_A}{point_B} = {len_a}, {point_B}{point_C} = 3*{len_a}, and {point_D} is a point on side {point_B}{point_C} with {point_B}{point_D} = {len_a}. Triangle {point_A}{point_B}{point_D} is folded along {point_A}{point_D} so that point {point_B} coincides with point {point_P}. If the projection of point {point_P} onto plane {point_A}{point_D}{point_C} lies within triangle {point_A}{point_D}{point_C} (including its boundary), find the length of the trajectory of moving point {point_P} during the folding process.",
    "solution": f"{result}",
    "image": f"images/{os.path.splitext(os.path.basename(__file__))[0]}.png"
}

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
    f.write(json.dumps({json_data["id"]: f"fz2_1_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}')"}, ensure_ascii=False) + "\n")
