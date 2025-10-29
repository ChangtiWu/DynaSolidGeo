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
point_P, point_A, point_B, point_C, point_D, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_c: float, len_d: float, len_e: float) -> float:
    """计算 cosθ 的表达式值"""
    numerator = len_c * abs(len_d - 2 * len_e)
    denom_part1 = math.sqrt(len_e**2 + (len_d - len_e)**2)
    denom_part2 = math.sqrt(2 * len_c**2 + (len_d - len_c)**2)
    denominator = denom_part1 * denom_part2
    return numerator / denominator


len_c = 1.0
len_d = 3.0
len_e = 2.0

# result = calculate(len_c, len_d, len_e)
# print(f"cosθ = {result:.4f}")
# Generate random lengths
len_c = round(len_scaling_factor * float(len_c), 2)
len_d = round(len_scaling_factor * float(len_d), 2)
len_e = round(len_scaling_factor * float(len_e), 2)

# Calculate the result
result = calculate(len_c, len_d, len_e)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_3_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"设四棱锥 {point_P}-{point_A}{point_B}{point_C}{point_D} 满足\n- {point_B}{point_C} ∥ {point_A}{point_D}；\n- {point_A}{point_B} = {point_B}{point_C} = {len_c} (>0)，{point_A}{point_D} = {len_d} (>0) 且 {point_A}{point_B} ⟂ {point_A}{point_D}；\n- 取点 {point_E} ∈ {point_A}{point_D} 使 {point_P}{point_E} ⟂ {point_A}{point_D} 且 {point_P}{point_E} = {point_E}{point_D} = {len_e} (>0)。\n\n设 θ 为平面 {point_P}{point_A}{point_B} 与平面 {point_P}{point_C}{point_D} 所成锐角，求\n\\(\\displaystyle\\cos θ\\) 。",
    "en_problem": f"Let a pyramid {point_P}-{point_A}{point_B}{point_C}{point_D} satisfy\n- {point_B}{point_C} ∥ {point_A}{point_D};\n- {point_A}{point_B} = {point_B}{point_C} = {len_c} (>0) and {point_A}{point_D} = {len_d} (>0) with {point_A}{point_B} ⟂ {point_A}{point_D};\n- A point {point_E} on {point_A}{point_D} is chosen so that {point_P}{point_E} ⟂ {point_A}{point_D} and {point_P}{point_E} = {point_E}{point_D} = {len_e} (>0).\n\nLet θ be the acute dihedral angle between planes {point_P}{point_A}{point_B} and {point_P}{point_C}{point_D}. Find \n\\(\\cos θ\\).",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_3_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}')"}, ensure_ascii=False) + "\n")
