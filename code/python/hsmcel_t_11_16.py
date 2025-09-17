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
import math

def calculate(len_m):
    """
    计算折成正三棱锥后的体积

    参数:
    len_m (float): 正方形边长

    返回:
    float: 正三棱锥体积
    """
    return ((2 - math.sqrt(3)) * math.sqrt(1 + math.sqrt(3)) / 12) * len_m**3


# 题干给定的数值
len_m = 1.0  # 正方形边长

# 验证输出
# volume = calculate(len_m)
# print(f"正三棱锥体积: {volume:.6f}")

# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)

# Calculate the result
result = calculate(len_m)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_11_16",
    "type": 8,
    "level": 2,
    "cn_problem": f"把边长为{len_m}的正方形剪去图中的阴影部分，然后沿图中的线折成一个正三棱锥，求这个正三棱锥的体积。",
    "en_problem": f"Cut out the shaded part from a square with side length {len_m}, then fold along the lines in the figure to form a regular triangular pyramid. Find the volume of this regular triangular pyramid.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_11_16({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
