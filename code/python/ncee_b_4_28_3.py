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
point_P, point_O, point_A, point_B, point_C, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_R):
    """
    计算集合 PB 中元素 E 使得 CE + OE 最小的最小值，公式为：
    min_{E∈PB} (CE + OE) = (√2 + √6)/2 * len_R

    参数:
    len_R (float): 长度参数（需为正数，代表实际长度）

    返回:
    float: CE + OE 的最小值
    """
    # 计算常数系数：(√2 + √6)/2
    constant = (math.sqrt(2) + math.sqrt(6)) / 2
    # 计算最小值
    min_value = constant * len_R
    return min_value

len_R = 1.0
# result1 = calculate(len_R)
# print(f"当 len_R={len_R} 时，min(CE+OE)={result1:.4f}")
# Generate random lengths
len_R = round(len_scaling_factor * float(len_R), 2)

# Calculate the result
result = calculate(len_R)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_28_3",
    "type": 3,
    "level": 2,
    "cn_problem": f"设圆锥 {point_P}-⟨⟳{point_O}⟩ 满足：\n- 圆 {point_O} 的半径为 {len_R} ({len_R}>0)，{point_A}{point_B} 为直径；\n- 顶点 {point_P} 在圆心 {point_O} 的垂线上，且 {point_P}{point_O} = {point_O}{point_B} = {len_R}；\n- 圆周上取点 {point_C} 使 ∠{point_B}{point_O}{point_C} = 90°（等价于 {point_B}{point_C} = √2·{len_R}）；\n- 点 {point_E} 在线段 {point_P}{point_B} 上。\n求和 {point_C}{point_E} + {point_O}{point_E} 的最小值。",
    "en_problem": f"In the right circular cone {point_P}-⟨⟳{point_O}⟩:\n- The base circle {point_O} has radius {len_R} ({len_R}>0) with diameter {point_A}{point_B};\n- The apex {point_P} lies on the line through the center {point_O} perpendicular to the plane of the circle, with {point_P}{point_O} = {point_O}{point_B} = {len_R};\n- A point {point_C} is chosen on the circle such that ∠{point_B}{point_O}{point_C} = 90° (equivalently {point_B}{point_C} = √2·{len_R});\n- Point {point_E} is on segment {point_P}{point_B}.\nFind the minimum value of {point_C}{point_E} + {point_O}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_28_3({mode}, {azimuth}, {elevation}, '{point_P}', '{point_O}', '{point_A}', '{point_B}', '{point_C}', '{point_E}')"}, ensure_ascii=False) + "\n")
