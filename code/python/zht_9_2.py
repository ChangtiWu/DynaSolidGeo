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
point_A, point_B, point_C, point_A1, point_B1, point_C1 = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_a, arg_theta):
    """
    计算拟柱体 ABC-A1B1C1 的体积

    参数:
    len_a (float): 棱长
    arg_theta (float): AC1 与平面 A1B1C1 所成角（弧度）

    返回:
    float: 拟柱体体积
    """
    return (math.sqrt(3) / 3) * len_a**3 * math.sin(arg_theta)


# 题干给定的数值
len_a = 1.0
arg_theta = math.radians(60)  # 题目中给的角为 60°

# 验证输出
#volume = calculate(len_a, arg_theta)
#print(f"拟柱体体积: {volume:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
arg_theta = round(random.uniform(0.9, 1.1) * float(arg_theta), 2)

# Calculate the result
result = calculate(len_a, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "zht_9_2",
    "type": 5,
    "level": 2,
    "cn_problem": f"设几何体 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 的所有棱长均为 {len_a}（即 {point_A}{point_B}={point_B}{point_C}={point_C}{point_A}={point_A1}{point_B1}={point_B1}{point_C1}={point_C1}{point_A1}={point_A}{point_A1}={point_B}{point_B1}={point_C}{point_C1}={len_a}），且 {point_A}{point_B} ∥ {point_A1}{point_B1}，{point_B}{point_C} ∥ {point_B1}{point_C1}。已知 {point_A}{point_C1} 与平面 {point_A1}{point_B1}{point_C1} 所成的角为 {arg_theta}，求该拟柱体的体积。",
    "en_problem": f"Let all edge lengths of geometric body {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} be {len_a} (i.e., {point_A}{point_B}={point_B}{point_C}={point_C}{point_A}={point_A1}{point_B1}={point_B1}{point_C1}={point_C1}{point_A1}={point_A}{point_A1}={point_B}{point_B1}={point_C}{point_C1}={len_a}), and {point_A}{point_B} ∥ {point_A1}{point_B1}, {point_B}{point_C} ∥ {point_B1}{point_C1}. Given that the angle between {point_A}{point_C1} and plane {point_A1}{point_B1}{point_C1} is {arg_theta}, find the volume of this prismatoid.",
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
    f.write(json.dumps({json_data["id"]: f"zht_9_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}')"}, ensure_ascii=False) + "\n")
