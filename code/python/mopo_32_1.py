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
point_A, point_B, point_C, point_D, point_E, point_B_prime, point_K = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_a: float, len_b: float) -> float:
    """
    计算点 K 的轨迹长度

    参数:
    len_a (float): 矩形 AB 的边长
    len_b (float): 矩形 BC 的边长

    返回:
    float: 轨迹长度
    """
    return (len_a / 2.0) * math.atan(len_b / len_a)


# 题干给定的数值
len_a = 1.0
len_b = math.sqrt(3)
arg_alpha = 120  # 二面角的平面角

# 计算结果
# result = calculate(len_a, len_b)
# print(f"轨迹长度: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_32_1",
    "type": 8,
    "level": 2,
    "cn_problem": f"在矩形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_B} = {len_a}，{point_B}{point_C} = {len_b}，{point_E}为线段{point_B}{point_C}上的动点。将△{point_A}{point_B}{point_E}沿{point_A}{point_E}折起得到△{point_A}{point_B_prime}{point_E}，当二面角{point_B_prime}-{point_A}{point_E}-{point_D}的平面角为{arg_alpha}°时，点{point_B_prime}在平面{point_A}{point_B}{point_C}上的投影为{point_K}。求{point_E}从{point_B}运动到{point_C}时，点{point_K}形成轨迹的长度。",
    "en_problem": f"In rectangle {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B} = {len_a} and {point_B}{point_C} = {len_b}. Point {point_E} is a moving point on segment {point_B}{point_C}. Triangle {point_A}{point_B}{point_E} is folded along {point_A}{point_E} to form triangle {point_A}{point_B_prime}{point_E}. When the plane angle of dihedral angle {point_B_prime}-{point_A}{point_E}-{point_D} is {arg_alpha}°, the projection of point {point_B_prime} onto plane {point_A}{point_B}{point_C} is {point_K}. Find the length of the trajectory formed by point {point_K} as {point_E} moves from {point_B} to {point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_32_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_B_prime}', '{point_K}')"}, ensure_ascii=False) + "\n")
