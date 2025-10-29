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
point_A, point_B, point_C, point_D, point_M, point_N, point_E, point_F, point_P = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math

def calculate():
    """
    计算二面角 F-ND-P 的正弦值

    参数:
    无

    返回:
    float: 二面角正弦值
    """
    # 根据题干给出的解答公式: sqrt(6) / 3
    return math.sqrt(6) / 3


# 题干参数变量（数值参数在公式中未使用，也可以不定义）
len_a = 1.0  # AB = 1

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate()
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_6_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"四边形{point_A}{point_B}{point_C}{point_D}中{point_A}{point_D}∥{point_B}{point_C}，{point_A}{point_B} = {len_a}，{point_A}{point_D} = 2*{len_a}，{point_B}{point_C} = 3*{len_a}，∠{point_A}{point_B}{point_C} = π/2，{point_M}为{point_A}{point_D}的中点，{point_N}为{point_B}{point_C}上一点，且{point_M}{point_N}∥{point_A}{point_B}。将四边形{point_A}{point_B}{point_N}{point_M}沿{point_M}{point_N}翻折，使得{point_A}{point_B}与{point_E}{point_F}重合，得到几何体{point_M}{point_D}{point_C}{point_N}{point_F}{point_E}，其中{point_F}{point_D} = √3*{len_a}。若{point_P}为{point_F}{point_C}的中点，求二面角{point_F}-{point_N}{point_D}-{point_P}的正弦值。",
    "en_problem": f"In quadrilateral {point_A}{point_B}{point_C}{point_D}, {point_A}{point_D}∥{point_B}{point_C}, {point_A}{point_B} = {len_a}, {point_A}{point_D} = 2*{len_a}, {point_B}{point_C} = 3*{len_a}, ∠{point_A}{point_B}{point_C} = π/2, {point_M} is the midpoint of {point_A}{point_D}, {point_N} is a point on {point_B}{point_C}, and {point_M}{point_N}∥{point_A}{point_B}. Fold quadrilateral {point_A}{point_B}{point_N}{point_M} along {point_M}{point_N} so that {point_A}{point_B} coincides with {point_E}{point_F}, obtaining geometric solid {point_M}{point_D}{point_C}{point_N}{point_F}{point_E}, where {point_F}{point_D} = √3*{len_a}. If {point_P} is the midpoint of {point_F}{point_C}, find the sine of dihedral angle {point_F}-{point_N}{point_D}-{point_P}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_6_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_M}', '{point_N}', '{point_E}', '{point_F}', '{point_P}')"}, ensure_ascii=False) + "\n")
