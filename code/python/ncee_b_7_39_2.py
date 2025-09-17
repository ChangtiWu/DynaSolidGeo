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
point_A, point_B, point_C, point_D, point_E, point_O = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate() -> float:
    """计算 cosθ 的值（固定为 √6/3）"""
    return math.sqrt(6) / 3

len_p = 1.0

# result = calculate()
# print(f"cosθ = {result:.6f}")

# Generate random lengths
len_p = round(len_scaling_factor * float(len_p), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_39_2",
    "type": 2,
    "level": 3,
    "cn_problem": f"在直角梯形 {point_A}{point_B}{point_C}{point_D} 中，{point_A}{point_D}∥{point_B}{point_C}，∠{point_B}{point_A}{point_D} = 90°，{point_A}{point_B} = {point_B}{point_C} = {len_p}>0，{point_A}{point_D} = 2*{len_p}。{point_E} 是 {point_A}{point_D} 的中点，{point_O} 是对角线 {point_A}{point_C} 与 {point_B}{point_E} 的交点。将 $\\triangle {point_A}{point_B}{point_E}$ 沿 {point_B}{point_E} 折起到 $\\triangle {point_A}'{point_B}{point_E}$ 的位置。若平面 {point_A}'{point_B}{point_E} ⊥ 平面 {point_B}{point_C}{point_D}{point_E}，求平面 {point_A}'{point_B}{point_C} 与平面 {point_A}'{point_C}{point_D} 夹角的余弦值 cos θ。",
    "en_problem": f"In right trapezoid {point_A}{point_B}{point_C}{point_D}, {point_A}{point_D}∥{point_B}{point_C}, ∠{point_B}{point_A}{point_D} = 90°, {point_A}{point_B} = {point_B}{point_C} = {len_p}>0, {point_A}{point_D} = 2*{len_p}. {point_E} is the midpoint of {point_A}{point_D}, {point_O} is the intersection of diagonal {point_A}{point_C} and {point_B}{point_E}. Triangle $\\triangle {point_A}{point_B}{point_E}$ is folded along {point_B}{point_E} to position $\\triangle {point_A}'{point_B}{point_E}$. If plane {point_A}'{point_B}{point_E} ⊥ plane {point_B}{point_C}{point_D}{point_E}, find the cosine value of the angle between plane {point_A}'{point_B}{point_C} and plane {point_A}'{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_39_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_O}')"}, ensure_ascii=False) + "\n")
