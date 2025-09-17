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
len_scaling_factor = round(random.uniform(0.1, 10.0), 1)

# Generate random point names
point_B, point_C, point_D, point_E, point_A, point_F, point_A1 = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_a, len_b, volume_v):
    """
    计算四棱锥 A₁-BCDE 的表面积

    参数:
    len_a (float): BC
    len_b (float): AC
    volume_v (float): 四棱锥体积

    返回:
    float: 四棱锥表面积
    """
    # 根据题解公式 S = 3*len_a*len_b/4 + 2*volume_v/len_a + (√3 * len_b * √(4*len_a^2 + len_b^2))/16
    return (3 * len_a * len_b) / 4 + (2 * volume_v) / len_a + (math.sqrt(3) * len_b * math.sqrt(4 * len_a ** 2 + len_b ** 2)) / 16


# 定义题干参数
len_a = 6.0      # BC
len_b = 8.0      # AC
volume_v = 12 * math.sqrt(3)  # 四棱锥体积

# 验证计算结果
#result = calculate(len_a, len_b, volume_v)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
volume_v = round((len_scaling_factor**3) * float(volume_v), 2)

# Calculate the result
result = calculate(len_a, len_b, volume_v)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_6_2",
    "type": 4,
    "level": 1,
    "cn_problem": f"在梯形 {point_B}{point_C}{point_D}{point_E} 中，{point_D}{point_E} ∥ {point_B}{point_C}，且 {point_D}{point_E} = (1/2){point_B}{point_C}，∠{point_C} = 90°，分别延长两腰交于点 {point_A}，点 {point_F} 为线段 {point_C}{point_D} 上的一点，将 △{point_A}{point_D}{point_E} 沿 {point_D}{point_E} 折起到 △{point_A1}{point_D}{point_E} 的位置，使 {point_A1}{point_F} ⊥ {point_C}{point_D}。设 {point_B}{point_C} = {len_a}，{point_A}{point_C} = {len_b}，四棱锥 {point_A1} - {point_B}{point_C}{point_D}{point_E} 的体积为 {volume_v}，求四棱锥 {point_A1} - {point_B}{point_C}{point_D}{point_E} 的表面积。",
    "en_problem": f"In trapezoid {point_B}{point_C}{point_D}{point_E}, {point_D}{point_E} ∥ {point_B}{point_C} and {point_D}{point_E} = (1/2){point_B}{point_C}, ∠{point_C} = 90°. Extend the two legs to meet at point {point_A}, and let {point_F} be a point on segment {point_C}{point_D}. Fold △{point_A}{point_D}{point_E} along {point_D}{point_E} to position △{point_A1}{point_D}{point_E} such that {point_A1}{point_F} ⊥ {point_C}{point_D}. Given {point_B}{point_C} = {len_a}, {point_A}{point_C} = {len_b}, and the volume of pyramid {point_A1} - {point_B}{point_C}{point_D}{point_E} is {volume_v}, find the surface area of pyramid {point_A1} - {point_B}{point_C}{point_D}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"area2_6_2({mode}, {azimuth}, {elevation}, '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_A}', '{point_F}', '{point_A1}')"}, ensure_ascii=False) + "\n")
