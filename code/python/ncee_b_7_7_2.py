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
point_P, point_A, point_B, point_C = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math


def calculate() -> float:
    """计算 θ 的角度值（已知 cosθ = 1/2）"""
    return math.radians(60)  # 直接返回 60°（或用 math.radians(60) 转换为弧度）


len_k = 1.0

# result = calculate()
# print(f"θ = {result}°")
# Generate random lengths
len_k = round(len_scaling_factor * float(len_k), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_7_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"设三棱锥 {point_P}-{point_A}{point_B}{point_C} 满足\n- {point_P}{point_A} ⟂ 平面 {point_A}{point_B}{point_C}，\n- {point_P}{point_A} = {point_A}{point_B} = {point_B}{point_C} = {len_k} (其中 {len_k} > 0)，\n- {point_P}{point_C} = \\sqrt{3}\\,{len_k}。\n设 θ 为二面角 \\(\\angle({point_A}-{point_P}{point_C}-{point_B})\\) 的锐角。求 θ 的大小（给出弧度值）。",
    "en_problem": f"In the tetrahedron {point_P}-{point_A}{point_B}{point_C}, the following hold:\n- {point_P}{point_A} ⟂ plane {point_A}{point_B}{point_C};\n- {point_P}{point_A} = {point_A}{point_B} = {point_B}{point_C} = {len_k} (with {len_k} > 0);\n- {point_P}{point_C} = \\sqrt{3}\\,{len_k}.\nLet θ be the acute dihedral angle \\(\\angle({point_A}-{point_P}{point_C}-{point_B})\\). Find θ (its radian value).",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_7_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}')"}, ensure_ascii=False) + "\n")
