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
point_P, point_A, point_B, point_C, point_D, point_O = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate():

    return math.sqrt(2) / 2


# 测试示例
len_b = 2.0
len_c = 2 * math.sqrt(2)
len_d = math.sqrt(6)
len_k = 5.0
len_a = math.sqrt(14)

# print(calculate())

# Generate random lengths
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)
len_d = round(len_scaling_factor * float(len_d), 2)
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_6_3",
    "type": 2,
    "level": 2,
    "cn_problem": f"在三棱锥{point_P}-{point_A}{point_B}{point_C}中，{point_A}{point_B}⊥{point_B}{point_C}，{point_A}{point_B}={len_b}，{point_B}{point_C}={len_c}，{point_P}{point_B}={point_P}{point_C}={len_d}，{point_D}为{point_B}{point_P}中点，{point_O}为{point_B}{point_C}中点，{point_A}{point_D}=√{len_k}·{point_D}{point_O}，满足条件({len_k}-1){len_d}^2=4({len_a}^2+{len_b}^2)。求二面角{point_D}-{point_A}{point_O}-{point_C}的正弦值。",
    "en_problem": f"In tetrahedron {point_P}-{point_A}{point_B}{point_C}, {point_A}{point_B}⊥{point_B}{point_C}, {point_A}{point_B}={len_b}, {point_B}{point_C}={len_c}, {point_P}{point_B}={point_P}{point_C}={len_d}, {point_D} is the midpoint of {point_B}{point_P}, {point_O} is the midpoint of {point_B}{point_C}, {point_A}{point_D}=√{len_k}·{point_D}{point_O}, satisfying condition ({len_k}-1){len_d}^2=4({len_a}^2+{len_b}^2). Find the sine of dihedral angle {point_D}-{point_A}{point_O}-{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_6_3({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}')"}, ensure_ascii=False) + "\n")
