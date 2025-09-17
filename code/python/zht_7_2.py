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
point_A, point_B, point_C, point_D, point_E, point_P, point_M, point_N = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math

def calculate():
    """
    计算直线 EN 与平面 PBC 所成角的正弦值

    返回:
    float: 正弦值
    """
    # 已知结果
    return 3 * math.sqrt(26) / 26


# 题干给定的数值
len_a = 1.0       # AB/2 = BC = DC = 1（单位可任意，按比例）
# AB = 2DC = 2BC = 2*len_a
# E 为 AB 中点，M 为 PB 中点，N 为 BC 上动点
# 折起形成三棱锥 M-EBN 和四棱锥 P-EBCD，体积比 1/6

# 验证输出
# result = calculate()
# print(f"正弦值: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "zht_7_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在直角梯形 {point_A}{point_B}{point_C}{point_D} 中，{point_A}{point_B} ∥ {point_D}{point_C}，∠{point_A}{point_B}{point_C} = 90°，设 {point_A}{point_B} = 2*{point_D}{point_C} = 2*{point_B}{point_C} = 2*{len_a}（即 {point_D}{point_C} = {point_B}{point_C} = {len_a}），{point_E} 为 {point_A}{point_B} 中点，故 {point_A}{point_E} = {point_E}{point_B} = {len_a}，四边形 {point_E}{point_B}{point_C}{point_D} 为正方形。沿 {point_D}{point_E} 折起 △{point_A}{point_D}{point_E} 至 △{point_P}{point_D}{point_E}，使 {point_P}{point_E} ⊥ {point_E}{point_B}。{point_M} 为 {point_P}{point_B} 中点，{point_N} 是 {point_B}{point_C} 上动点，满足 V_{point_M}-{point_E}{point_B}{point_N}/V_{point_P}-{point_E}{point_B}{point_C}{point_D} = 1/6，求直线 {point_E}{point_N} 与平面 {point_P}{point_B}{point_C} 所成角的正弦值。",
    "en_problem": f"In the right trapezoid {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B} ∥ {point_D}{point_C}, ∠{point_A}{point_B}{point_C} = 90°, let {point_A}{point_B} = 2*{point_D}{point_C} = 2*{point_B}{point_C} = 2*{len_a} (i.e., {point_D}{point_C} = {point_B}{point_C} = {len_a}), {point_E} is the midpoint of {point_A}{point_B}, so {point_A}{point_E} = {point_E}{point_B} = {len_a}, quadrilateral {point_E}{point_B}{point_C}{point_D} is a square. Fold △{point_A}{point_D}{point_E} along {point_D}{point_E} to △{point_P}{point_D}{point_E}, so that {point_P}{point_E} ⊥ {point_E}{point_B}. {point_M} is the midpoint of {point_P}{point_B}, {point_N} is a moving point on {point_B}{point_C}, satisfying V_{point_M}-{point_E}{point_B}{point_N}/V_{point_P}-{point_E}{point_B}{point_C}{point_D} = 1/6, find the sine value of the angle between line {point_E}{point_N} and plane {point_P}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"zht_7_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_P}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
