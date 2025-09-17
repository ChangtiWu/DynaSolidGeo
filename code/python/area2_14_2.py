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
def calculate(len_R):
    """
    计算圆柱表面积与球表面积之比

    参数:
    len_R (float): 球的半径（圆柱底面半径等于球的半径，高等于球直径）

    返回:
    float: 圆柱表面积与球表面积之比
    """
    # 根据题解公式，表面积之比 = 3/2
    return 3 / 2


# 定义题干中的参数
len_R = 1.0  # 球的半径
# 验证计算结果
# result = calculate(len_R)
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_R = round(len_scaling_factor * float(len_R), 2)

# Calculate the result
result = calculate(len_R)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_14_2",
    "type": 4,
    "level": 1,
    "cn_problem": f"已知圆柱内有一个内切球，设球的半径为 {len_R}，且圆柱的底面半径等于球的半径 {len_R}，圆柱的高等于球的直径 2*{len_R}。求圆柱的表面积与球的表面积之比。",
    "en_problem": f"Given a cylinder with an inscribed sphere, let the sphere's radius be {len_R}, and the cylinder's base radius equals the sphere's radius {len_R}, while the cylinder's height equals the sphere's diameter 2*{len_R}. Find the ratio of the cylinder's surface area to the sphere's surface area.",
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
    f.write(json.dumps({json_data["id"]: f"area2_14_2({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
