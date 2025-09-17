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
point_A, point_B, point_C, point_D, point_O1, point_O2, point_E, point_F, point_G, point_H = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math


def calculate(len_r, len_R, arg_theta, volume_pyramid):
    """
    计算给定的几何表达式（圆台的侧面积）

    参数:
    len_r (float): 上底面半径
    len_R (float): 下底面半径
    arg_theta (float): 角度（弧度制）
    volume_pyramid (float): 三棱锥体积

    返回:
    float: 计算结果
    """
    return math.pi * (len_r + len_R) * math.sqrt(
        (24 * volume_pyramid / (len_R ** 2 * math.sin(arg_theta))) ** 2 + (len_R - len_r) ** 2
    )


# 定义题干中的变量
len_r = 2  # CD / 2
len_R = 4  # AB / 2
arg_theta = math.radians(60)  # 将60°转换为弧度
volume_pyramid = 5 * math.sqrt(3) / 3

# result = calculate(len_r, len_R, arg_theta, volume_pyramid)
# print(f"计算结果: {result:.6f}")


# Calculate the result
result = calculate(len_r, len_R, arg_theta, volume_pyramid)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area1_19_2",
    "type": 4,
    "level": 2,
    "cn_problem": f"梯形 {point_A}{point_B}{point_C}{point_D} 是圆台 {point_O1}{point_O2} 的轴截面，{point_E}，{point_F} 分别在底面圆 {point_O1}，{point_O2} 的圆周上，{point_E}{point_F} 为圆台的母线，∠{point_D}{point_O1}{point_E} = {arg_theta}。已知上底面直径 {point_C}{point_D} = 2*{len_r}，下底面直径 {point_A}{point_B} = 2*{len_R}（{len_r} < {len_R}），{point_G}，{point_H} 分别为 {point_O2}{point_B}，{point_B}{point_F} 的中点。若三棱锥 {point_C} - {point_G}{point_B}{point_H} 的体积为 {volume_pyramid}，求圆台 {point_O1}{point_O2} 的侧面积。",
    "en_problem": f"Trapezoid {point_A}{point_B}{point_C}{point_D} is the axial cross-section of frustum {point_O1}{point_O2}, {point_E} and {point_F} are on the circumferences of base circles {point_O1} and {point_O2} respectively, {point_E}{point_F} is a slant line of the frustum, ∠{point_D}{point_O1}{point_E} = {arg_theta}. Given that upper base diameter {point_C}{point_D} = 2*{len_r}, lower base diameter {point_A}{point_B} = 2*{len_R} ({len_r} < {len_R}), {point_G} and {point_H} are midpoints of {point_O2}{point_B} and {point_B}{point_F} respectively. If the volume of pyramid {point_C} - {point_G}{point_B}{point_H} is {volume_pyramid}, find the lateral surface area of frustum {point_O1}{point_O2}.",
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
    f.write(json.dumps({json_data["id"]: f"area1_19_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O1}', '{point_O2}', '{point_E}', '{point_F}', '{point_G}', '{point_H}')"}, ensure_ascii=False) + "\n")
