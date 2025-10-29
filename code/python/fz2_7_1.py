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
point_A, point_B, point_C, point_D, point_O = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math

def calculate(len_a, arg_alpha, arg_theta_2):
    """
    计算翻折后点 O 到直线 AC 距离的最小值

    参数:
    len_a (float): 菱形边长
    arg_alpha (float): ∠BAD 的角度（弧度）
    arg_theta_2 (float): θ 的上界（弧度）

    返回:
    float: 距离最小值
    """
    # 根据题干给出的解答公式: len_a * cos(arg_alpha/2) * cos(arg_theta_2/2)
    return len_a * math.cos(arg_alpha / 2) * math.cos(arg_theta_2 / 2)


# 定义题干中的参数变量
len_a = 8.0                     # 菱形边长
arg_alpha = math.radians(60)    # ∠BAD = 60°
arg_theta_1 = math.radians(90) # θ 的下界 90°
arg_theta_2 = math.radians(120) # θ 的上界 120°

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_a, arg_alpha, arg_theta_2)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, arg_alpha, arg_theta_2)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz2_7_1",
    "type": 8,
    "level": 1,
    "cn_problem": f"已知菱形{point_A}{point_B}{point_C}{point_D}的边长为{len_a}，∠{point_B}{point_A}{point_D} = {arg_alpha}（0 < {arg_alpha} < π），对角线{point_A}{point_C}与{point_B}{point_D}交于点{point_O}。将菱形{point_A}{point_B}{point_C}{point_D}沿对角线{point_B}{point_D}翻折成平面角为 arg_theta 的二面角，且{arg_theta_1} ≤  arg_theta  ≤ {arg_theta_2}（{arg_theta_2} > {arg_theta_1}）。求翻折后点{point_O}到直线{point_A}{point_C}距离的最小值。",
    "en_problem": f"Given rhombus {point_A}{point_B}{point_C}{point_D} with side length {len_a} and ∠{point_B}{point_A}{point_D} = {arg_alpha} (0 < {arg_alpha} < π), diagonals {point_A}{point_C} and {point_B}{point_D} intersect at point {point_O}. The rhombus {point_A}{point_B}{point_C}{point_D} is folded along diagonal {point_B}{point_D} to form a dihedral angle with plane angle  arg_theta , where {arg_theta_1} ≤  arg_theta  ≤ {arg_theta_2} ({arg_theta_2} > {arg_theta_1}). Find the minimum distance from point {point_O} to line {point_A}{point_C} after folding.",
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
    f.write(json.dumps({json_data["id"]: f"fz2_7_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}')"}, ensure_ascii=False) + "\n")
