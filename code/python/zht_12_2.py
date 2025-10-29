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
point_A, point_B, point_C, point_D, point_E, point_A1, point_M = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算二面角 C-MB-E 的正弦值，当 λ = 1/2

    参数:
    len_a (float): BC 的长度的一半（保持 AC = 2*BC）

    返回:
    float: sin(二面角 C-MB-E)
    """
    return math.sqrt(390) / 20


# 题干给定的数值
len_a = 3.0  # BC/AC的一半比例用作参考

# 验证输出
# sin_value = calculate(len_a)
# print(f"sin(二面角 C-MB-E) = {sin_value:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "zht_12_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"在 Rt△{point_A}{point_B}{point_C} 中，∠{point_C} = 90°，设 {point_A}{point_C} = 2*{len_a}，{point_B}{point_C} = {len_a}（保持 {point_A}{point_C} = 2*{point_B}{point_C} 的比例）。{point_D}, {point_E} 分别在 {point_A}{point_C}, {point_A}{point_B} 上，{point_D}{point_E} ∥ {point_B}{point_C} 且经过△{point_A}{point_B}{point_C}的重心（重心分中线为2:1，故 {point_A}{point_D} = 2*{point_C}{point_D}，即 {point_C}{point_D} = {point_A}{point_C}/3 = 2*{len_a}/3，{point_D}{point_E} = 2/3·{point_B}{point_C} = 2*{len_a}/3）。将△{point_A}{point_D}{point_E}沿{point_D}{point_E}折起至△{point_A1}{point_D}{point_E}，使 {point_A1}{point_C} ⊥ {point_C}{point_D}。动点 {point_M} 满足 {point_A1}{point_M} = (1/2){point_A1}{point_D}（即 λ = 1/2），求二面角 {point_C}-{point_M}{point_B}-{point_E} 的正弦值。",
    "en_problem": f"In Rt△{point_A}{point_B}{point_C}, ∠{point_C} = 90°, let {point_A}{point_C} = 2*{len_a}, {point_B}{point_C} = {len_a} (maintaining the ratio {point_A}{point_C} = 2*{point_B}{point_C}). {point_D}, {point_E} are on {point_A}{point_C}, {point_A}{point_B} respectively, {point_D}{point_E} ∥ {point_B}{point_C} and passes through the centroid of △{point_A}{point_B}{point_C} (centroid divides median in ratio 2:1, so {point_A}{point_D} = 2*{point_C}{point_D}, i.e., {point_C}{point_D} = {point_A}{point_C}/3 = 2*{len_a}/3, {point_D}{point_E} = 2/3·{point_B}{point_C} = 2*{len_a}/3). Fold △{point_A}{point_D}{point_E} along {point_D}{point_E} to △{point_A1}{point_D}{point_E}, so that {point_A1}{point_C} ⊥ {point_C}{point_D}. Moving point {point_M} satisfies {point_A1}{point_M} = (1/2){point_A1}{point_D} (i.e., λ = 1/2), find the sine value of dihedral angle {point_C}-{point_M}{point_B}-{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"zht_12_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_A1}', '{point_M}')"}, ensure_ascii=False) + "\n")
