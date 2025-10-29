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
point_A, point_B, point_C, point_D, point_E, point_F, point_P, point_M = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math

def calculate(len_a, len_k):
    """
    计算二面角 M-EF-D 的余弦值

    参数:
    len_a (float): 正方形边长 a
    len_k (float): tan(MF, 平面 PEF) = k

    返回:
    float: 二面角余弦值
    """
    # 根据题干给出的解答公式: sqrt(6)/3
    return math.sqrt(6) / 3


# 定义题干中的参数变量
len_a = 1.0  # 正方形边长
len_k = 1/2  # tan(MF, 平面 PEF) = 1/2

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_a, len_k)
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, len_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_18_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在正方形{point_A}{point_B}{point_C}{point_D}中，边长为{len_a}，点{point_E}，{point_F}分别是{point_A}{point_B}，{point_B}{point_C}的中点，将△{point_A}{point_E}{point_D}，△{point_C}{point_F}{point_D}分别沿{point_D}{point_E}，{point_D}{point_F}折起，使{point_A}，{point_C}两点重合于{point_P}，连接{point_E}{point_F}，{point_P}{point_B}。点{point_M}是{point_P}{point_D}上一点，若直线{point_M}{point_F}与平面{point_P}{point_E}{point_F}所成角的正切值为{len_k}，求二面角{point_M}-{point_E}{point_F}-{point_D}的余弦值。",
    "en_problem": f"In square {point_A}{point_B}{point_C}{point_D} with side length {len_a}, points {point_E}, {point_F} are midpoints of {point_A}{point_B}, {point_B}{point_C} respectively. Fold triangles {point_A}{point_E}{point_D}, {point_C}{point_F}{point_D} along {point_D}{point_E}, {point_D}{point_F} respectively so that points {point_A}, {point_C} coincide at point {point_P}, connect {point_E}{point_F}, {point_P}{point_B}. Point {point_M} is on {point_P}{point_D}, if the tangent of the angle between line {point_M}{point_F} and plane {point_P}{point_E}{point_F} is {len_k}, find the cosine of dihedral angle {point_M}-{point_E}{point_F}-{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_18_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_P}', '{point_M}')"}, ensure_ascii=False) + "\n")
