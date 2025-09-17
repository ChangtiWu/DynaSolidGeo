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
point_P, point_A, point_B, point_C, point_O, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_a, len_h, arg_alpha):
    """
    计算二面角正弦值

    参数:
    len_a (float): PA = PB 的长度
    len_h (float): PO 的长度
    arg_alpha (float): ∠ABO = ∠CBO 的角度（弧度制）

    返回:
    float: 二面角的正弦值
    """
    sin_alpha = math.sin(arg_alpha)
    cos_alpha = math.cos(arg_alpha)

    numerator = len_h * math.sqrt(len_h ** 2 + (len_a ** 2 - len_h ** 2) * (sin_alpha ** 2 + 9 * cos_alpha ** 2))
    denominator = math.sqrt(len_h ** 2 + 9 * (len_a ** 2 - len_h ** 2) * cos_alpha ** 2) * math.sqrt(len_h ** 2 + (len_a ** 2 - len_h ** 2) * sin_alpha ** 2)

    result = numerator / denominator
    return result


# 定义题干参数
len_a = 5.0
len_h = 3.0
arg_alpha = math.radians(30)

# 验证输出（与参考答案对比）
# result = calculate(len_a, len_h, arg_alpha)
# print(f"二面角正弦值: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h, arg_alpha)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_15_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"在三棱锥{point_P}-{point_A}{point_B}{point_C}中，{point_P}{point_O}是底面{point_A}{point_B}{point_C}的高（{point_P}{point_O}⊥平面{point_A}{point_B}{point_C}），{point_P}{point_A}={point_P}{point_B}={len_a}，∠{point_A}{point_B}{point_O}=∠{point_C}{point_B}{point_O}={arg_alpha}（{point_O}为{point_P}{point_O}在底面的垂足），{point_P}{point_O}={len_h}，且{point_A}{point_B}⊥{point_A}{point_C}。{point_E}为{point_P}{point_B}的中点，求二面角{point_C}-{point_A}{point_E}-{point_B}的正弦值。",
    "en_problem": f"In triangular pyramid {point_P}-{point_A}{point_B}{point_C}, {point_P}{point_O} is the height to base {point_A}{point_B}{point_C} ({point_P}{point_O}⊥plane {point_A}{point_B}{point_C}), {point_P}{point_A}={point_P}{point_B}={len_a}, ∠{point_A}{point_B}{point_O}=∠{point_C}{point_B}{point_O}={arg_alpha} (where {point_O} is the foot of {point_P}{point_O} on the base), {point_P}{point_O}={len_h}, and {point_A}{point_B}⊥{point_A}{point_C}. {point_E} is the midpoint of {point_P}{point_B}. Find the sine of dihedral angle {point_C}-{point_A}{point_E}-{point_B}.",
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
    f.write(json.dumps({json_data["id"]: f"sup_15_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_O}', '{point_E}')"}, ensure_ascii=False) + "\n")
