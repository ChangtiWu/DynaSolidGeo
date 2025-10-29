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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_P = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算平面 α 与 ABCD 平面所成锐二面角的最小值及截面面积

    参数:
    len_a (float): 正方体棱长

    返回:
    tuple: (最小锐二面角, 截面面积)
    """
    
    area_section = len_a**2 * (4 - 3 * math.sqrt(2) / 2)
    return area_section


# 题干给定的数值
len_a = 1.0  # 正方体棱长

# 验证输出
# angle, area = calculate(len_a)
# print(f"最小锐二面角: {angle:.6f} rad")
# print(f"截面面积: {area:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "zht_14_3_2",
    "type": 7,
    "level": 2,
    "cn_problem": f"设正方体 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} 的棱长为 {len_a}，{point_P} 是对角面 {point_B}{point_D}{point_D1}{point_B1}（包含边界）内一点，满足 {point_P}{point_A} ⊥ {point_P}{point_C}。过 {point_P} 作平面 α 与直线 {point_P}{point_C} 垂直，求：平面 α 与平面 {point_A}{point_B}{point_C}{point_D} 所成锐二面角为最小值时平面 α 截正方体所得截面图形的面积。",
    "en_problem": f"Let the edge length of cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} be {len_a}, {point_P} is a point in the diagonal face {point_B}{point_D}{point_D1}{point_B1} (including boundary), satisfying {point_P}{point_A} ⊥ {point_P}{point_C}. Through {point_P}, make plane α perpendicular to line {point_P}{point_C}. When the value of the acute dihedral angle between plane α and plane {point_A}{point_B}{point_C}{point_D} is minimum, find the area of the cross-section figure when plane α intersects the cube.",
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
    f.write(json.dumps({json_data["id"]: f"zht_14_3_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_P}')"}, ensure_ascii=False) + "\n")
