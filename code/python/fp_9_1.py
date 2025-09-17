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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_P, point_M, point_N = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math

def calculate(len_edge, len_divisions):
    """
    计算△PMN的最小周长

    参数:
    len_edge (float): 正方体的棱长
    len_divisions (int): 等分份数 (点P在BC1上的等分位置)

    返回:
    float: △PMN的最小周长
    """
    # 公式: perimeter_min = ((n - 1) / n) * a * (sqrt(3) + 1)
    return ((len_divisions - 1) / len_divisions) * len_edge * (math.sqrt(3) + 1)


# 题干给定的数值
len_edge = 4.0
len_divisions = 4

# 验证输出
#result = calculate(len_edge, len_divisions)
#print(f"计算结果: {result:.6f}")


# Generate random lengths
len_edge = round(len_scaling_factor * float(len_edge), 2)

# Calculate the result
result = calculate(len_edge, len_divisions)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fp_9_1",
    "type": 3,
    "level": 1,
    "cn_problem": f"在棱长为 {len_edge} 的正方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 中，点 {point_P} 是 {point_B}{point_C1} 上靠近 {point_C1} 的 {len_divisions} 等分点（{len_divisions} ∈ ℕ*, {len_divisions} ≥ 2），点 {point_M}、{point_N} 分别在 {point_B}{point_C}、{point_B}{point_D} 上，求 △{point_P}{point_M}{point_N} 周长的最小值。",
    "en_problem": f"In a cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} with edge length {len_edge}, point {point_P} is the {len_divisions}-division point on {point_B}{point_C1} closer to {point_C1} ({len_divisions} ∈ ℕ*, {len_divisions} ≥ 2), and points {point_M}, {point_N} are respectively on {point_B}{point_C}, {point_B}{point_D}. Find the minimum perimeter of △{point_P}{point_M}{point_N}.",
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
    f.write(json.dumps({json_data["id"]: f"fp_9_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_P}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
