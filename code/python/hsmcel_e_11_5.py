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
len_scaling_factor = round(random.uniform(1, 5.0), 1)

# Generate random point names
point_A, point_C, point_B, point_P = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math

def calculate(len_a, len_b, len_c):
    """
    计算二面角 P-AC-B 的大小（弧度制）

    参数:
    len_a (float): 直角边 BC
    len_b (float): 直角边 AC
    len_c (float): 折叠后斜边 AB 的长度

    返回:
    float: 二面角（弧度）
    """
    # 代入公式
    numerator = len_a**2 + len_b**2 - len_c**2
    frac = numerator / (len_a * len_b)

    sin_alpha = math.sqrt(
        2 * (1 - math.sqrt(1 - frac**2))
    ) / math.sqrt(4 - frac**2)

    # 返回角度（弧度制）
    return sin_alpha


# 题目给定的数据
len_a = 3.0       # BC
len_b = 2.0       # AC
len_c = math.sqrt(7)  # AB 折叠后长度

# 验证输出
#result = calculate(len_a, len_b, len_c)
#print(f"二面角大小: {result:.6f} ")


# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_11_5",
    "type": 8,
    "level": 3,
    "cn_problem": f"在Rt△{point_A}{point_C}{point_B}中，直角边{point_A}{point_C}={len_b}，{point_B}{point_C}={len_a}，{point_P}为斜边{point_A}{point_B}上一点。沿{point_C}{point_P}将此直角三角形折成直二面角{point_P}-{point_A}{point_C}-{point_B}，折叠后{point_A}{point_B}={len_c}，求二面角{point_P}-{point_A}{point_C}-{point_B}的大小。",
    "en_problem": f"In right triangle {point_A}{point_C}{point_B} with legs {point_A}{point_C}={len_b} and {point_B}{point_C}={len_a}, point {point_P} is on hypotenuse {point_A}{point_B}. Fold the right triangle along {point_C}{point_P} to form a right dihedral angle {point_P}-{point_A}{point_C}-{point_B}. After folding, {point_A}{point_B}={len_c}. Find the measure of dihedral angle {point_P}-{point_A}{point_C}-{point_B}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_11_5({mode}, {azimuth}, {elevation}, '{point_A}', '{point_C}', '{point_B}', '{point_P}')"}, ensure_ascii=False) + "\n")
