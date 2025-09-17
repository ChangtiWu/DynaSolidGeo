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
point_P, point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate():
    """
    计算平面 PBD 与 平面 PBC 的夹角余弦值
    
    返回:
    float: cos 值
    """
    # 结果已知为 sqrt(5)/5
    return math.sqrt(5) / 5


# 题干给定的数值 (虽然最终结果不依赖具体数值，但按要求写上)
len_AB = 4.0

# AB // CD, AB ⊥ BC
# 侧面 PCD 是正三角形
# 侧面 PCD ⊥ 底面 ABCD

# 验证输出
# result = calculate()
# print(f"计算结果: {result:.6f}")

len_AB = round(len_scaling_factor * float(len_AB), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "zht_2_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}中,底面{point_A}{point_B}{point_C}{point_D}是直角梯形,{point_A}{point_B}//{point_C}{point_D}, {point_A}{point_B} ⊥ {point_B}{point_C},且{point_A}{point_B} = {point_B}{point_D} = 2*{point_C}{point_D} = {len_AB},侧面{point_P}{point_C}{point_D}是正三角形,侧面{point_P}{point_C}{point_D}⊥底面 {point_A}{point_B}{point_C}{point_D},{point_E}为{point_P}{point_C}中点,作{point_E}{point_F}⊥{point_P}{point_B}交{point_P}{point_B}于{point_F}. 求平面 {point_P}{point_B}{point_D}与平面 {point_P}{point_B}{point_C}的夹角的余弦值.",
    "en_problem": f"In the quadrangular pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, the base {point_A}{point_B}{point_C}{point_D} is a right trapezoid, {point_A}{point_B} // {point_C}{point_D}, {point_A}{point_B} ⊥ {point_B}{point_C}, and {point_A}{point_B} = {point_B}{point_D} = 2*{point_C}{point_D} = {len_AB}. The lateral face {point_P}{point_C}{point_D} is an equilateral triangle, and the lateral face {point_P}{point_C}{point_D} is perpendicular to the base {point_A}{point_B}{point_C}{point_D}. {point_E} is the midpoint of {point_P}{point_C}, and {point_E}{point_F} is drawn perpendicular to {point_P}{point_B}, intersecting {point_P}{point_B} at {point_F}. Find the cosine value of the angle between plane {point_P}{point_B}{point_D} and plane {point_P}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"zht_2_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
