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


def calculate(len_a, len_h, len_r):
    """计算总体积volume_total（公式：(3√3/2)len_a²len_h - πlen_r²len_h）"""
    term1 = (3 * math.sqrt(3) / 2) * (len_a ** 2) * len_h
    term2 = math.pi * (len_r ** 2) * len_h
    return term1 - term2


# 测试示例
len_a = 2.0
len_h = 2.0
len_r = 0.5

# print(calculate(len_a, len_h, len_r))

# Generate random lengths
len_r = round(len_scaling_factor * float(len_r), 2)
len_h = round(len_scaling_factor * float(len_h), 2)
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, len_h, len_r)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_s1_2_19_1",
    "type": 5,
    "level": 1,
    "cn_problem": f"六角螺帽毛坯由正六棱柱（底面正六边形边长为{len_a}，高为{len_h}）挖去一个圆柱（内孔半径为{len_r}，高为{len_h}）构成。求该螺帽毛坯的体积。",
    "en_problem": f"A hexagonal nut blank is formed by removing a cylinder (inner radius {len_r}, height {len_h}) from a regular hexagonal prism (base regular hexagon side length {len_a}, height {len_h}). Find the volume of this hexagonal nut blank.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_s1_2_19_1({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
