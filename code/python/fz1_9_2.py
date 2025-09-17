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
point_A, point_B, point_C, point_D, point_E, point_F, point_P = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate():
    """
    计算二面角 P-EF-B 的平面角 θ

    返回:
    float: θ 的值（弧度）
    """
    # 根据题干给出的解答公式: π / 2
    return math.pi / 2


# 定义题干中的参数变量
len_a = 4.0        # AB = 4
len_lambda = 0.5   # λ 在 (0, 1)，这里赋值方便验证

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate()
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)


# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_9_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"设菱形{point_A}{point_B}{point_C}{point_D}的边长为{len_a}（{len_a} > 0），∠{point_A}{point_B}{point_C} = 120°，{point_A}{point_E} = {len_lambda}{point_A}{point_D}，{point_A}{point_F} = {len_lambda}{point_A}{point_B}（0 < {len_lambda} < 1）。沿{point_E}{point_F}将△{point_A}{point_E}{point_F}向上折起得到棱锥{point_P}-{point_B}{point_C}{point_D}{point_E}{point_F}，设二面角{point_P}-{point_E}{point_F}-{point_B}的平面角为 arg_theta 。若平面{point_P}{point_E}{point_F}与平面{point_P}{point_B}{point_F}所成锐二面角的余弦值为√5/5，求 arg_theta 的值。",
    "en_problem": f"Let rhombus {point_A}{point_B}{point_C}{point_D} have side length {len_a} ({len_a} > 0), ∠{point_A}{point_B}{point_C} = 120°, {point_A}{point_E} = {len_lambda}{point_A}{point_D}, {point_A}{point_F} = {len_lambda}{point_A}{point_B} (0 < {len_lambda} < 1). Fold triangle {point_A}{point_E}{point_F} upward along {point_E}{point_F} to form pyramid {point_P}-{point_B}{point_C}{point_D}{point_E}{point_F}, let the plane angle of dihedral angle {point_P}-{point_E}{point_F}-{point_B} be  arg_theta . If the cosine of the acute dihedral angle between plane {point_P}{point_E}{point_F} and plane {point_P}{point_B}{point_F} is √5/5, find the value of  arg_theta .",
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
    f.write(json.dumps({json_data["id"]: f"fz1_9_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_P}')"}, ensure_ascii=False) + "\n")
