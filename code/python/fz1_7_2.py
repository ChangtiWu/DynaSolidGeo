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
point_P, point_A, point_B, point_C, point_D, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_a, len_b):
    """
    计算点 D 到平面 PBC 的距离

    参数:
    len_a (float): 长度 AP
    len_b (float): 长度 AB

    返回:
    float: 距离
    """
    # 根据题干给出的解答公式: (3 * len_a * len_b) / sqrt(len_a^2 + 4 * len_b^2)
    return (3 * len_a * len_b) / math.sqrt(len_a ** 2 + 4 * len_b ** 2)


# 定义题干中的参数变量
len_a = 2.0  # AP
len_b = 1.0  # AB，因 CD = 3AB = 3，可得 AB = 1

# 验证计算结果（确认与参考答案一致后注释掉）
#result = calculate(len_a, len_b)
#print(f"计算结果: {result:.6f}")


# Generate random lengths
len_b = round(len_scaling_factor * float(len_b), 2)
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_7_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_B}∥{point_C}{point_D}，{point_A}{point_B}⊥{point_A}{point_D}，设{point_A}{point_B} = {len_b}，则{point_C}{point_D} = 3*{len_b}；设{point_A}{point_P} = {len_a}，则{point_A}{point_D} = 2*{len_a}（且{point_A}{point_P}⊥{point_D}{point_P}）。将△{point_P}{point_A}{point_D}沿{point_A}{point_D}折起后，{point_E}是棱{point_A}{point_D}上一点且{point_A}{point_D} = 4*{point_A}{point_E}，且{point_P}{point_E}⊥平面{point_A}{point_B}{point_C}{point_D}。求点{point_D}到平面{point_P}{point_B}{point_C}的距离。",
    "en_problem": f"In pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, {point_A}{point_B}∥{point_C}{point_D}, {point_A}{point_B}⊥{point_A}{point_D}, let {point_A}{point_B} = {len_b}, then {point_C}{point_D} = 3*{len_b}; let {point_A}{point_P} = {len_a}, then {point_A}{point_D} = 2*{len_a} (and {point_A}{point_P}⊥{point_D}{point_P}). After folding triangle {point_P}{point_A}{point_D} along {point_A}{point_D}, {point_E} is a point on edge {point_A}{point_D} with {point_A}{point_D} = 4*{point_A}{point_E}, and {point_P}{point_E}⊥plane {point_A}{point_B}{point_C}{point_D}. Find the distance from point {point_D} to plane {point_P}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_7_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
