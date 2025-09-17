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
point_P, point_C, point_D, point_A, point_B = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_s, len_t):
    r"""
    计算正弦值 $\sin\theta = \frac{\sqrt{3}}{2} \cdot \frac{\text{len}_s}{\text{len}_t}$（其中 $0 < \text{len}_s < \text{len}_t$）。

    参数:
    len_s (float): 分子参数（需满足 $0 < \text{len}_s < \text{len}_t$）
    len_t (float): 分母参数（需大于 $\text{len}_s$）

    返回:
    float: 计算得到的 $\sin\theta$ 值

    异常:
    ValueError: 若 $\text{len}_s \leq 0$ 或 $\text{len}_s \geq \text{len}_t$
    """
    # 校验参数条件
    if not (0 < len_s < len_t):
        raise ValueError("需满足 0 < len_s < len_t")

    # 计算常数项 √3/2
    constant = math.sqrt(3) / 2
    # 计算比例项 len_s / len_t
    ratio = len_s / len_t
    # 计算最终正弦值
    sin_theta = constant * ratio
    return sin_theta


len_s = 2.0
len_t = 3.0

# result1 = calculate(len_s, len_t)
# print(f"当 len_s={len_s}, len_t={len_t} 时，sinθ≈{result1:.4f}")  # 输出约 0.4330

# Generate random lengths
len_s = round(len_scaling_factor * float(len_s), 2)
len_t = round(len_scaling_factor * float(len_t), 2)

# Calculate the result
result = calculate(len_s, len_t)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_15_3",
    "type": 2,
    "level": 3,
    "cn_problem": f"设等边侧面 △{point_P}{point_C}{point_D} 边长 {len_s} (>0)，即 {point_P}{point_C} = {point_C}{point_D} = {point_D}{point_P} = {len_s}；\n- 保持 {point_P}{point_A}{point_C} ⟂ {point_P}{point_C}{point_D}，且 {point_P}{point_A} ⟂ {point_C}{point_D}；\n- 设 {point_A}{point_D} = {len_t} (>{len_s})；底面 {point_A}{point_B}{point_C}{point_D} 仍为平行四边形，保持原题所有平行 / 垂直关系。\n令 θ 为直线 {point_A}{point_D} 与平面 {point_P}{point_A}{point_C} 所成的锐角。求 sin θ。",
    "en_problem": f"The lateral face △{point_P}{point_C}{point_D} is equilateral with side length {len_s} (>0), so {point_P}{point_C} = {point_C}{point_D} = {point_D}{point_P} = {len_s};\n- Planes {point_P}{point_A}{point_C} and {point_P}{point_C}{point_D} are perpendicular, and {point_P}{point_A} ⟂ {point_C}{point_D};\n- Let {point_A}{point_D} = {len_t} (> {len_s}); the base {point_A}{point_B}{point_C}{point_D} remains a parallelogram with all original parallel and perpendicular relations.\nLet θ be the acute angle between line {point_A}{point_D} and plane {point_P}{point_A}{point_C}. Find sin θ .",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_15_3({mode}, {azimuth}, {elevation}, '{point_P}', '{point_C}', '{point_D}', '{point_A}', '{point_B}')"}, ensure_ascii=False) + "\n")
