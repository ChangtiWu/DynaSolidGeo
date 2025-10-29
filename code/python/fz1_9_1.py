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
    计算 λ 的值

    参数:
    len_k (float): 体积比 P-BCD : P-BDEF

    返回:
    float: λ 的值
    """
    # 根据题干给出的解答公式: sqrt(len_k * (len_k - 1)) / len_k
    return math.sqrt(len_k * (len_k - 1)) / len_k


# 定义题干中的参数变量
len_a = 4.0        # AB = AD = 4
arg_theta = 120.0  # ∠ABC = 120°
len_k = 9.0 / 5.0  # 体积比 = 9/5

# 验证计算结果（确认与参考答案一致后注释掉）
#result = calculate(len_k)
#print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_k = round(len_scaling_factor * float(len_k), 2)

# Calculate the result
result = calculate(len_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_9_1",
    "type": 8,
    "level": 2,
    "cn_problem": f"在菱形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_B} = {point_A}{point_D} = {len_a}，∠{point_A}{point_B}{point_C} = {arg_theta}°，{point_A}{point_E} =  len_lambda {point_A}{point_D}，{point_A}{point_F} =  len_lambda {point_A}{point_B}（0 <  len_lambda  < 1）。沿{point_E}{point_F}将△{point_A}{point_E}{point_F}向上折起得到棱锥{point_P}-{point_B}{point_C}{point_D}{point_E}{point_F}。若三棱锥{point_P}-{point_B}{point_C}{point_D}和四棱锥{point_P}-{point_B}{point_D}{point_E}{point_F}的体积之比为{len_k}，求 len_lambda 的值（0 <  len_lambda  < 1）。",
    "en_problem": f"In rhombus {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B} = {point_A}{point_D} = {len_a}, ∠{point_A}{point_B}{point_C} = {arg_theta}°, {point_A}{point_E} =  len_lambda {point_A}{point_D}, {point_A}{point_F} =  len_lambda {point_A}{point_B} (0 <  len_lambda  < 1). Fold triangle {point_A}{point_E}{point_F} upward along {point_E}{point_F} to form pyramid {point_P}-{point_B}{point_C}{point_D}{point_E}{point_F}. If the volume ratio of triangular pyramid {point_P}-{point_B}{point_C}{point_D} to quadrilateral pyramid {point_P}-{point_B}{point_D}{point_E}{point_F} is {len_k}, find the value of  len_lambda  (0 <  len_lambda  < 1).",
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
    f.write(json.dumps({json_data["id"]: f"fz1_9_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_P}')"}, ensure_ascii=False) + "\n")
