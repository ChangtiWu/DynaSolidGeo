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


def calculate(len_a, ang_theta):
    """
    计算体积 V_{point_F-point_A point_B point_C}

    参数:
        len_a (float): 长度参数 a
        ang_theta (float): 角度 θ（以弧度为单位）

    返回:
        float: 体积计算结果

    公式:
        V = (len_a³ / 3) × cos²(θ) × sin³(θ)
    """
    # 计算主要表达式
    return (len_a ** 3 / 3) * (math.cos(ang_theta) ** 2) * (math.sin(ang_theta) ** 3)

# 边长为 2，角度为 π/4 (45 度)
len_a = 2.0
ang_theta = math.pi/3

# volume = calculate(len_a, ang_theta)
# print(f"体积 V = {volume:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, ang_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_4_2",
    "type": 5,
    "level": 2,
    "cn_problem": f"设四面体 {point_A}{point_B}{point_C}{point_D} 满足：{point_A}{point_B}={point_B}{point_C}={len_a}（{len_a}>0）；∠{point_A}{point_C}{point_B}={ang_theta}（0<{ang_theta}<\\tfrac{{\\pi}}{{2}}）；{point_A}{point_D}⊥{point_C}{point_D}，且 {point_A}{point_D}={point_C}{point_D}；∠{point_A}{point_D}{point_B}=∠{point_B}{point_D}{point_C}；{point_E} 为 {point_A}{point_C} 的中点。记点 {point_F} 在棱 {point_B}{point_D} 上。当 \\triangle {point_A}{point_F}{point_C} 的面积达到最小值时，求三棱锥 {point_F}-{point_A}{point_B}{point_C} 的体积 V_{{{point_F}-{point_A}{point_B}{point_C}}}。",
    "en_problem": f"Given tetrahedron {point_A}{point_B}{point_C}{point_D} satisfying: {point_A}{point_B}={point_B}{point_C}={len_a} (where {len_a}>0); ∠{point_A}{point_C}{point_B}={ang_theta} (0<{ang_theta}<\\tfrac{{\\pi}}{{2}}）；{point_A}{point_D}⊥{point_C}{point_D}，且 {point_A}{point_D}={point_C}{point_D}；∠{point_A}{point_D}{point_B}=∠{point_B}{point_D}{point_C}；{point_E} 为 {point_A}{point_C} 的中点。记点 {point_F} 在棱 {point_B}{point_D} 上。当 \\triangle {point_A}{point_F}{point_C} 的面积达到最小值时，求三棱锥 {point_F}-{point_A}{point_B}{point_C} 的体积 V_{{{point_F}-{point_A}{point_B}{point_C}}}。",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_4_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
