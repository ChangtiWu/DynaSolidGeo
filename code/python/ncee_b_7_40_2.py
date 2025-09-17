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
point_D, point_E, point_F, point_A, point_B, point_C, point_G, point_H = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math

def calculate():
    """
    计算平面 FGH 与平面 ACFD 的锐角大小（度数）

    返回:
    float: 锐角（单位：度）
    """
    # 已知结果
    return 60.0


# 题干给定的数值
len_m = 1.0        # DE 长度（单位可任意）
arg_alpha = math.radians(45)  # ∠BAC = 45°

# print(calculate(arg_gamma))


# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_40_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在三棱台{point_D}{point_E}{point_F}-{point_A}{point_B}{point_C}中，{point_A}{point_B} = 2{point_D}{point_E}，{point_G}、{point_H}分别为{point_A}{point_C}、{point_B}{point_C}的中点。已知{point_C}{point_F} ⊥ 平面{point_A}{point_B}{point_C}，{point_A}{point_B} ⊥ {point_B}{point_C}，∠{point_B}{point_A}{point_C} = {arg_alpha}，且{point_C}{point_F} = {point_D}{point_E} = {len_m}。求平面{point_F}{point_G}{point_H}与平面{point_A}{point_C}{point_F}{point_D}所成角（锐角）的大小。",
    "en_problem": f"In triangular frustum {point_D}{point_E}{point_F}-{point_A}{point_B}{point_C}, {point_A}{point_B} = 2{point_D}{point_E}, and {point_G}, {point_H} are midpoints of {point_A}{point_C}, {point_B}{point_C} respectively. Given that {point_C}{point_F} ⊥ plane {point_A}{point_B}{point_C}, {point_A}{point_B} ⊥ {point_B}{point_C}, ∠{point_B}{point_A}{point_C} = {arg_alpha}, and {point_C}{point_F} = {point_D}{point_E} = {len_m}. Find the measure of the acute angle between plane {point_F}{point_G}{point_H} and plane {point_A}{point_C}{point_F}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_40_2({mode}, {azimuth}, {elevation}, '{point_D}', '{point_E}', '{point_F}', '{point_A}', '{point_B}', '{point_C}', '{point_G}', '{point_H}')"}, ensure_ascii=False) + "\n")
