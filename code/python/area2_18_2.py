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
point_P, point_A, point_B, point_C, point_O, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
def calculate():
    """
    返回三棱锥平面夹角 cosα 的最大值

    返回: cosα_max
    """
    # 最小值
    cos_alpha_min = 0
    # 最大值趋近于 sqrt(21)/7
    cos_alpha_max = (21 ** 0.5) / 7
    return cos_alpha_max


# 定义题干中的参数（仅数值参数，点名不用定义）
len_a = 2.0
len_b = 2 ** 0.5
arg_cos_theta0 = math.sqrt(2) / 4
# 验证计算结果
#cos_min, cos_max = calculate()
#print(f"cosα 最小值: {cos_min:.6f}, 最大值: {cos_max:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)



# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_18_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在三棱锥 {point_P} - {point_A}{point_B}{point_C} 中，底面 {point_A}{point_B}{point_C} 是边长为 {len_a} 的等边三角形，{point_P}{point_A} = {point_P}{point_C} = {len_b}，异面直线 {point_P}{point_C} 与 {point_A}{point_B} 所成角的余弦值为 {arg_cos_theta0}。点 {point_F} 是线段 {point_P}{point_B}（不含端点）上的动点。平面 {point_A}{point_C}{point_F} 与平面 {point_P}{point_B}{point_C} 的夹角为 arg_alpha ，求 cos arg_alpha 的最大值。",
    "en_problem": f"In the tetrahedron {point_P} - {point_A}{point_B}{point_C}, the base {point_A}{point_B}{point_C} is an equilateral triangle with side length {len_a}, and {point_P}{point_A} = {point_P}{point_C} = {len_b}. The cosine of the angle between the skew lines {point_P}{point_C} and {point_A}{point_B} is {arg_cos_theta0}. Point {point_F} moves along segment {point_P}{point_B} (excluding endpoints). The plane {point_A}{point_C}{point_F} forms an angle arg_alpha with plane {point_P}{point_B}{point_C}. Find the maximum value of cos arg_alpha.",
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
    f.write(json.dumps({json_data["id"]: f"area2_18_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_O}', '{point_F}')"}, ensure_ascii=False) + "\n")
