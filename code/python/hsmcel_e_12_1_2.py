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
point_S, point_A, point_B, point_P, point_Q, point_O, point_E, point_F = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_l):
    """
    计算三棱锥S-O-E-F体积的最大值

    参数:
    len_l (float): 圆锥母线长

    返回:
    float: 三棱锥体积的最大值
    """
    # 推导得到三棱锥体积公式 V = len_l / 12 * O_F * E_F
    # 在Rt△O-E-F中，O_F ** 2 + E_F ** 2 = O_E ** 2 = (len_l / 2) ** 2
    # 根据均值不等式 O_F * E_F <= (O_F ** 2 + E_F ** 2) / 2 = len_l ** 2 / 8
    # 体积 V = len_l / 12 * O_F * E_F <= len_l / 12 * len_l ** 2 / 8 = len_l ** 3 / 96
    return len_l ** 3 / 96


len_l = 2.0  # 可修改母线长进行计算
# result = calculate(len_l)
# print(f"三棱锥体积的最大值为: {result:.6f}")
# Generate random lengths
len_l = round(len_scaling_factor * float(len_l), 2)

# Calculate the result
result = calculate(len_l)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_12_1_2",
    "type": 7,
    "level": 3,
    "cn_problem": f"设圆锥的轴截面{point_S}{point_A}{point_B}为等腰直角三角形，母线长为{len_l}，{point_P}、{point_Q}分别是底面圆周上和圆内的动点，{point_O}为底面圆的圆心，且{point_O}{point_Q} ⊥ {point_P}{point_Q}。{point_E}是母线{point_S}{point_P}的中点，{point_F}是{point_O}点在{point_S}{point_Q}上的射影。求三棱锥{point_S}-{point_O}{point_E}{point_F}体积的最大值。",
    "en_problem": f"Let the axial cross-section {point_S}{point_A}{point_B} of a cone be an isosceles right triangle, with slant height {len_l}. {point_P} and {point_Q} are moving points on the circumference and inside the base circle respectively. {point_O} is the center of the base circle, and {point_O}{point_Q} ⊥ {point_P}{point_Q}. {point_E} is the midpoint of the slant height {point_S}{point_P}, and {point_F} is the projection of point {point_O} onto {point_S}{point_Q}. Find the maximum volume of the triangular pyramid {point_S}-{point_O}{point_E}{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_12_1_2({mode}, {azimuth}, {elevation}, '{point_S}', '{point_A}', '{point_B}', '{point_P}', '{point_Q}', '{point_O}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
