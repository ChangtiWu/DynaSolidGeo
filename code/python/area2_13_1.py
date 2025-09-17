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

def calculate(len_R, len_l, len_h):
    """
    计算圆锥内接圆柱的表面积

    参数:
    len_R (float): 圆锥底面半径
    len_l (float): 圆锥母线长
    len_h (float): 圆柱高

    返回:
    float: 圆柱表面积
    """
    # 先计算圆锥高
    H = math.sqrt(len_l ** 2 - len_R ** 2)
    # 圆柱底面半径
    r = len_R * (1 - len_h / H)
    # 圆柱表面积
    return 2 * math.pi * r * (r + len_h)


# 定义题干参数
len_R = 2.0   # 圆锥底面半径
len_l = 4.0   # 圆锥母线长
len_h = math.sqrt(3)   # 圆柱高

# 验证计算结果
#result = calculate(len_R, len_l, len_h)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_R = round(len_scaling_factor * float(len_R), 2)
len_l = round(len_scaling_factor * float(len_l), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_R, len_l, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_13_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"在底面半径为 {len_R}，母线长为 {len_l} 的圆锥中，内接一个高为 {len_h} 的圆柱，求该圆柱的表面积。",
    "en_problem": f"In a cone with base radius {len_R} and slant height {len_l}, there is an inscribed cylinder with height {len_h}. Find the surface area of this cylinder.",
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
    f.write(json.dumps({json_data["id"]: f"area2_13_1({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
