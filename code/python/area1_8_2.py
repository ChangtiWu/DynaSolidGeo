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
point_A, point_B, point_C = random.sample(string.ascii_uppercase, 3)

# Add result calculation code
import math


def calculate(len_sphere_radius, len_density, len_cylinder_radius, len_height):
    """
    计算给定的几何表达式（圆柱侧面积与球B表面积的比值）

    参数:
    len_sphere_radius (float): 小球半径
    len_density (float): 小球材质密度
    len_cylinder_radius (float): 圆柱底面半径
    len_height (float): 圆柱高

    返回:
    float: 计算结果
    """
    return math.sqrt(3) + 2


# 定义题干中的变量
len_sphere_radius = 1  # 题干有提，但公式没用到，需定义
len_density = 1e3  # 给出 >1×10³，定义为1000占位


# result = calculate(len_sphere_radius, len_density, len_cylinder_radius, len_height)
# print(f"计算结果: {result:.6f}")
 
# Generate random lengths
len_sphere_radius = round(len_scaling_factor * float(len_sphere_radius), 2)
len_cylinder_radius = (math.sqrt(3) + 2) * len_sphere_radius / 2
len_height = 4 * len_sphere_radius

# Calculate the result
result = calculate(len_sphere_radius, len_density, len_cylinder_radius, len_height)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area1_8_2",
    "type": 4,
    "level": 1,
    "cn_problem": f"在水平放置的圆柱内，放入三个半径均为 {len_sphere_radius} 的实心小球 {point_A},{point_B},{point_C}（小球材质密度 > {len_density}），小球 {point_A},{point_C} 分别与上底面、下底面相切，小球 {point_B} 与圆柱壁相切，且 {point_A},{point_B},{point_C} 在圆柱的轴截面中。已知圆柱底面半径 {len_cylinder_radius} = \\frac{{(\\sqrt{{3}} + 2)*{len_sphere_radius}}}{{2}}，圆柱的高 {len_height} = 4*{len_sphere_radius}，求圆柱的侧面积与球 {point_B} 的表面积的比值。",
    "en_problem": f"In a horizontally placed cylinder, three solid spheres {point_A}, {point_B}, {point_C} with radius {len_sphere_radius} are placed (sphere material density > {len_density}). Spheres {point_A} and {point_C} are tangent to the upper and lower bases respectively, sphere {point_B} is tangent to the cylinder wall, and {point_A}, {point_B}, {point_C} lie in the axial cross-section of the cylinder. Given that the cylinder base radius {len_cylinder_radius} = \\frac{{(\\sqrt{{3}} + 2)*{len_sphere_radius}}}{{2}} and cylinder height {len_height} = 4*{len_sphere_radius}, find the ratio of the cylinder's lateral surface area to the surface area of sphere {point_B}.",
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
    f.write(json.dumps({json_data["id"]: f"area1_8_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}')"}, ensure_ascii=False) + "\n")
