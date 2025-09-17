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
point_A, point_B, point_C, point_D, point_M, point_N, point_P, point_T = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math

def calculate():
    """
    计算平面 MNA 与平面 MNT 夹角的余弦值

    返回:
    float: 夹角的余弦值
    """
    # 根据题干给出的解答公式: sqrt(6) / 3
    return math.sqrt(6) / 3


# 定义题干中的参数变量
len_side = 4.0  # 正方形边长 = 4

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate()
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_side = round(len_scaling_factor * float(len_side), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_4_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在边长为{len_side}的正方形{point_A}{point_B}{point_C}{point_D}中，{point_M}是{point_B}{point_C}的中点，{point_N}是{point_C}{point_D}的中点。将△{point_A}{point_B}{point_M}，△{point_A}{point_D}{point_N}分别沿{point_A}{point_M}，{point_A}{point_N}折叠，使{point_B}，{point_D}点重合于点{point_P}。在四棱锥{point_P}-{point_A}{point_M}{point_C}{point_N}中，满足{point_A}{point_T} = 3*{point_T}{point_P}，求平面{point_M}{point_N}{point_A}与平面{point_M}{point_N}{point_T}夹角的余弦值。",
    "en_problem": f"In square {point_A}{point_B}{point_C}{point_D} with side length {len_side}, {point_M} is the midpoint of {point_B}{point_C} and {point_N} is the midpoint of {point_C}{point_D}. Triangles {point_A}{point_B}{point_M} and {point_A}{point_D}{point_N} are folded along {point_A}{point_M} and {point_A}{point_N} respectively, so that points {point_B} and {point_D} coincide at point {point_P}. In pyramid {point_P}-{point_A}{point_M}{point_C}{point_N}, given {point_A}{point_T} = 3*{point_T}{point_P}, find the cosine of the angle between plane {point_M}{point_N}{point_A} and plane {point_M}{point_N}{point_T}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_4_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}', '{point_N}', '{point_P}', '{point_T}')"}, ensure_ascii=False) + "\n")
