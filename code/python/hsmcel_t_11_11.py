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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_P, point_Q = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算正方体 D1P + PQ 的最小值

    参数:
    len_a (float): 正方体棱长

    返回:
    float: 最小值
    """
    return len_a * (1 + math.sqrt(2) / 2)


# 题干给定的数值
len_a = 2.0  # 正方体棱长

# 验证输出
# min_distance = calculate(len_a)
# print(f"D1P + PQ 最小值: {min_distance:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_11_11",
    "type": 7,
    "level": 2,
    "cn_problem": f"设正方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}的棱长为{len_a}（{len_a} > 0），{point_P}是面对角线{point_B}{point_C1}上一动点，{point_Q}是底面{point_A}{point_B}{point_C}{point_D}上一动点，求{point_D1}{point_P} + {point_P}{point_Q}的最小值。",
    "en_problem": f"Let cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} have edge length {len_a} ({len_a} > 0), {point_P} is a moving point on face diagonal {point_B}{point_C1}, and {point_Q} is a moving point on base {point_A}{point_B}{point_C}{point_D}. Find the minimum value of {point_D1}{point_P} + {point_P}{point_Q}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_11_11({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_P}', '{point_Q}')"}, ensure_ascii=False) + "\n")
