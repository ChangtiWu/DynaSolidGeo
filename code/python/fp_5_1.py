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
point_A, point_B = random.sample(string.ascii_uppercase, 2)

# Add result calculation code
import math

def calculate(len_height, len_radius):
    """
    计算圆柱侧面最短路径长度

    参数:
    len_height (float): 圆柱的高
    len_radius (float): 底面半径

    返回:
    float: 最短路径长度
    """
    # 公式: shortest = sqrt(h^2 + (πr)^2)
    return math.sqrt(len_height**2 + (math.pi * len_radius)**2)


# 题干给定的数值
len_height = math.sqrt(13)
len_radius = math.sqrt(3)

# 验证输出
#result = calculate(len_height, len_radius)
#print(f"计算结果: {result:.6f}")


# Generate random lengths
len_height = round(len_scaling_factor * float(len_height), 2)
len_radius = round(len_scaling_factor * float(len_radius), 2)

# Calculate the result
result = calculate(len_height, len_radius)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fp_5_1",
    "type": 3,
    "level": 1,
    "cn_problem": f"设圆柱的高为 {len_height}，底面圆的半径为 {len_radius}。在此圆柱侧面上，从左下顶点 {point_A} 到右上顶点 {point_B} 的路径中，最短路径的长度为______。",
    "en_problem": f"Let the height of the cylinder be {len_height} and the radius of the base circle be {len_radius}. On the lateral surface of this cylinder, from the bottom-left vertex {point_A} to the top-right vertex {point_B}, find the length of the shortest path.",
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
    f.write(json.dumps({json_data["id"]: f"fp_5_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}')"}, ensure_ascii=False) + "\n")
