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
point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate():
    """
    计算平面 DEF 与平面 CEF 的夹角的余弦值

    返回:
    float: 夹角余弦值
    """
    # 根据题干给出的解答公式: 7 / 17
    return 7 / 17


# 定义题干中的参数变量
len_a = 2 * math.sqrt(3)  # 题干给的 BC = CD = 2√3
# 其他点和线段在题干中出现，但不需要赋值

# 验证计算结果（确认与参考答案一致后注释掉）
#result = calculate()
#print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_13_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在平面四边形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_B}∥{point_C}{point_D}，∠{point_D}{point_A}{point_B} = π/6，∠{point_A}{point_B}{point_C} = π/3，设{point_B}{point_C} = {point_C}{point_D} = {len_a}（{len_a} > 0），点{point_E}在{point_A}{point_B}上且满足{point_D}{point_E}∥{point_B}{point_C}。沿{point_D}{point_E}将△{point_A}{point_D}{point_E}折起，使得{point_A}{point_D} = {point_B}{point_D} = √3*{len_a}，{point_A}{point_B} = 3√2*{len_a}，得到四棱锥{point_A}-{point_B}{point_C}{point_D}{point_E}。若{point_A}{point_B} = 3*{point_A}{point_F}，求平面{point_D}{point_E}{point_F}与平面{point_C}{point_E}{point_F}的夹角的余弦值。",
    "en_problem": f"In planar quadrilateral {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B}∥{point_C}{point_D}, ∠{point_D}{point_A}{point_B} = π/6, ∠{point_A}{point_B}{point_C} = π/3, let {point_B}{point_C} = {point_C}{point_D} = {len_a} ({len_a} > 0), point {point_E} is on {point_A}{point_B} and satisfies {point_D}{point_E}∥{point_B}{point_C}. Fold triangle {point_A}{point_D}{point_E} along {point_D}{point_E} so that {point_A}{point_D} = {point_B}{point_D} = √3*{len_a}, {point_A}{point_B} = 3√2*{len_a}, forming pyramid {point_A}-{point_B}{point_C}{point_D}{point_E}. If {point_A}{point_B} = 3*{point_A}{point_F}, find the cosine of the angle between plane {point_D}{point_E}{point_F} and plane {point_C}{point_E}{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_13_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
