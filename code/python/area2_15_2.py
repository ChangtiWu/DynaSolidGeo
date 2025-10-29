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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1 = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math

def calculate(len_a, len_b, len_h):
    """
    计算圆台体积

    参数:
    len_a (float): 上底边长
    len_b (float): 下底边长
    len_h (float): 圆台高

    返回:
    float: 圆台体积
    """
    # 根据题解公式 V = π * len_h / 12 * (len_a^2 + len_a * len_b + len_b^2)
    return math.pi * len_h / 12 * (len_a ** 2 + len_a * len_b + len_b ** 2)


# 定义题干中的参数
len_a = 20.0  # 上底边长
len_b = 40.0  # 下底边长
len_h = 30.0  # 圆台高

# 验证计算结果
#volume_V = calculate(len_a, len_b, len_h)
#print(f"圆台体积: {volume_V:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_b, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_15_2",
    "type": 4,
    "level": 1,
    "cn_problem": f"一个正四棱台 {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1}，上底边长为 {len_a}，下底边长为 {len_b}，高为 {len_h}。若将该四棱台最大限度地打磨成一个圆台，且圆台的上、下底面分别内切于四棱台的上、下底正方形，高为四棱台的高，求圆台的体积。",
    "en_problem": f"A square frustum {point_A}{point_B}{point_C}{point_D} - {point_A1}{point_B1}{point_C1}{point_D1} has upper base side length {len_a}, lower base side length {len_b}, and height {len_h}. If the frustum is maximally carved into a circular frustum with the top and bottom circles inscribed in the squares of the frustum and height equal to that of the frustum, find the volume of the circular frustum.",
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
    f.write(json.dumps({json_data["id"]: f"area2_15_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}')"}, ensure_ascii=False) + "\n")
