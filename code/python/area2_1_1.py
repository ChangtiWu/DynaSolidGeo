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


def calculate(len_a, len_b, len_l):
    """
    计算正四棱台的表面积

    参数:
    len_a (float): 上底边长
    len_b (float): 下底边长
    len_l (float): 侧棱长

    返回:
    float: 表面积
    """
    # 计算根号内的部分: len_l^2 - ((len_b - len_a)/2)^2
    inner_expr = len_l ** 2 - ((len_b - len_a) / 2) ** 2

    # 计算表面积: len_a^2 + len_b^2 + 2 * (len_a + len_b) * sqrt(inner_expr)
    surface_area = len_a ** 2 + len_b ** 2 + 2 * (len_a + len_b) * math.sqrt(inner_expr)

    return surface_area


# 定义题干中的变量
len_a = 2   # 上底边长
len_b = 4   # 下底边长
len_l = math.sqrt(3)  # 侧棱长

# 验证计算结果
#result = calculate(len_a, len_b, len_l)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_l = round(len_scaling_factor * float(len_l), 2)

# Calculate the result
result = calculate(len_a, len_b, len_l)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_1_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"已知正四棱台的上底面边长为 {len_a}，下底面边长为 {len_b}（{len_b} > {len_a} > 0），侧棱长为 {len_l}，求该正四棱台的表面积。",
    "en_problem": f"Given a regular square frustum with upper base side length {len_a}, lower base side length {len_b} (where {len_b} > {len_a} > 0), and lateral edge length {len_l}, find the surface area of the frustum.",
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
    f.write(json.dumps({json_data["id"]: f"area2_1_1({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
