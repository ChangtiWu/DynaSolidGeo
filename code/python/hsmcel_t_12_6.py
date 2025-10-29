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
point_P, point_O, point_A, point_B, point_H, point_C = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_l: float) -> float:
    """
    计算当三棱锥 O-PHC 体积最大时 OB 的长度

    参数:
    len_l (float): 圆锥母线长 (PA)

    返回:
    float: OB 的长度
    """
    return len_l * math.sqrt(6) / 6


# 示例：题目中给定 PA=4，即 len_l = 4
len_l = 4

# 验证输出
# print(f"当 len_l = {len_l} 时, OB = {OB:.6f}")

# Generate random lengths
len_l = round(len_scaling_factor * float(len_l), 2)

# Calculate the result
result = calculate(len_l)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_12_6",
    "type": 7,
    "level": 2,
    "cn_problem": f"设圆锥的母线长为{len_l}，顶点为{point_P}，底面圆心为{point_O}，轴截面为等腰直角三角形。{point_A}是底面圆周上的点，{point_B}是底面圆内的点，满足{point_A}{point_B}⊥{point_O}{point_B}，{point_O}{point_H}⊥{point_P}{point_B}于{point_H}，{point_C}为{point_P}{point_A}的中点。当三棱锥{point_O}-{point_P}{point_H}{point_C}的体积最大时，求{point_O}{point_B}的长。",
    "en_problem": f"Let the cone have generatrix length {len_l}, vertex {point_P}, and base center {point_O}, with the axial section being an isosceles right triangle. Point {point_A} is on the base circle, point {point_B} is inside the base circle, satisfying {point_A}{point_B}⊥{point_O}{point_B}, {point_O}{point_H}⊥{point_P}{point_B} at {point_H}, and {point_C} is the midpoint of {point_P}{point_A}. When the volume of tetrahedron {point_O}-{point_P}{point_H}{point_C} is maximized, find the length of {point_O}{point_B}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_12_6({mode}, {azimuth}, {elevation}, '{point_P}', '{point_O}', '{point_A}', '{point_B}', '{point_H}', '{point_C}')"}, ensure_ascii=False) + "\n")
