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
import math

def calculate(len_radius, len_height):
    """
    计算两个相等铁球在圆柱容器内能放下的最大半径

    参数:
    len_radius (float): 圆柱底面半径
    len_height (float): 圆柱高度

    返回:
    float: 铁球最大半径
    """
    return len_radius + len_height / 2 - math.sqrt(len_radius * len_height)


# 题干给定的数值
len_radius = 4.0
len_height = 9.0

# 验证输出
#max_radius = calculate(len_radius, len_height)
#print(f"最大铁球半径: {max_radius:.6f} cm")

# Generate random lengths
len_radius = round(len_scaling_factor * float(len_radius), 2)
len_height = round(len_scaling_factor * float(len_height), 2)

# Calculate the result
result = calculate(len_radius, len_height)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee25_4_1",
    "type": 3,
    "level": 1,
    "cn_problem": f"一个底面半径为 {len_radius}，高为 {len_height} 的封闭圆柱形容器（壁厚忽略）内有两个半径相等的铁球，求铁球半径的**最大值**。",
    "en_problem": f"A closed cylindrical container with base radius {len_radius} and height {len_height} (wall thickness negligible) contains two iron balls of equal radius. Find the **maximum** radius of the iron balls.",
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
    f.write(json.dumps({json_data["id"]: f"ncee25_4_1({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
