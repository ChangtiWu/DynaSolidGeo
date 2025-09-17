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

# Add result calculation code
def calculate(len_a, len_b):
    """
    计算正四棱台的高

    参数:
    len_a (float): 上底面边长
    len_b (float): 下底面边长

    返回:
    float: 高
    """
    # 根据题目给出的解答公式 h = (len_a * len_b) / (len_a + len_b)
    return (len_a * len_b) / (len_a + len_b)


# 定义题干中的参数
len_a = 2.0   # 上底面边长
len_b = 4.0   # 下底面边长

# 验证计算结果
#result = calculate(len_a, len_b)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a, len_b)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_1_2",
    "type": 3,
    "level": 1,
    "cn_problem": f"正四棱台的上底面边长为 {len_a}，下底面边长为 {len_b}（{len_b} > {len_a} > 0），若棱台的侧面积等于两底面面积之和，求它的高。",
    "en_problem": f"A regular square frustum has upper base side length {len_a} and lower base side length {len_b} (where {len_b} > {len_a} > 0). If the lateral surface area equals the sum of the two base areas, find the height of the frustum.",
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
    f.write(json.dumps({json_data["id"]: f"area2_1_2({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
