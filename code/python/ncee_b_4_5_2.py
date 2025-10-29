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
point_A, point_B, point_C, point_D, point_O, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(param_r, len_s, ang_phi):
    """
    计算四面体 A-BCD 的体积 V_{A-BCD}

    参数:
        param_r (float): 比例参数 r
        len_s (float): 长度参数 s
        ang_phi (float): 角度 φ（以弧度为单位）

    返回:
        float: 体积计算结果

    公式:
        V_{A-BCD} = [√3 × (r + 2) × s] / [12 × r × cos(φ)] × √(1 - s⁴ × cos²(φ))
    """
    # 计算分子部分
    numerator = math.sqrt(3) * (param_r + 2) * len_s

    # 计算分母部分
    denominator = 12 * param_r * math.cos(ang_phi)

    # 计算平方根项
    square_root_term = math.sqrt(1 - (len_s ** 4) * (math.cos(ang_phi) ** 2))

    # 返回最终计算结果
    return (numerator / denominator) * square_root_term

# 设置参数值
param_r = 2
len_s = 1
ang_phi = math.radians(45)

# 计算体积
# volume = calculate(param_r, len_s, ang_phi)
#
# print(f"四面体体积 V = {volume:.6f}")
# Generate random lengths
# len_s = round(len_scaling_factor * float(len_s), 2)



# Calculate the result
result = calculate(param_r, len_s, ang_phi)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_5_2",
    "type": 5,
    "level": 3,
    "cn_problem": f"在四面体 {point_A}-{point_B}{point_C}{point_D} 中，平面 {point_A}{point_B}{point_D} ⊥ 平面 {point_B}{point_C}{point_D}，{point_A}{point_B}={point_A}{point_D}，{point_O} 为 {point_B}{point_D} 的中点。△{point_O}{point_C}{point_D} 是边长为 {len_s} 的等边三角形，点 {point_E} 在棱 {point_A}{point_D} 上，满足 {point_D}{point_E}={param_r}·{point_E}{point_A}（{param_r}>0），二面角 {point_E}-{point_B}{point_C}-{point_D} 的大小为 {ang_phi}（0<{ang_phi}<\\tfrac{{\\pi}}{{2}}）。求四面体 {point_A}-{point_B}{point_C}{point_D} 的体积。",
    "en_problem": f"In tetrahedron {point_A}-{point_B}{point_C}{point_D}, plane {point_A}{point_B}{point_D} ⊥ plane {point_B}{point_C}{point_D}, {point_A}{point_B}={point_A}{point_D}, {point_O} is the midpoint of {point_B}{point_D}. Triangle {point_O}{point_C}{point_D} is equilateral with side length {len_s}, point {point_E} lies on edge {point_A}{point_D} satisfying {point_D}{point_E}={param_r}·{point_E}{point_A} (where {param_r}>0), and the dihedral angle {point_E}-{point_B}{point_C}-{point_D} is {ang_phi} (0<{ang_phi}<\\tfrac{{\\pi}}{{2}}）。求四面体 {point_A}-{point_B}{point_C}{point_D} 的体积。",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_5_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}', '{point_E}')"}, ensure_ascii=False) + "\n")
