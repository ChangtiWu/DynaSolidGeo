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
point_A, point_B, point_C, point_D, point_E, point_F, point_G, point_M = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算四面体 ADFM 的外接球半径

    参数:
    len_a (float): 基本长度单位 a

    返回:
    float: 外接球半径
    """
    # 根据题干给出的解答公式: sqrt(5) * len_a
    return math.sqrt(5) * len_a


# 定义题干中的参数变量
len_a = 1.0  # 题干里的“a”，这里给一个数值方便验证

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_a)
# print(f"计算结果: {result:.6f}")



# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_2_1",
    "type": 8,
    "level": 2,
    "cn_problem": f"在矩形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_B} = 4*{len_a}，{point_A}{point_D} = 3*{len_a}，{point_A}{point_B} = 4*{point_A}{point_E}，{point_E}，{point_F}，{point_G}分别在线段{point_B}{point_E}，{point_B}{point_C}上，且{point_F}{point_G}∥{point_C}{point_E}。将△{point_B}{point_F}{point_G}沿{point_F}{point_G}折起，使{point_B}到达{point_M}的位置，且平面{point_F}{point_G}{point_M}⊥平面{point_A}{point_D}{point_C}{point_G}{point_F}。若直线{point_D}{point_M}与平面{point_A}{point_D}{point_C}{point_G}{point_F}所成角的正切值为√37/37，求四面体{point_A}{point_D}{point_F}{point_M}的外接球半径。",
    "en_problem": f"In rectangle {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B} = 4*{len_a}, {point_A}{point_D} = 3*{len_a}, {point_A}{point_B} = 4*{point_A}{point_E}, {point_E}, {point_F}, {point_G} are respectively on segments {point_B}{point_E}, {point_B}{point_C}, and {point_F}{point_G}∥{point_C}{point_E}. Triangle {point_B}{point_F}{point_G} is folded along {point_F}{point_G} so that {point_B} reaches position {point_M}, and plane {point_F}{point_G}{point_M}⊥plane {point_A}{point_D}{point_C}{point_G}{point_F}. If the tangent of the angle between line {point_D}{point_M} and plane {point_A}{point_D}{point_C}{point_G}{point_F} is √37/37, find the radius of the circumsphere of tetrahedron {point_A}{point_D}{point_F}{point_M}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_2_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_G}', '{point_M}')"}, ensure_ascii=False) + "\n")
