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
point_B, point_B1, point_E, point_A, point_A1, point_D1 = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(ratio_t):
    r"""
    计算正弦值 $\sin\theta = \frac{1}{\sqrt{\,{ratio_t}^{2}+2}}$。

    参数:
    ratio_t (float): 比例参数(需满足 $0 < ratio_t < 1$)

    返回:
    float: 计算得到的 $\sin\theta$ 值

    异常:
    ValueError: 若 ratio_t 不在 (0, 1) 范围内
    """
    # 校验参数范围
    if not (0 < ratio_t < 1):
        raise ValueError("ratio_t 必须满足 0 < ratio_t < 1")

    # 计算分母的平方根部分：√(ratio_t² + 2)
    denominator = math.sqrt(ratio_t ** 2 + 2)
    # 计算正弦值
    sin_theta = 1 / denominator
    return sin_theta

len_a = 1.0 #正方体的棱长，任意长度
ratio_t = 0.5

# result1 = calculate(ratio_t)
# print(f"当 ratio_t={ratio_t} 时，sinθ≈{result1:.4f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
ratio_t = round(random.uniform(0.2, 0.8), 1)

# Calculate the result
result = calculate(ratio_t)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_6_11_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"把正方体棱长统一设为 {len_a} (>0)，并令点 {point_E} 在棱 {point_B}{point_B1} 上按比例\n{point_B}{point_E} : {point_E}{point_B1} = {ratio_t} : (1 − {ratio_t})\n其中 0 < {ratio_t} < 1。当 {ratio_t} = 1/2 时即为原题的“中点”。\n求直线 {point_A}{point_A1} 与平面 {point_A}{point_D1}{point_E} 所成锐角 θ 的正弦值。",
    "en_problem": f"Let the cube have edge length {len_a} (>0). On edge {point_B}{point_B1}, choose point {point_E} so that\n{point_B}{point_E} : {point_E}{point_B1} = {ratio_t} : (1 − {ratio_t}),\nwith 0 < {ratio_t} < 1 (when {ratio_t}=1/2, E is the midpoint as in the original problem). Find sin θ, where θ is the acute angle between line {point_A}{point_A1} and plane {point_A}{point_D1}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_6_11_2({mode}, {azimuth}, {elevation}, '{point_B}', '{point_B1}', '{point_E}', '{point_A}', '{point_A1}', '{point_D1}')"}, ensure_ascii=False) + "\n")
