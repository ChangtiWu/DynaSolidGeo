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
point_V, point_A, point_B, point_C, point_E, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_slant, arg_alpha):
    """
    计算 △AEF 周长的最小值

    参数:
    len_slant (float): 侧棱长
    arg_alpha (float): 面角 (弧度)

    返回:
    float: 周长最小值
    """
    # 公式1: l * sqrt(2 * (1 - cos(3α)))
    result1 = len_slant * math.sqrt(2 * (1 - math.cos(3 * arg_alpha)))
    # 公式2: 2l * sin(3α/2)
    result2 = 2 * len_slant * math.sin(3 * arg_alpha / 2)
    # 两个结果应当相等
    return result1


# 题干给定的数值
len_slant = 4.0
arg_alpha = math.radians(30)

# 验证输出
#res1, res2 = calculate(len_slant, arg_alpha)
#print(f"公式1结果: {res1:.6f}")
#print(f"公式2结果: {res2:.6f}")


# Generate random lengths

len_slant = round(len_scaling_factor * float(len_slant), 2)

# Calculate the result
result = calculate(len_slant, arg_alpha)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fp_13_1",
    "type": 3,
    "level": 1,
    "cn_problem": f"在三棱锥 {point_V}-{point_A}{point_B}{point_C} 中，侧棱  len_VA  =  len_VB  =  len_VC  = {len_slant}，三个面角满足 ∠{point_A}{point_V}{point_B} = ∠{point_B}{point_V}{point_C} = ∠{point_A}{point_V}{point_C} = {arg_alpha}。过点 {point_A} 作截面 {point_A}{point_E}{point_F}（其中 {point_E} ∈ {point_V}{point_B}，{point_F} ∈ {point_V}{point_C}），求 △{point_A}{point_E}{point_F} 周长的最小值。",
    "en_problem": f"In triangular pyramid {point_V}-{point_A}{point_B}{point_C}, the lateral edges  len_VA  =  len_VB  =  len_VC  = {len_slant}, and the three face angles satisfy ∠{point_A}{point_V}{point_B} = ∠{point_B}{point_V}{point_C} = ∠{point_A}{point_V}{point_C} = {arg_alpha}. Through point {point_A}, construct a section {point_A}{point_E}{point_F} (where {point_E} ∈ {point_V}{point_B}, {point_F} ∈ {point_V}{point_C}). Find the minimum perimeter of △{point_A}{point_E}{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"fp_13_1({mode}, {azimuth}, {elevation}, '{point_V}', '{point_A}', '{point_B}', '{point_C}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
