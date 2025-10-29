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
point_A, point_B1, point_C, point_D1 = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算正四面体的表面积和体积

    参数:
    len_a (float): 四面体的棱长

    返回:
    tuple: 表面积 S 和体积 V
    """

    # 体积公式 V = (√2 / 12) * len_a^3
    V = (math.sqrt(2) / 12) * len_a ** 3
    return V


# 定义题干参数
len_a = math.sqrt(2)

# 验证计算结果
#surface_area, volume = calculate(len_a)
#print(f"表面积: {surface_area:.6f}, 体积: {volume:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_8_1_2",
    "type": 5,
    "level": 1,
    "cn_problem": f"若四面体 {point_A} - {point_B1}{point_C}{point_D1} 各棱长均为 {len_a}，求该四面体的体积。",
    "en_problem": f"If all edges of tetrahedron {point_A} - {point_B1}{point_C}{point_D1} have length {len_a}, find the volume of this tetrahedron.",
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
    f.write(json.dumps({json_data["id"]: f"area2_8_1_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B1}', '{point_C}', '{point_D1}')"}, ensure_ascii=False) + "\n")
