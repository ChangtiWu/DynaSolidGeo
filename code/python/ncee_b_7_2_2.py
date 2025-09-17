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
point_A, point_B, point_C, point_D, point_E, point_F, point_O, point_M = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math

def calculate(len_a, len_c):
    """
    计算二面角 F-BM-E 的正弦值

    参数:
    len_a (float): 梯形短边（AB = BC = EF = len_a, AD = 2*len_a）
    len_c (float): ED 的长度

    返回:
    float: sin(∠(F-BM-E))
    """
    numerator = 4 * math.sqrt(3) * len_a * math.sqrt(4 * (len_c**2) - (len_a**2))
    denominator = 16 * (len_c**2) - (len_a**2)
    return numerator / denominator


# ====== 代入题目给的数据验证 ======
len_a = 2
len_c = math.sqrt(10)

# print(calculate(len_a, S, T))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_2_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在五面体中，四边形{point_A}{point_B}{point_C}{point_D}和{point_A}{point_D}{point_E}{point_F}均为等腰梯形，满足：{point_E}{point_F} ∥ {point_A}{point_D}，{point_B}{point_C} ∥ {point_A}{point_D}，{point_A}{point_D} = 2{len_a}，{point_A}{point_B} = {point_B}{point_C} = {point_E}{point_F} = {len_a}，{point_E}{point_D} = {len_c}，且{point_F}{point_B} = √({len_c}^2 + {len_a}^2/2)（保证{point_O}{point_F} ⊥ {point_O}{point_B}，{point_O}为{point_A}{point_M}中点）。{point_M}为{point_A}{point_D}的中点，求二面角{point_F}-{point_B}{point_M}-{point_E}的正弦值。",
    "en_problem": f"In a pentahedron, quadrilaterals {point_A}{point_B}{point_C}{point_D} and {point_A}{point_D}{point_E}{point_F} are both isosceles trapezoids satisfying: {point_E}{point_F} ∥ {point_A}{point_D}, {point_B}{point_C} ∥ {point_A}{point_D}, {point_A}{point_D} = 2{len_a}, {point_A}{point_B} = {point_B}{point_C} = {point_E}{point_F} = {len_a}, {point_E}{point_D} = {len_c}, and {point_F}{point_B} = √({len_c}^2 + {len_a}^2/2) (ensuring {point_O}{point_F} ⊥ {point_O}{point_B}, where {point_O} is the midpoint of {point_A}{point_M}). {point_M} is the midpoint of {point_A}{point_D}. Find the sine value of dihedral angle {point_F}-{point_B}{point_M}-{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_2_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_O}', '{point_M}')"}, ensure_ascii=False) + "\n")
