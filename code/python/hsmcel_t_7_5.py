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
point_P, point_A, point_B, point_C, point_E, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate():
    """
    计算当 △AEF 面积最大时，tan(θ) 的值

    返回:
    float: tan(θ)
    """
    return math.sqrt(2) / 2


# 题干给定的数值
len_a = 2.0  # PA = AB = 2
# ∠BPC = θ，△AEF 面积最大时求 tanθ

# 验证输出
# tan_theta = calculate()
# print(f"tanθ: {tan_theta:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_7_5",
    "type": 2,
    "level": 2,
    "cn_problem": f"在四面体{point_P}{point_A}{point_B}{point_C}中，{point_P}{point_A} ⊥ 平面{point_A}{point_B}{point_C}，∠{point_A}{point_C}{point_B} = 90°，{point_A}{point_E} ⊥ {point_P}{point_B}于{point_E}，{point_A}{point_F} ⊥ {point_P}{point_C}于{point_F}。若{point_P}{point_A} = {point_A}{point_B} = {len_a}（{len_a}为正常数），∠{point_B}{point_P}{point_C} =  arg_theta ，求当△{point_A}{point_E}{point_F}的面积最大时，tan arg_theta 的值。",
    "en_problem": f"In tetrahedron {point_P}{point_A}{point_B}{point_C}, {point_P}{point_A} ⊥ plane {point_A}{point_B}{point_C}, ∠{point_A}{point_C}{point_B} = 90°, {point_A}{point_E} ⊥ {point_P}{point_B} at {point_E}, {point_A}{point_F} ⊥ {point_P}{point_C} at {point_F}. If {point_P}{point_A} = {point_A}{point_B} = {len_a} ({len_a} is a positive constant), ∠{point_B}{point_P}{point_C} =  arg_theta , find the value of tan arg_theta  when the area of triangle {point_A}{point_E}{point_F} is maximized.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_7_5({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
