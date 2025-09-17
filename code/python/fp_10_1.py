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
point_M, point_A, point_B = random.sample(string.ascii_uppercase, 3)

# Add result calculation code
import math

def calculate(len_upper_radius, len_lower_radius, len_slant):
    """
    计算从M绕圆台侧面到A的最短绳长

    参数:
    len_upper_radius (float): 上底半径
    len_lower_radius (float): 下底半径
    len_slant (float): 母线长

    返回:
    float: 最短绳长
    """
    # 按公式分步写清楚
    term1 = (len_lower_radius * len_slant) / (len_lower_radius - len_upper_radius)
    term2 = (len_slant * (len_lower_radius + len_upper_radius)) / (2 * (len_lower_radius - len_upper_radius))
    angle = (2 * math.pi * (len_lower_radius - len_upper_radius)) / len_slant

    result = math.sqrt(term1**2 + term2**2 - 2 * term1 * term2 * math.cos(angle))
    return result


# 题干给定的数值
len_upper_radius = 5.0
len_lower_radius = 10.0
len_slant = 20.0

# 验证输出
#result = calculate(len_upper_radius, len_lower_radius, len_slant)
#print(f"计算结果: {result:.6f}")


# Generate random lengths
len_upper_radius = round(len_scaling_factor * float(len_upper_radius), 2)
len_lower_radius = round(len_scaling_factor * float(len_lower_radius), 2)
len_slant = round(len_scaling_factor * float(len_slant), 2)

# Calculate the result
result = calculate(len_upper_radius, len_lower_radius, len_slant)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fp_10_1",
    "type": 3,
    "level": 1,
    "cn_problem": f"设圆台上底面半径为 {len_upper_radius}，下底面半径为 {len_lower_radius}（{len_lower_radius} > {len_upper_radius}），母线长为 {len_slant}，点 {point_M} 是母线 {point_A}{point_B} 的中点。求从 {point_M} 绕圆台侧面到 {point_A} 的最短绳长。",
    "en_problem": f"Let the upper base radius of the frustum be {len_upper_radius}, the lower base radius be {len_lower_radius} ({len_lower_radius} > {len_upper_radius}), the slant height be {len_slant}, and point {point_M} is the midpoint of generatrix {point_A}{point_B}. Find the shortest rope length from {point_M} around the lateral surface of the frustum to {point_A}.",
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
    f.write(json.dumps({json_data["id"]: f"fp_10_1({mode}, {azimuth}, {elevation}, '{point_M}', '{point_A}', '{point_B}')"}, ensure_ascii=False) + "\n")
