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
point_O, point_A, point_B, point_C, point_D, point_E, point_F, point_S = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_R):
    """计算最大体积volume_max（公式：(4√15/125) * len_R³）"""
    return (4 * math.sqrt(15) / 125) * (len_R ** 3)


# 测试示例
len_R = 5.0

# print(calculate(len_R))

# Generate random lengths
len_R = round(len_scaling_factor * float(len_R), 2)

# Calculate the result
result = calculate(len_R)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_s1_2_27_1",
    "type": 8,
    "level": 2,
    "cn_problem": f"圆形纸片的圆心为{point_O}，半径为{len_R}。等边三角形{point_A}{point_B}{point_C}的中心为{point_O}，点{point_D}，{point_E}，{point_F}在圆{point_O}上，△{point_D}{point_B}{point_C}，△{point_E}{point_C}{point_A}，△{point_F}{point_A}{point_B}分别是以{point_B}{point_C}，{point_C}{point_A}，{point_A}{point_B}为底边的等腰三角形。沿虚线剪开后，分别以{point_B}{point_C}，{point_C}{point_A}，{point_A}{point_B}为折痕折起△{point_D}{point_B}{point_C}，△{point_E}{point_C}{point_A}，△{point_F}{point_A}{point_B}，使得{point_D}，{point_E}，{point_F}重合为点{point_S}，得到三棱锥。当△{point_A}{point_B}{point_C}的边长变化时，所得三棱锥体积的最大值为多少？",
    "en_problem": f"A circular paper has center {point_O} and radius {len_R}. An equilateral triangle {point_A}{point_B}{point_C} has its center at {point_O}. Points {point_D}, {point_E}, {point_F} are on circle {point_O}, and triangles △{point_D}{point_B}{point_C}, △{point_E}{point_C}{point_A}, △{point_F}{point_A}{point_B} are isosceles triangles with bases {point_B}{point_C}, {point_C}{point_A}, {point_A}{point_B} respectively. After cutting along dotted lines and folding △{point_D}{point_B}{point_C}, △{point_E}{point_C}{point_A}, △{point_F}{point_A}{point_B} along fold lines {point_B}{point_C}, {point_C}{point_A}, {point_A}{point_B}, points {point_D}, {point_E}, {point_F} coincide at point {point_S} to form a triangular pyramid. When the edge length of △{point_A}{point_B}{point_C} varies, what is the maximum volume of the resulting triangular pyramid?",
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
    f.write(json.dumps({json_data["id"]: f"ncee_s1_2_27_1({mode}, {azimuth}, {elevation}, '{point_O}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_S}')"}, ensure_ascii=False) + "\n")
