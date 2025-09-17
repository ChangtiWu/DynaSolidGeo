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
def calculate(len_k):
    """
    计算圆柱体积与球体积之比

    参数:
    len_k (float): 圆柱底面半径与球半径的比例常数

    返回:
    float: 圆柱体积与球体积之比
    """
    # 根据题目给出的公式 V_cylinder / V_sphere = 3 * len_k^2 / 2
    return 3 * (len_k ** 2) / 2


# 定义题干中的参数
len_k = 1.0  # 示例比例，可根据题意修改
len_R = 1.0
len_h = 2.0
len_r = 1.0
# 验证计算结果
#result = calculate(len_k)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_R = round(len_scaling_factor * float(len_R), 2)
len_h = 2*len_R
len_r = len_R

# Calculate the result
result = calculate(len_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_14_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"已知圆柱内有一个球，设球的半径为 {len_R}，圆柱的高为 {len_h}，底面半径为 {len_r}，满足球的直径等于圆柱的高（{len_h} = 2*{len_R}），且圆柱底面半径 {len_r} = {len_k}{len_R}（其中 {len_k} > 0 为常数）。求圆柱的体积与球的体积之比。",
    "en_problem": f"Given a cylinder containing a sphere, let the sphere's radius be {len_R}, the cylinder's height be {len_h}, and the base radius be {len_r}, such that the sphere's diameter equals the cylinder's height ({len_h} = 2*{len_R}), and the cylinder's base radius {len_r} = {len_k}{len_R} (where {len_k} > 0 is a constant). Find the ratio of the cylinder's volume to the sphere's volume.",
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
    f.write(json.dumps({json_data["id"]: f"area2_14_1({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
