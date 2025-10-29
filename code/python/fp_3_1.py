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
point_S = random.sample(string.ascii_uppercase, 1)[0]

# Add result calculation code

import math

def calculate(len_radius, len_cycles):
    """
    计算圆锥的母线长

    参数:
    len_radius (float): 底面半径
    len_cycles (int): 滚动圈数

    返回:
    float: 母线长
    """
    # 母线长公式: l = cycles * radius
    return len_cycles * len_radius


# 题干给定的数值
len_radius = 3.0
len_cycles = 4

# 验证输出
#result = calculate(len_radius, len_cycles)
#print(f"计算结果: {result:.6f}")



# Generate random lengths
len_radius = round(len_scaling_factor * float(len_radius), 2)
len_cycles = round(random.uniform(0.1, 10.0) * float(len_cycles), 2)

# Calculate the result
result = calculate(len_radius, len_cycles)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fp_3_1",
    "type": 3,
    "level": 1,
    "cn_problem": f"如图是底面半径为 {len_radius} 的圆锥，将其放倒在一平面上，使圆锥在此平面内绕圆锥顶点 {point_S} 滚动，当这个圆锥在平面内转回原位置时，圆锥本身恰好滚动了 {len_cycles} 周，则圆锥的母线长为______。",
    "en_problem": f"As shown in the figure, a cone with base radius {len_radius} is placed on its side on a plane, and the cone rolls around its vertex {point_S} on this plane. When the cone returns to its original position on the plane, it has rolled exactly {len_cycles} times around itself. Find the slant height of the cone.",
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
    f.write(json.dumps({json_data["id"]: f"fp_3_1({mode}, {azimuth}, {elevation}, '{point_S}')"}, ensure_ascii=False) + "\n")
