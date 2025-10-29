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
point_A, point_B, point_C, point_D, point_O1, point_O2, point_M = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math

def calculate(len_radius, arg_theta):
    """
    计算圆台的母线长

    参数:
    len_radius (float): 上底半径
    arg_theta (float): cos∠MO₁D 的值

    返回:
    float: 母线长
    """
    # 公式: l = r / sqrt(2 * (1 - cosθ))
    return len_radius / math.sqrt(2 * (1 - arg_theta))


# 题干给定的数值
len_upper = 2 * math.sqrt(3)
len_lower = 4 * math.sqrt(3)
len_radius = math.sqrt(3)
arg_theta = 5 / 8

# 验证输出
#result = calculate(len_radius, arg_theta)
#print(f"计算结果: {result:.6f}")


# Generate random lengths
len_upper = round(len_scaling_factor * float(len_upper), 2)
len_radius = round(len_scaling_factor * float(len_radius), 2)
len_lower = round(len_scaling_factor * float(len_lower), 2)

# Calculate the result
result = calculate(len_radius, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fp_4_1",
    "type": 3,
    "level": 1,
    "cn_problem": f"在圆亭（圆台）{point_O1}{point_O2} 的轴截面 {point_A}{point_B}{point_C}{point_D} 中，上底直径 {len_upper} = 2*{len_radius}（故上底半径  len_upper_radius  = {len_radius}，弧 CD 为半圆，圆心角 180°），下底直径 {len_lower} = 2*{len_upper}（即 {len_lower} = 4*{len_radius}，下底半径  len_lower_radius  = 2*{len_radius}）。点 {point_M} 为弧 CD 上一点，且弧  len_arc1  = 2弧 len_arc2 （弧 CD 被分为 3 等份，弧 len_arc2  = 60°，弧 len_arc1  = 120°），若 cos∠{point_M}{point_O1}{point_D} = {arg_theta}，求圆台的母线长。",
    "en_problem": f"In the axial cross-section {point_A}{point_B}{point_C}{point_D} of the frustum {point_O1}{point_O2}, the upper base diameter {len_upper} = 2*{len_radius} (hence the upper base radius  len_upper_radius  = {len_radius}, arc CD is a semicircle with central angle 180°), the lower base diameter {len_lower} = 2*{len_upper} (i.e., {len_lower} = 4*{len_radius}, lower base radius  len_lower_radius  = 2*{len_radius}). Point {point_M} is a point on arc CD, and arc  len_arc1  = 2 arc  len_arc2  (arc CD is divided into 3 equal parts, arc  len_arc2  = 60°, arc  len_arc1  = 120°). If cos∠{point_M}{point_O1}{point_D} = {arg_theta}, find the slant height of the frustum.",
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
    f.write(json.dumps({json_data["id"]: f"fp_4_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O1}', '{point_O2}', '{point_M}')"}, ensure_ascii=False) + "\n")
