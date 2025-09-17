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

def calculate():
    """
    计算二面角 D-AB-F 的正弦值
    已知:
        DA = DB = DC = a
        BD ⟂ CD
        ∠ADB = ∠ADC = 60°
        E 为 BC 中点
        F 满足 EF = DA
    结果与 a 无关
    """
    # 根据几何关系，结论为 √3/3
    return math.sqrt(3) / 3

len_a = 1
arg_alpha = math.pi / 3

len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_5_2",
    "type": 2,
    "level": 3,
    "cn_problem": f"三棱锥{point_A}-{point_B}{point_C}{point_D}中，{point_D}{point_A} = {point_D}{point_B} = {point_D}{point_C} = {len_a}，{point_B}{point_D} ⊥ {point_C}{point_D}，∠{point_A}{point_D}{point_B} = ∠{point_A}{point_D}{point_C} = {arg_alpha}，{point_E}为{point_B}{point_C}的中点。设点{point_F}满足$\\overrightarrow{{{point_E}{point_F}}} = \\overrightarrow{{{point_D}{point_A}}}$，求二面角{point_D}-{point_A}{point_B}-{point_F}的正弦值。",
    "en_problem": f"In tetrahedron {point_A}-{point_B}{point_C}{point_D}, {point_D}{point_A} = {point_D}{point_B} = {point_D}{point_C} = {len_a}, {point_B}{point_D} ⊥ {point_C}{point_D}, ∠{point_A}{point_D}{point_B} = ∠{point_A}{point_D}{point_C} = {arg_alpha}, and {point_E} is the midpoint of {point_B}{point_C}. Given that point {point_F} satisfies $\\overrightarrow{{{point_E}{point_F}}} = \\overrightarrow{{{point_D}{point_A}}}$, find the sine value of dihedral angle {point_D}-{point_A}{point_B}-{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_5_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
