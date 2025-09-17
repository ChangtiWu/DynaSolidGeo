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
point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math

def calculate(len_a, arg_theta):
    """
    计算点 D 到平面 ABC 的距离

    参数:
    len_a (float): 等腰三角形腰长 AB = AC
    arg_theta (float): ∠BAC 的角度（单位：弧度，π/2 < arg_theta < π）

    返回:
    float: 距离
    """
    # 根据题干给出的解答公式: (len_a / 2) * sqrt(4 * cot^2(arg_theta/2) - 1)
    return (len_a / 2) * math.sqrt(4 * (1 / math.tan(arg_theta / 2)) ** 2 - 1)


# 定义题干中的参数变量
len_a = 2.0                    # AB = AC = 2
arg_theta = math.radians(120)  # ∠BAC = 120°

# 验证计算结果（确认与参考答案一致后注释掉）
#result = calculate(len_a, arg_theta)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz2_8_1",
    "type": 8,
    "level": 1,
    "cn_problem": f"在等腰三角形{point_A}{point_B}{point_C}中，{point_A}{point_B} = {point_A}{point_C} = {len_a}，∠{point_B}{point_A}{point_C} = {arg_theta}（\\frac{{π}}{{2}} < {arg_theta} < π），{point_D}为{point_B}{point_C}上一点，且{point_A}{point_D} ⊥ {point_A}{point_B}。将三角形{point_B}{point_A}{point_D}沿{point_A}{point_D}翻折，使平面{point_A}{point_B}{point_D} ⊥ 平面{point_A}{point_C}{point_D}，连接{point_B}{point_C}，求点{point_D}到平面{point_A}{point_B}{point_C}的距离。",
    "en_problem": f"In isosceles triangle {point_A}{point_B}{point_C}, {point_A}{point_B} = {point_A}{point_C} = {len_a}, ∠{point_B}{point_A}{point_C} = {arg_theta} (\\frac{{π}}{{2}} < {arg_theta} < π), {point_D} is a point on {point_B}{point_C} such that {point_A}{point_D} ⊥ {point_A}{point_B}. Triangle {point_B}{point_A}{point_D} is folded along {point_A}{point_D} so that plane {point_A}{point_B}{point_D} ⊥ plane {point_A}{point_C}{point_D}, connecting {point_B}{point_C}. Find the distance from point {point_D} to plane {point_A}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"fz2_8_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
