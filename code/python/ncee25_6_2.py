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
point_A, point_B, point_C, point_D, point_F, point_E, point_D_prime, point_A_prime = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math

def calculate(len_t):
    """
    计算四面体二面角的正弦值

    参数:
    len_t (float): 题干中定义的基本长度单元

    返回:
    float: 二面角的正弦值
    """
    return math.sqrt(42) / 7


# 题干给定的数值
len_t = 1.0  # 题干中长度单位比例，可任意正数

# 验证输出
#sin_theta = calculate(len_t)
#print(f"二面角正弦值: {sin_theta:.6f}")

# Generate random lengths
len_t = round(len_scaling_factor * float(len_t), 2)

# Calculate the result
result = calculate(len_t)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee25_6_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"设 {len_t}>0，四边形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_B} // {point_C}{point_D}，∠ {point_D}{point_A}{point_B}=90^\\circ，{point_F}为{point_C}{point_D}中点，{point_E}{point_F} // {point_A}{point_D}，且{point_A}{point_B}=3*{len_t}，{point_C}{point_D}=2*{len_t}。将四边形{point_E}{point_F}{point_D}{point_A}沿{point_E}{point_F}翻折至{point_E}{point_F}{point_D_prime}{point_A_prime}，使平面{point_E}{point_F}{point_D_prime}{point_A_prime}与平面{point_E}{point_F}{point_C}{point_B}成60^\\circ二面角，求面{point_B}{point_C}{point_D_prime}与面{point_E}{point_F}{point_D_prime}{point_A_prime}所成二面角的正弦值。",
    "en_problem": f"Let {len_t}>0, in quadrilateral {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B} // {point_C}{point_D}, ∠ {point_D}{point_A}{point_B}=90^\\circ, {point_F} is the midpoint of {point_C}{point_D}, {point_E}{point_F} // {point_A}{point_D}, and {point_A}{point_B}=3*{len_t}, {point_C}{point_D}=2*{len_t}. Fold quadrilateral {point_E}{point_F}{point_D}{point_A} along {point_E}{point_F} to {point_E}{point_F}{point_D_prime}{point_A_prime}, so that plane {point_E}{point_F}{point_D_prime}{point_A_prime} and plane {point_E}{point_F}{point_C}{point_B} form a 60^\\circ dihedral angle. Find the sine of the dihedral angle between {point_B}{point_C}{point_D_prime} and {point_E}{point_F}{point_D_prime}{point_A_prime}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee25_6_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_F}', '{point_E}', '{point_D_prime}', '{point_A_prime}')"}, ensure_ascii=False) + "\n")
