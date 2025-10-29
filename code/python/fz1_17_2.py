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

def calculate(len_k):
    """
    计算二面角 P-CE-F 的正切值

    参数:
    len_k (float): 题干中的比值 k（BE = k * AE）

    返回:
    float: 二面角正切值
    """
    # 根据题干给出的解答公式: sqrt(k^2 + 1)
    return math.sqrt(len_k ** 2 + 1)


# 定义题干中的参数变量
len_a = 2.0
len_k = 2.0  # BE = 2 * AE

# 验证计算结果（确认与参考答案一致后注释掉）
# result = calculate(len_k)
# print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_17_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在△{point_A}{point_B}{point_C}中，{point_A}{point_C}⊥{point_B}{point_C}，{point_A}{point_C} = {point_B}{point_C} = {len_a}（{len_a} > 0），{point_D}是{point_A}{point_C}的中点，{point_E}，{point_F}分别是{point_B}{point_A}，{point_B}{point_C}边上的动点，且{point_E}{point_F}∥{point_A}{point_C}，满足{point_B}{point_E} = {len_k}{point_A}{point_E}（{len_k} > 0）。将△{point_B}{point_E}{point_F}沿{point_E}{point_F}折起，使点{point_B}折至点{point_P}的位置，且二面角{point_P}-{point_E}{point_F}-{point_C}为直二面角，求二面角{point_P}-{point_C}{point_E}-{point_F}的正切值。",
    "en_problem": f"In triangle {point_A}{point_B}{point_C}, {point_A}{point_C}⊥{point_B}{point_C}, {point_A}{point_C} = {point_B}{point_C} = {len_a} ({len_a} > 0), {point_D} is the midpoint of {point_A}{point_C}, {point_E}, {point_F} are moving points on sides {point_B}{point_A}, {point_B}{point_C} respectively, and {point_E}{point_F}∥{point_A}{point_C}, satisfying {point_B}{point_E} = {len_k}{point_A}{point_E} ({len_k} > 0). Fold triangle {point_B}{point_E}{point_F} along {point_E}{point_F} so that point {point_B} moves to position {point_P}, and the dihedral angle {point_P}-{point_E}{point_F}-{point_C} is a right dihedral angle, find the tangent of dihedral angle {point_P}-{point_C}{point_E}-{point_F}.",
    "solution": f"{result}",
    "image": f"images/{os.path.splitext(os.path.basename(__file__))[0]}.png"
}

# video mode
if args.mode == 1:
    json_data["image"] = f"videos/{os.path.splitext(os.path.basename(__file__))[0]}.mp4"



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
    f.write(json.dumps({json_data["id"]: f"fz1_17_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_P}')"}, ensure_ascii=False) + "\n")
