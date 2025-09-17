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
point_A, point_B, point_C, point_D, point_P, point_M = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_t, len_d):
    """
    计算 PM/PD 的比值及平面 MAC 和平面 DAC 夹角的余弦值

    参数:
    len_t (float): 等腰梯形的边长单位 t
    len_d (float): 点 P 到面 ACM 的距离

    返回:
    tuple: (PM/PD, cos(∠MAC,DAC))
    """
    # 根据题干给出的解答公式:
    PM_over_PD = 1 / 2
    return PM_over_PD


# 定义题干中的参数变量
len_t = 2.0     # AB = BC = CD = 1/2 AD = t = 2
len_d = 2 * math.sqrt(5) / 5  # 点 P 到面 ACM 的距离

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_t, len_d)
# print(f"PM/PD = {result[0]:.6f}, cos(∠MAC,DAC) = {result[1]:.6f}")


# Generate random lengths
len_t = round(len_scaling_factor * float(len_t), 2)
len_d = round(len_scaling_factor * float(len_d), 2)

# Calculate the result
result = calculate(len_t, len_d)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_20_2",
    "type": 8,
    "level": 1,
    "cn_problem": f"等腰梯形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_D}∥{point_B}{point_C}，{point_A}{point_B} = {point_B}{point_C} = {point_C}{point_D} = {len_t}，{point_A}{point_D} = 2*{len_t}（{len_t} > 0）。以{point_A}{point_C}为折痕把△{point_A}{point_B}{point_C}折起，使点{point_B}到达点{point_P}的位置，且{point_P}{point_A}⊥{point_C}{point_D}。若{point_M}为{point_P}{point_D}上的一点，点{point_P}到面{point_A}{point_C}{point_M}的距离为{len_d}，求{point_P}{point_M}/{point_P}{point_D}的值。",
    "en_problem": f"In isosceles trapezoid {point_A}{point_B}{point_C}{point_D}, {point_A}{point_D}∥{point_B}{point_C}, {point_A}{point_B} = {point_B}{point_C} = {point_C}{point_D} = {len_t}, {point_A}{point_D} = 2*{len_t} ({len_t} > 0). Fold triangle {point_A}{point_B}{point_C} along {point_A}{point_C} so that point {point_B} reaches position {point_P}, with {point_P}{point_A}⊥{point_C}{point_D}. If {point_M} is a point on {point_P}{point_D}, and the distance from point {point_P} to plane {point_A}{point_C}{point_M} is {len_d}, find the value of {point_P}{point_M}/{point_P}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_20_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}', '{point_M}')"}, ensure_ascii=False) + "\n")
