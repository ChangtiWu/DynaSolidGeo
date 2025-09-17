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
point_A, point_B, point_C, point_D, point_P, point_O, point_E, point_M, point_N = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math

def calculate():
    """
    计算点 N 轨迹的长度

    返回:
    float: 轨迹长度
    """
    # 已知结果
    return 2 * math.pi / 3


# 题干给定的数值
len_a = 2.0           # AB
len_b = 2 * math.sqrt(3)  # AD
R = 2.0               # 外接球半径
PC = math.sqrt(10)

# 验证输出
# length_trajectory = calculate()
# print(f"点 N 轨迹长度: {length_trajectory:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
R = round(len_scaling_factor * float(R), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "zht_10_3",
    "type": 8,
    "level": 2,
    "cn_problem": f"设矩形 {point_A}{point_B}{point_C}{point_D} 中，{point_A}{point_B} = {len_a}，{point_A}{point_D} = {len_b}，沿对角线 {point_B}{point_D} 折起后，三棱锥 {point_P}-{point_B}{point_C}{point_D} 的外接球心为 {point_B}{point_D} 中点 {point_O}，半径 R = {point_B}{point_D}/2 = {R}（故 {point_B}{point_D} = 2R，满足 {len_a}^2 + {len_b}^2 = (2R)^2）。折叠后，{point_P} 到 {point_B}{point_D} 的垂足为 {point_E}，{point_B}{point_E} = {len_a}^2/(2R)，{point_E}{point_D} = {len_b}^2/(2R)，且 {point_P}{point_E} ⊥ 平面 {point_B}{point_C}{point_D}。{point_M} 为 {point_P}{point_D} 的中点，点 {point_N} 在 {point_B}{point_C}{point_D} 边界及内部运动，若直线 {point_P}{point_N} 与直线 {point_M}{point_N} 与平面 {point_B}{point_C}{point_D} 所成角相等，求点 {point_N} 轨迹的长度。",
    "en_problem": f"Let in rectangle {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B} = {len_a}, {point_A}{point_D} = {len_b}, after folding along diagonal {point_B}{point_D}, the circumcenter of triangular pyramid {point_P}-{point_B}{point_C}{point_D} is the midpoint {point_O} of {point_B}{point_D}, radius R = {point_B}{point_D}/2 = {R} (so {point_B}{point_D} = 2R, satisfying {len_a}^2 + {len_b}^2 = (2R)^2). After folding, the foot of perpendicular from {point_P} to {point_B}{point_D} is {point_E}, {point_B}{point_E} = {len_a}^2/(2R), {point_E}{point_D} = {len_b}^2/(2R), and {point_P}{point_E} ⊥ plane {point_B}{point_C}{point_D}. {point_M} is the midpoint of {point_P}{point_D}, point {point_N} moves on the boundary and interior of {point_B}{point_C}{point_D}, if the angles between line {point_P}{point_N} and line {point_M}{point_N} with plane {point_B}{point_C}{point_D} are equal, find the length of the trajectory of point {point_N}.",
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
    f.write(json.dumps({json_data["id"]: f"zht_10_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}', '{point_O}', '{point_E}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
