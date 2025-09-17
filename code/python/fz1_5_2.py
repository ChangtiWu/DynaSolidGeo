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
point_A, point_B, point_C, point_D, point_E, point_A1, point_P = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_side):
    """
    计算二面角 P-BD-A1 的余弦值

    参数:
    len_side (float): 菱形的边长

    返回:
    float: 二面角的余弦值
    """
    # 根据题干给出的解答公式: 1/7
    return 1 / 7


# 定义题干中的参数变量
len_side = 2.0  # AB = AD = 2

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_side)
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_side = round(len_scaling_factor * float(len_side), 2)

# Calculate the result
result = calculate(len_side)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_5_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在菱形{point_A}{point_B}{point_C}{point_D}中，∠{point_A} = 60°，{point_A}{point_B} = {point_A}{point_D} = {len_side}，{point_E}为{point_A}{point_D}的中点。将△{point_A}{point_B}{point_E}沿{point_B}{point_E}折起到△{point_A1}{point_B}{point_E}的位置，使得{point_A1}{point_D} = {len_side}√2/2。若{point_P}为线段{point_A1}{point_C}的中点，求二面角{point_P}-{point_B}{point_D}-{point_A1}的余弦值。",
    "en_problem": f"In rhombus {point_A}{point_B}{point_C}{point_D}, ∠{point_A} = 60°, {point_A}{point_B} = {point_A}{point_D} = {len_side}, and {point_E} is the midpoint of {point_A}{point_D}. Triangle {point_A}{point_B}{point_E} is folded along {point_B}{point_E} to position △{point_A1}{point_B}{point_E}, such that {point_A1}{point_D} = {len_side}√2/2. If {point_P} is the midpoint of segment {point_A1}{point_C}, find the cosine of dihedral angle {point_P}-{point_B}{point_D}-{point_A1}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_5_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_A1}', '{point_P}')"}, ensure_ascii=False) + "\n")
