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
point_P, point_A = random.sample(string.ascii_uppercase, 2)

# Add result calculation code
import math

def calculate(len_radius, arg_alpha):
    """
    计算圆锥侧面积

    参数:
    len_radius (float): 圆锥底面半径
    arg_alpha (float): 圆锥母线与底面所成角（弧度）

    返回:
    float: 圆锥侧面积
    """
    return math.pi * len_radius**2 / math.cos(arg_alpha)


# 题干给定的数值
len_radius = 1.0  # 底面半径 AB/2
arg_alpha = math.pi / 3  # PA 与底面所成角 π/3

# 验证输出
# side_area = calculate(len_radius, arg_alpha)
# print(f"圆锥侧面积: {side_area:.6f}")

# Generate random lengths
len_radius = round(len_scaling_factor * float(len_radius), 2)

# Calculate the result
result = calculate(len_radius, arg_alpha)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee25_9_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"设圆锥的底面直径为2*{len_radius}（底面半径为{len_radius}），直线{point_P}{point_A}与圆锥底面所成的角为{arg_alpha}（0<{arg_alpha}<\\frac{{\\pi}}{{2}}），求圆锥的侧面积。",
    "en_problem": f"Let the base diameter of the cone be 2*{len_radius} (base radius {len_radius}), and the angle between line {point_P}{point_A} and the cone base be {arg_alpha} (0<{arg_alpha}<\\frac{{\\pi}}{{2}}). Find the lateral surface area of the cone.",
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
    f.write(json.dumps({json_data["id"]: f"ncee25_9_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}')"}, ensure_ascii=False) + "\n")
