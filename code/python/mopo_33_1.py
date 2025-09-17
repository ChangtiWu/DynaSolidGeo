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
point_P, point_E, point_F, point_B, point_C, point_A = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
def calculate(len_n, len_m):
    """计算轨迹方程右侧的常数项（表达式为(2lenₙ² - lenₘ²)/4）"""
    return (2 * len_n ** 2 - len_m ** 2) / 4


# 测试示例
len_n = 2
len_m = 2

# print(calculate(len_n, len_m))

# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)
len_n = round(len_scaling_factor * float(len_n), 2)

# Calculate the result
result = calculate(len_n, len_m)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "mopo_33_1",
    "type": 7,
    "level": 2,
    "cn_problem": f"平面 $\\\\alpha$ 与圆柱相交，且平面 $\\\\alpha$ 与圆柱的轴不垂直，点 {point_P} 为平面 $\\\\alpha$ 与圆柱表面交线上的任意一点，在圆柱内部放置两个半径与圆柱底面半径相同的球，平面 $\\\\alpha$ 分别与两球切于 {point_E}, {point_F} 两点，过点 {point_P} 作圆柱的母线，分别与两球切于 {point_B}, {point_C} 两点，记线段 ${point_E}{point_F}$ 长度为 ${len_m}$，线段 ${point_B}{point_C}$ 长度为 ${len_n}$，且 ${len_n} > {len_m}$。在平面 $\\\\alpha$ 内 $\\\\Gamma$ 的任意两条互相垂直的切线的交点为 {point_A}，建立适当的坐标系，求动点 {point_A} 的轨迹方程： x^2 + y^2 = ______。",
    "en_problem": f"Plane $\\\\alpha$ intersects a cylinder, and plane $\\\\alpha$ is not perpendicular to the axis of the cylinder. Point {point_P} is any point on the intersection line between plane $\\\\alpha$ and the cylinder surface, two spheres with radii equal to the base radius of the cylinder are placed inside the cylinder. Plane $\\\\alpha$ is tangent to the two spheres at points {point_E} and {point_F} respectively. A generatrix of the cylinder passing through point {point_P} is tangent to the two spheres at points {point_B} and {point_C} respectively. Let the length of segment ${point_E}{point_F}$ be ${len_m}$ and the length of segment ${point_B}{point_C}$ be ${len_n}$, where ${len_n} > {len_m}$. In plane $\\\\alpha$, the intersection point of any two mutually perpendicular tangent lines of $\\\\Gamma$ is {point_A}. Establish an appropriate coordinate system and find the trajectory equation of moving point {point_A}: x^2 + y^2 = ______.",
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
    f.write(json.dumps({json_data["id"]: f"mopo_33_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_E}', '{point_F}', '{point_B}', '{point_C}', '{point_A}')"}, ensure_ascii=False) + "\n")
