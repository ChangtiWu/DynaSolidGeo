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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_O, point_BC, point_M, point_P = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math

def calculate(len_L):
    """
    计算三棱柱的侧面积

    参数:
    len_L (float): 点 P 的轨迹长度

    返回:
    float: 三棱柱的侧面积
    """
    # 根据题解公式 area_side = 2 * len_L^2 * (2√2 + √15)
    return 2 * (len_L ** 2) * (2 * math.sqrt(2) + math.sqrt(15))


# 定义题干中的参数
len_L = math.sqrt(2)  # 点 P 的轨迹长度

# 验证计算结果
# result = calculate(len_L)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_L = round(len_scaling_factor * float(len_L), 2)

# Calculate the result
result = calculate(len_L)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_4_2",
    "type": 4,
    "level": 2,
    "cn_problem": f"在三棱柱 {point_A}{point_B}{point_C} - {point_A1}{point_B1}{point_C1} 中，{point_A}{point_B} ⊥ {point_A}{point_C}，设 len_AB = len_AC = len_t，len_AA1 = 2*len_t，点 {point_A1} 在底面 {point_A}{point_B}{point_C} 的射影为 {point_BC} 中点 {point_O}，{point_M} 为 {point_B1}{point_C1} 的中点。设点 {point_P} 为底面 {point_A}{point_B}{point_C} 内（包括边界）的动点，且 {point_B1}{point_P} // 平面 {point_A1}{point_M}{point_C}，若点 {point_P} 的轨迹长度为 {len_L}，求三棱柱的侧面积。",
    "en_problem": f"In the prism {point_A}{point_B}{point_C} - {point_A1}{point_B1}{point_C1}, {point_A}{point_B} ⊥ {point_A}{point_C}, let len_AB = len_AC = len_t, len_AA1 = 2*len_t, the projection of {point_A1} onto the base {point_A}{point_B}{point_C} is the midpoint {point_O} of {point_BC}, and {point_M} is the midpoint of {point_B1}{point_C1}. Let {point_P} be a point moving inside the base {point_A}{point_B}{point_C} (including the boundary), and {point_B1}{point_P} ∥ plane {point_A1}{point_M}{point_C}. If the trajectory length of {point_P} is {len_L}, find the lateral surface area of the prism.",
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
    f.write(json.dumps({json_data["id"]: f"area2_4_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_O}', '{point_BC}', '{point_M}', '{point_P}')"}, ensure_ascii=False) + "\n")
