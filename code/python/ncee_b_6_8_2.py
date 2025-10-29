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

def calculate(len_a, len_b, len_c):
    """
    计算直线 AN 与平面 PDM 所成角的正弦值

    参数:
    len_a (float): 长度参数 a
    len_b (float): 长度参数 b
    len_c (float): 长度参数 c

    返回:
    float: 计算结果
    """
    # 计算 √(len_b² / 4 - len_a²)
    sqrt_term = math.sqrt(len_b ** 2 / 4 - len_a ** 2)

    # 计算向量 AN 的坐标分量
    an_x = 3 * sqrt_term / 2
    an_y = -5 * len_a / 2
    an_z = math.sqrt(len_c ** 2 - 3 * len_a ** 2 - len_b ** 2 / 4) / 2

    # 计算向量 AN 的模长
    magnitude_an = math.sqrt(an_x ** 2 + an_y ** 2 + an_z ** 2)

    # 平面 PDM 的法向量可取 (0, 1, 0)，其模长为 1
    magnitude_n = 1

    # 计算向量 AN 与法向量 n 点积的绝对值
    dot_product_abs = abs(an_y)

    # 计算直线 AN 与平面 PDM 所成角的正弦值
    sin_theta = dot_product_abs / (magnitude_an * magnitude_n)

    return sin_theta


len_a = 1
len_b = 4
len_c = math.sqrt(15)
arg_theta = math.pi * 2 / 3
# print(calculate(len_a, len_b, len_p))

# Generate random lengths

len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_8_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}中，底面{point_A}{point_B}{point_C}{point_D}是平行四边形，∠{point_A}{point_B}{point_C} = {arg_theta}（满足cos{arg_theta} = -2{len_a}/{len_b}，且{len_b} > 2{len_a}），{point_A}{point_B} = {len_a}，{point_B}{point_C} = {len_b}，{point_P}{point_A} = {len_c}。{point_M}、{point_N}分别为{point_B}{point_C}、{point_P}{point_C}的中点，{point_P}{point_D} ⊥ {point_D}{point_C}，{point_P}{point_M} ⊥ {point_M}{point_D}。求直线{point_A}{point_N}与平面{point_P}{point_D}{point_M}所成角的正弦值。",
    "en_problem": f"In quadrilateral pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, the base {point_A}{point_B}{point_C}{point_D} is a parallelogram, ∠{point_A}{point_B}{point_C} = {arg_theta} (satisfying cos{arg_theta} = -2{len_a}/{len_b}, and {len_b} > 2{len_a}), {point_A}{point_B} = {len_a}, {point_B}{point_C} = {len_b}, {point_P}{point_A} = {len_c}. {point_M} and {point_N} are the midpoints of {point_B}{point_C} and {point_P}{point_C} respectively, {point_P}{point_D} ⊥ {point_D}{point_C}, {point_P}{point_M} ⊥ {point_M}{point_D}. Find the sine of the angle between line {point_A}{point_N} and plane {point_P}{point_D}{point_M}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_8_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
