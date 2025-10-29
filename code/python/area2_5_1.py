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
point_P, point_A, point_B, point_C = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math

def calculate(len_a, len_b, len_c):
    """
    计算三棱锥 P-ABC 的表面积

    参数:
    len_a (float): PA
    len_b (float): PB
    len_c (float): PC

    返回:
    float: 表面积
    """
    # 根据题目给出的解答公式
    return 0.5 * (len_a * len_b + len_a * len_c + len_b * len_c) + 0.5 * math.sqrt(len_a**2 * len_b**2 + len_b**2 * len_c**2 + len_a**2 * len_c**2)


# 定义题干中的参数
len_a = 2 * math.sqrt(7)   # PA
len_b = 2 * math.sqrt(2)   # PB
len_c = 2 * math.sqrt(2)   # PC

# 验证计算结果
#result = calculate(len_a, len_b, len_c)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_5_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"在三棱锥 {point_P} - {point_A}{point_B}{point_C} 中，{point_P}{point_A}，{point_P}{point_B}，{point_P}{point_C} 两两垂直，设 {point_P}{point_A} = {len_a}，{point_P}{point_B} = {len_b}，{point_P}{point_C} = {len_c}，求三棱锥 {point_P} - {point_A}{point_B}{point_C} 的表面积。",
    "en_problem": f"In triangular pyramid {point_P} - {point_A}{point_B}{point_C}, edges {point_P}{point_A}, {point_P}{point_B}, and {point_P}{point_C} are mutually perpendicular. Let {point_P}{point_A} = {len_a}, {point_P}{point_B} = {len_b}, and {point_P}{point_C} = {len_c}. Find the surface area of triangular pyramid {point_P} - {point_A}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"area2_5_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}')"}, ensure_ascii=False) + "\n")
