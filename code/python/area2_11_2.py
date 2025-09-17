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
def calculate(len_R, len_H, len_x):
    """
    计算内接圆柱的高

    参数:
    len_R (float): 圆锥底面半径
    len_H (float): 圆锥高
    len_x (float): 圆柱底面半径

    返回:
    float: 圆柱高
    """
    # 根据题解公式 h = H * (1 - x/R)
    return len_H * (1 - len_x / len_R)


# 定义题干中的参数
len_R = 1.0   # 圆锥底面半径
len_H = 3.0   # 圆锥高
len_x = 0.5   # 圆柱底面半径（举例赋值，可按需要改变）

# 验证计算结果
#result = calculate(len_R, len_H, len_x)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_R = round(len_scaling_factor * float(len_R), 2)
len_H = round(len_scaling_factor * float(len_H), 2)
len_x = round(len_scaling_factor * float(len_x), 2)

# Calculate the result
result = calculate(len_R, len_H, len_x)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_11_2",
    "type": 3,
    "level": 1,
    "cn_problem": f"已知一个圆锥的底面半径为 {len_R}，高为 {len_H}，在圆锥中有一个底面半径为 {len_x} 的内接圆柱，求圆柱的高。",
    "en_problem": f"Given a cone with base radius {len_R} and height {len_H}, and an inscribed cylinder with base radius {len_x}, express the height of the cylinder.",
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
    f.write(json.dumps({json_data["id"]: f"area2_11_2({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
