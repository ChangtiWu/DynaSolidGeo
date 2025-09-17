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
point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate():
    """计算满足cos(theta) = √3/3的角度theta（弧度制）"""
    return math.sqrt(3) / 3


# 测试示例
arg_alpha = math.pi / 3 * 2

# print(calculate())


# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_5_5_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"四边形{point_A}{point_B}{point_C}{point_D}为菱形，∠{point_A}{point_B}{point_C}={arg_alpha}，{point_E}，{point_F}是平面{point_A}{point_B}{point_C}{point_D}同一侧的两点，{point_B}{point_E}⊥平面{point_A}{point_B}{point_C}{point_D}，{point_D}{point_F}⊥平面{point_A}{point_B}{point_C}{point_D}，{point_B}{point_E}=2*{point_D}{point_F}，{point_A}{point_E}⊥{point_E}{point_C}。求直线{point_A}{point_E}与直线{point_C}{point_F}所成角的余弦值。",
    "en_problem": f"Quadrilateral {point_A}{point_B}{point_C}{point_D} is a rhombus with ∠{point_A}{point_B}{point_C}={arg_alpha}. Points {point_E} and {point_F} are on the same side of plane {point_A}{point_B}{point_C}{point_D}, with {point_B}{point_E}⊥plane {point_A}{point_B}{point_C}{point_D}, {point_D}{point_F}⊥plane {point_A}{point_B}{point_C}{point_D}, and {point_B}{point_E}=2*{point_D}{point_F}. Given {point_A}{point_E}⊥{point_E}{point_C}, find the cosine of the angle between lines {point_A}{point_E} and {point_C}{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_5_5_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
