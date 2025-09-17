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
point_P, point_A, point_O, point_B, point_A1 = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math

def calculate(len_r, area_S, arg_theta):
    """
    计算异面直线 A1B 与 AP 所成角的大小（用反三角函数表示）

    参数:
    len_r (float): 圆柱底面半径
    area_S (float): 圆柱表面积
    arg_theta (float): ∠AOP (弧度制)

    返回:
    float: 所成角的大小 (弧度)
    """
    # 圆柱高 h = (侧面积) / (底面周长) = (area_S - 2πr^2) / (2πr)
    h = (area_S - 2 * math.pi * len_r**2) / (2 * math.pi * len_r)

    numerator = 2 * len_r * math.sin(arg_theta / 2)
    denominator = math.sqrt(4 * len_r**2 + h**2)

    return numerator / denominator


# ====== 验证题目给的数据 ======
len_r = 2.0
area_S = 20 * math.pi
arg_theta = 2 * math.pi / 3  # 120°


# Generate random lengths
len_r = round(len_scaling_factor * float(len_r), 2)
area_S = round(len_scaling_factor * float(area_S), 2)

# Calculate the result
result = calculate(len_r, area_S, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fp_11_2",
    "type": 2,
    "level": 1,
    "cn_problem": f"设圆柱底面半径为{len_r}，表面积为{area_S}，底面圆周上点{point_P}满足∠{point_A}{point_O}{point_P} = {arg_theta}（0 < {arg_theta} < π，{point_A}{point_B}为底面圆直径），求异面直线{point_A1}{point_B}与{point_A}{point_P}所成角的大小。",
    "en_problem": f"Let a cylinder have base radius {len_r}, surface area {area_S}, and point {point_P} on the base circle such that ∠{point_A}{point_O}{point_P} = {arg_theta} (where 0 < {arg_theta} < π and {point_A}{point_B} is a diameter of the base circle). Find the measure of the angle between skew lines {point_A1}{point_B} and {point_A}{point_P}.",
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
    f.write(json.dumps({json_data["id"]: f"fp_11_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_O}', '{point_B}', '{point_A1}')"}, ensure_ascii=False) + "\n")
