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
point_P, point_A, point_B, point_C, point_E, point_O = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_r, len_h):
    """
    计算反余弦表达式的值，公式为：
    arccos( (√2 * len_r) / (2 * √(len_r² + len_h²)) )
    
    参数:
        len_r (float/int): 长度参数 r（需为非负实数）
        len_h (float/int): 长度参数 h（需为非负实数）
    
    返回:
        float: 反余弦计算结果（单位：弧度）
    
    异常:
        ValueError: 若分母为零（len_r 和 len_h 同时为零）或分数值超出 [-1, 1] 范围
    """
    # 计算分子：√2 * len_r
    numerator = math.sqrt(2) * len_r
    # 计算分母：2 * √(len_r² + len_h²)
    denominator = 2 * math.sqrt(len_r**2 + len_h**2)
    
    # 检查分母是否为零（避免除以零错误）
    if denominator == 0:
        raise ValueError("分母不能为零，len_r 和 len_h 不能同时为零。")
    
    # 计算分数值（需确保在 [-1, 1] 范围内，否则 acos 会抛出 ValueError）
    fraction = numerator / denominator
    
    # 计算反余弦并返回结果
    return math.acos(fraction)

len_r = 1
len_h = 2

# print(calculate(len_r, len_h))
# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)
len_r = round(len_scaling_factor * float(len_r), 2)

# Calculate the result
result = calculate(len_r, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_5_6_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"如图，圆锥的顶点为{point_P}，底面的一条直径为{point_A}{point_B}，{point_C}为半圆弧{point_A}{point_B}的中点，{point_E}为劣弧{point_C}{point_B}的中点。已知圆锥的高{point_P}{point_O} = {len_h}，底面半径{point_O}{point_A} = {len_r}，求异面直线{point_P}{point_A}与{point_O}{point_E}所成角的大小。",
    "en_problem": f"As shown in the figure, the vertex of the cone is {point_P}, a diameter of the base is {point_A}{point_B}, {point_C} is the midpoint of the semicircle arc {point_A}{point_B}, {point_E} is the midpoint of the minor arc {point_C}{point_B}. Given the height of the cone {point_P}{point_O} = {len_h}, the base radius {point_O}{point_A} = {len_r}, find the size of the angle between the skew lines {point_P}{point_A} and {point_O}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_5_6_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_E}', '{point_O}')"}, ensure_ascii=False) + "\n")
