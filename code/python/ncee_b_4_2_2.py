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
point_P, point_A, point_B, point_C, point_D, point_E, point_O, point_F = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a, len_b, len_c, ang_theta):
    """
    计算给定参数对应的体积V。

    参数:
        len_a (float): 长度参数（如某边长）。
        len_b (float): 长度参数（如另一边长）。
        len_c (float): 长度参数（如高度相关长度）。
        ang_theta (float): 角度参数（弧度制，影响余弦项）。

    返回:
        float: 计算得到的体积V。

    注意:
        输入角度需为弧度制；根号内表达式需非负（否则会抛出数学错误）。
    """
    # 计算第一个平方根项：√(len_c² - len_b²/4)
    sqrt_term1 = math.sqrt(len_c ** 2 - (len_b ** 2) / 4)

    # 计算分数项：(len_a²/len_b²) + (len_b²)/(4*len_a²)
    fraction = (len_a ** 2 / len_b ** 2) + (len_b ** 2) / (4 * len_a ** 2)

    # 计算余弦平方项：cos²(ang_theta)
    cos_sq = math.cos(ang_theta) ** 2

    # 计算第二个平方根项：√(1 - fraction * cos_sq)
    sqrt_term2 = math.sqrt(1 - fraction * cos_sq)

    # 计算最终体积V
    V = (len_a * len_b / 6) * sqrt_term1 * sqrt_term2

    return V


len_a = 2
len_b = 2 * math.sqrt(2)
len_c = math.sqrt(6)
ang_theta = math.pi / 3 * 2

# V = calculate(len_a, len_b, len_c, ang_theta)
# print(f"体积 V = {V:.4f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)


# Calculate the result
result = calculate(len_a, len_b, len_c, ang_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_2_2",
    "type": 5,
    "level": 3,
    "cn_problem": f"在三棱锥 {point_P}-{point_A}{point_B}{point_C} 中，{point_A}{point_B} ⊥ {point_B}{point_C}，{point_A}{point_B} = {len_a}，{point_B}{point_C} = {len_b}，{point_P}{point_B} = {point_P}{point_C} = {len_c}（其中 {len_a},{len_b},{len_c} > 0，且 {len_c} > \\tfrac{{{len_b}}}{{2}}）。设 {point_D},{point_E},{point_O} 分别是 {point_B}{point_P},{point_A}{point_P},{point_B}{point_C} 的中点，点 {point_F} 在棱 {point_A}{point_C} 上，且 {point_B}{point_F} ⊥ {point_A}{point_O}，已知 ∠{point_P}{point_O}{point_F} = {ang_theta}。求三棱锥 {point_P}-{point_A}{point_B}{point_C} 的体积。",
    "en_problem": f"In the triangular pyramid {point_P}-{point_A}{point_B}{point_C}, {point_A}{point_B} ⊥ {point_B}{point_C} with {point_A}{point_B} = {len_a}, {point_B}{point_C} = {len_b}, and {point_P}{point_B} = {point_P}{point_C} = {len_c} (where {len_a},{len_b},{len_c} > 0 and {len_c} > \\tfrac{{{len_b}}}{{2}}). Let {point_D},{point_E},{point_O} be the midpoints of {point_B}{point_P},{point_A}{point_P},{point_B}{point_C} respectively. Point {point_F} lies on edge {point_A}{point_C} such that {point_B}{point_F} ⊥ {point_A}{point_O}. Given ∠{point_P}{point_O}{point_F} = {ang_theta}, find the volume of the triangular pyramid {point_P}-{point_A}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_2_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_O}', '{point_F}')"}, ensure_ascii=False) + "\n")
