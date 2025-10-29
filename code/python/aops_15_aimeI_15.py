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
point_A, point_B, point_O = random.sample(string.ascii_uppercase, 3)

# Add result calculation code
import math


def calculate(len_r, ang_phi, len_h):
    """计算面积area_S的值（公式：[len_r(ang_phi + 2sinφ)]/(4cos(φ/2)) * √(len_h² + 4len_r²cos²(φ/2))）"""
    # 计算中间三角函数值
    sin_ang_phi = math.sin(ang_phi)
    cos_ang_phi_half = math.cos(ang_phi / 2)

    # 计算分子部分：len_r*(ang_phi + 2sin(ang_phi))
    numerator = len_r * (ang_phi + 2 * sin_ang_phi)

    # 计算分母部分：4*cos(ang_phi/2)
    denominator = 4 * cos_ang_phi_half

    # 计算分数项
    fraction = numerator / denominator

    # 计算平方根内的部分：len_h² + 4len_r²cos²(ang_phi/2)
    sqrt_inner = len_h ** 2 + 4 * (len_r ** 2) * (cos_ang_phi_half ** 2)
    sqrt_term = math.sqrt(sqrt_inner)

    # 计算最终面积
    return fraction * sqrt_term


# 测试示例
len_r = 6.0
ang_phi = math.pi / 3 * 2
len_h = 8.0

# print(calculate(len_r, ang_phi, len_h))

# Generate random lengths
len_r = round(len_scaling_factor * float(len_r), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_r, ang_phi, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_15_aimeI_15",
    "type": 2,
    "level": 2,
    "cn_problem": f"如图，设有一圆柱形木块，其底面半径为 {len_r}>0，高为 {len_h}>0。在下底面圆周上取两点 {point_A}、{point_B}，使得圆心角 ∠{point_A}{point_O}{point_B}={ang_phi}（0<{ang_phi}<π）。过点 {point_A}、{point_B} 及圆柱的几何中心 {point_O}（两底面圆心连线的中点）作一平面，将圆柱劈成两半并显露出新的平截面。求该平截面的面积。",
    "en_problem": f"As shown, consider a cylindrical block of wood with base radius {len_r}>0 and height {len_h}>0. Two points {point_A} and {point_B} are chosen on the circumference of the bottom face such that the central angle ∠{point_A}{point_O}{point_B}={ang_phi} (0<{ang_phi}<π). A plane is drawn through points {point_A}, {point_B}, and the geometric center {point_O} of the cylinder (the midpoint of the line connecting the centers of the two bases), cutting the cylinder in half and revealing a new cross-section. Find the area of this cross-section.",
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
    f.write(json.dumps({json_data["id"]: f"aops_15_aimeI_15({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_O}')"}, ensure_ascii=False) + "\n")
