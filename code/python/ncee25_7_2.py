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
point_P, point_A, point_B, point_C, point_D, point_O = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_a, len_b, len_c, len_height):
    """
    计算直线 AC 与直线 PO 所成角的余弦值

    参数:
    len_a (float): AB
    len_b (float): AD
    len_c (float): BC
    len_height (float): PA

    返回:
    float: 余弦值
    """
    numerator = len_c**2
    denominator = 2 * math.sqrt((len_a**2 + len_c**2) * (len_c**2 / 4 + len_height**2))
    return numerator / denominator


# 题干给定的数值
len_height = math.sqrt(2)  # PA
len_a = math.sqrt(2)       # AB
len_b = 1 + math.sqrt(3)   # AD
len_c = 2                   # BC

# 验证输出
#cos_theta = calculate(len_a, len_b, len_c, len_height)
#print(f"余弦值: {cos_theta:.6f}")

# Generate random lengths
len_height = round(len_scaling_factor * float(len_height), 2)
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c, len_height)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee25_7_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}中，{point_P}{point_A}⊥平面{point_A}{point_B}{point_C}{point_D}，{point_A}{point_B}⊥{point_A}{point_D}，{point_B}{point_C}∥{point_A}{point_D}。设{point_P}{point_A}={len_height}，{point_A}{point_B}={len_a}，{point_A}{point_D}={len_b}，{point_B}{point_C}={len_c}，且满足{len_a}^2={len_b}^2-{len_b}{len_c}（保证{point_P}、{point_B}、{point_C}、{point_D}共球且球心{point_O}在平面{point_A}{point_B}{point_C}{point_D}上）。已知该球的球心为{point_O}，求直线{point_A}{point_C}与直线{point_P}{point_O}所成角的余弦值。",
    "en_problem": f"In the quadrangular pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, {point_P}{point_A}⊥plane {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B}⊥{point_A}{point_D}, {point_B}{point_C}∥{point_A}{point_D}. Let {point_P}{point_A}={len_height}, {point_A}{point_B}={len_a}, {point_A}{point_D}={len_b}, {point_B}{point_C}={len_c}, and satisfy {len_a}^2={len_b}^2-{len_b}{len_c} (ensuring {point_P}, {point_B}, {point_C}, {point_D} are concyclic and the center {point_O} lies on plane {point_A}{point_B}{point_C}{point_D}). Given that the center of the sphere is {point_O}, find the cosine of the angle between line {point_A}{point_C} and line {point_P}{point_O}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee25_7_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}')"}, ensure_ascii=False) + "\n")
