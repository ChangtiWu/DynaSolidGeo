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
point_A, point_B, point_C, point_D, point_E, point_A1 = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(arg_theta, arg_alpha):
    """
    计算直线 A'C 与平面 A'ED 所成角的正弦值

    参数:
    arg_theta (float): 平行四边形 DAB 角（弧度）
    arg_alpha (float): 二面角 A'-DE-C 的角度（弧度）

    返回:
    float: 正弦值
    """
    numerator = 2 * math.cos(arg_theta / 2) * math.sin(arg_alpha)
    denominator = math.sqrt(
        math.sin(arg_theta / 2)**2 + (math.cos(arg_theta / 2)**2) * (5 - 4 * math.cos(arg_alpha))
    )
    return numerator / denominator


# 题干给定的数值
len_a = 2 * math.sqrt(3) / 2  # AB = 4√3 -> len_a = AD = 2√3
arg_theta = math.pi / 3        # ∠DAB
arg_alpha = math.pi / 3        # 二面角 A'-DE-C

# 验证输出
#sin_angle = calculate(arg_theta, arg_alpha)
#print(f"正弦值: {sin_angle:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(arg_theta, arg_alpha)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "zht_20_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在平行四边形 {point_A}{point_B}{point_C}{point_D} 中，{point_A}{point_B} = 2*{point_A}{point_D} = 2*{len_a}（即 {point_A}{point_D} = {point_B}{point_C} = {len_a}，{point_A}{point_B} = 2*{len_a}），∠{point_D}{point_A}{point_B} = {arg_theta}，{point_E} 为 {point_A}{point_B} 的中点。将 △{point_A}{point_D}{point_E} 沿直线 {point_D}{point_E} 翻折为 △{point_A1}{point_D}{point_E}，二面角 {point_A1}-{point_D}{point_E}-{point_C} 的大小为 {arg_alpha}，求直线 {point_A1}{point_C} 与平面 {point_A1}{point_E}{point_D} 所成角的正弦值。",
    "en_problem": f"In parallelogram {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B} = 2*{point_A}{point_D} = 2*{len_a} (i.e., {point_A}{point_D} = {point_B}{point_C} = {len_a}, {point_A}{point_B} = 2*{len_a}), ∠{point_D}{point_A}{point_B} = {arg_theta}, {point_E} is the midpoint of {point_A}{point_B}. Fold △{point_A}{point_D}{point_E} along line {point_D}{point_E} to form △{point_A1}{point_D}{point_E}, the dihedral angle {point_A1}-{point_D}{point_E}-{point_C} has size {arg_alpha}, find the sine value of the angle between line {point_A1}{point_C} and plane {point_A1}{point_E}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"zht_20_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_A1}')"}, ensure_ascii=False) + "\n")
