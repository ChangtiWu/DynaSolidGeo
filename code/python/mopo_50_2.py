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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_P, point_F = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math

def calculate(len_h):
    """
    计算三棱锥P-B1CF体积的最小值

    参数:
    len_h (float): 长方体的高，即len_AE = len_AA1

    返回:
    float: 三棱锥体积的最小值
    """
    # △B1CF的面积 S = √3 * len_h^2 / 2
    S = math.sqrt(3) * len_h ** 2 / 2

    # 点P到平面B1CF的距离公式中的参数部分 d = |len_h * (2√6/3 * sin(θ + π/4) - 3)| / √3
    # 当 sin(θ + π/4) = 1 时，d取得最小值 d_min
    sin_term = math.sqrt(2)  # sin(θ + π/4)的最大值为1, 则 2√6/3 * 1 = 2√6/3
    d_min_numerator = abs(2 * math.sqrt(6) / 3 * 1 - 3) * len_h
    d_min = d_min_numerator / math.sqrt(3)

    # 三棱锥体积 V_min = (1/3) * S * d_min
    V_min = (1/3) * S * d_min

    # 简化表达式 V_min = len_h^3 * (9 - 2√6) / 18
    # 计算数值结果
    V_min_simplified = (len_h ** 3) * (9 - 2 * math.sqrt(6)) / 18
    return V_min_simplified

# 示例使用
len_h = 3
# min_volume = calculate(len_h)
# print(f"三棱锥体积的最小值为: {min_volume:.6f}")
# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_50_2",
    "type": 7,
    "level": 3,
    "cn_problem": f"在长方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}中，设{point_A}{point_B} = 2*{point_A}{point_D} = 2*{point_A}{point_A1} = 2*{len_h}（即{point_A}{point_D} = {point_A}{point_A1} = {len_h}，{point_A}{point_B} = 2*{len_h}）。点{point_E}在棱{point_A}{point_B}上，满足{point_B}{point_E} = 2*{point_A}{point_E}（故{point_A}{point_E} = 2*{len_h}/3，{point_B}{point_E} = 4*{len_h}/3）。动点{point_P}满足{point_B}{point_P} = √3*{point_E}{point_P}且在平面{point_A}{point_B}{point_C}{point_D}内运动，{point_F}为{point_C1}{point_D1}的中点，求三棱锥{point_P}-{point_B1}{point_C}{point_F}体积的最小值。",
    "en_problem": f"In cuboid {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, let {point_A}{point_B} = 2*{point_A}{point_D} = 2*{point_A}{point_A1} = 2*{len_h} (i.e., {point_A}{point_D} = {point_A}{point_A1} = {len_h}, {point_A}{point_B} = 2*{len_h}). Point {point_E} is on edge {point_A}{point_B}, satisfying {point_B}{point_E} = 2*{point_A}{point_E} (so {point_A}{point_E} = 2*{len_h}/3, {point_B}{point_E} = 4*{len_h}/3). Moving point {point_P} satisfies {point_B}{point_P} = √3*{point_E}{point_P} and moves within plane {point_A}{point_B}{point_C}{point_D}, {point_F} is the midpoint of {point_C1}{point_D1}. Find the minimum volume of triangular pyramid {point_P}-{point_B1}{point_C}{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_50_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_P}', '{point_F}')"}, ensure_ascii=False) + "\n")
