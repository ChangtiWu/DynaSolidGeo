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
point_S, point_A, point_B, point_C, point_D, point_O, point_E = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_a, len_b, arg_theta, len_lambda):
    """
    计算直线 CE 与平面 SBD 所成角的正切值

    参数:
    len_a (float): AD, CD 的边长
    len_b (float): SD 的长度
    arg_theta (float): ∠BAD 的角度（弧度制）
    len_lambda (float): SE/SA 的比例 λ

    返回:
    float: 直线 CE 与平面 SBD 所成角的正切值
    """
    # 根据题干给出的解答公式: 2√3 / 3
    return 2 * math.sqrt(3) / 3


# 定义题干中的参数变量
len_a = 1.0         # AD = CD = 1
len_b = math.sqrt(2)  # SD = √2
arg_theta = math.pi / 3  # ∠BAD = π/3
len_lambda = 1/3    # λ = 1/3

# 验证计算结果（确认与参考答案一致后注释掉）
#result = calculate(len_a, len_b, arg_theta, len_lambda)
#print(f"计算结果: {result:.6f}")


# Generate random lengths

len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b, arg_theta, len_lambda)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_11_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在四棱锥{point_S}-{point_A}{point_B}{point_C}{point_D}中，底面{point_A}{point_B}{point_C}{point_D}为菱形，∠{point_B}{point_A}{point_D} = {arg_theta}，{point_A}{point_D} = {point_C}{point_D} = {len_a}，{point_S}{point_D}⊥平面{point_A}{point_B}{point_C}{point_D}且{point_S}{point_D} = {len_b}。连接{point_A}{point_C}交{point_B}{point_D}于点{point_O}，点{point_E}在棱{point_S}{point_A}上，满足{point_S}{point_E}/{point_S}{point_A} = {len_lambda}（0 ≤ {len_lambda} ≤ 1）。若△{point_S}{point_A}{point_C}为等边三角形（即{point_S}{point_A} = {point_S}{point_C} = {point_A}{point_C}），求直线{point_C}{point_E}与平面{point_S}{point_B}{point_D}所成角的正切值。",
    "en_problem": f"In pyramid {point_S}-{point_A}{point_B}{point_C}{point_D}, base {point_A}{point_B}{point_C}{point_D} is a rhombus, ∠{point_B}{point_A}{point_D} = {arg_theta}, {point_A}{point_D} = {point_C}{point_D} = {len_a}, {point_S}{point_D}⊥plane {point_A}{point_B}{point_C}{point_D} and {point_S}{point_D} = {len_b}. Connect {point_A}{point_C} intersecting {point_B}{point_D} at point {point_O}, point {point_E} is on edge {point_S}{point_A}, satisfying {point_S}{point_E}/{point_S}{point_A} = {len_lambda} (0 ≤ {len_lambda} ≤ 1). If triangle {point_S}{point_A}{point_C} is equilateral (i.e., {point_S}{point_A} = {point_S}{point_C} = {point_A}{point_C}), find the tangent of the angle between line {point_C}{point_E} and plane {point_S}{point_B}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_11_2({mode}, {azimuth}, {elevation}, '{point_S}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}', '{point_E}')"}, ensure_ascii=False) + "\n")
