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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_F, point_G = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math

def calculate(len_k):
    """
    计算正方体中平面 FBE 与平面 EBG 的夹角余弦值

    参数:
    len_k (float): CG : GC1 比值，即 CG = len_k * GC1

    返回:
    float: 余弦值
    """
    numerator = 6 * len_k + 2
    denominator = math.sqrt(5) * math.sqrt(9 * len_k**2 + 12 * len_k + 8)
    return abs(numerator / denominator)


# 题干给定的数值
len_a = 4.0  # 正方体棱长
len_k = 3.0  # CG : GC1 = 3 : 1

# 验证输出
#cos_theta = calculate(len_k)
#print(f"余弦值: {cos_theta:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_k = round(random.uniform(1.0, 5.0) * float(len_k), 2)

# Calculate the result
result = calculate(len_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee25_10_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"正方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}的棱长为{len_a}，{point_E}为{point_A1}{point_D1}的中点，{point_F}为{point_C1}{point_B1}的中点，{point_C}{point_G}={len_k}·{point_G}{point_C1}（即{point_C}{point_G}与{point_G}{point_C1}的长度比为{len_k}:1）。求平面{point_F}{point_B}{point_E}与平面{point_E}{point_B}{point_G}夹角的余弦值。",
    "en_problem": f"The edge length of cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} is {len_a}, {point_E} is the midpoint of {point_A1}{point_D1}, {point_F} is the midpoint of {point_C1}{point_B1}, {point_C}{point_G}={len_k}·{point_G}{point_C1} (i.e., the length ratio of {point_C}{point_G} to {point_G}{point_C1} is {len_k}:1). Find the cosine of the angle between plane {point_F}{point_B}{point_E} and plane {point_E}{point_B}{point_G}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee25_10_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_F}', '{point_G}')"}, ensure_ascii=False) + "\n")
