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
point_P, point_A, point_B, point_C, point_D, point_M, point_N = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate():
    """
    计算直线 CD 与平面 AMN 所成角（弧度）

    返回:
    float: 角度（弧度）
    """
    # 已知结果
    return math.asin(math.sqrt(3)/3)


# 题干给定的数值
len_a = 2.0   # PA = AD = 2

# 验证输出
# angle = calculate()
# print(f"直线 CD 与平面 AMN 所成角（弧度）: {angle:.6f}")
# print(f"角度制: {math.degrees(angle):.2f}°")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_6_18",
    "type": 2,
    "level": 2,
    "cn_problem": f"如图，{point_P}为正方形{point_A}{point_B}{point_C}{point_D}外一点，且{point_P}{point_A} ⊥ 平面{point_A}{point_B}{point_C}{point_D}，{point_P}{point_A} = {point_A}{point_D} = {len_a}（{len_a} > 0），点{point_M}、{point_N}分别在棱{point_P}{point_D}、{point_P}{point_C}上，且{point_P}{point_C} ⊥ 平面{point_A}{point_M}{point_N}。求直线{point_C}{point_D}和平面{point_A}{point_M}{point_N}所成角的大小。",
    "en_problem": f"As shown in the figure, {point_P} is a point outside square {point_A}{point_B}{point_C}{point_D}, with {point_P}{point_A} ⊥ plane {point_A}{point_B}{point_C}{point_D}, {point_P}{point_A} = {point_A}{point_D} = {len_a} ({len_a} > 0). Points {point_M} and {point_N} are on edges {point_P}{point_D} and {point_P}{point_C} respectively, and {point_P}{point_C} ⊥ plane {point_A}{point_M}{point_N}. Find the angle between line {point_C}{point_D} and plane {point_A}{point_M}{point_N}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_6_18({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
