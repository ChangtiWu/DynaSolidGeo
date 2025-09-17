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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
def calculate(len_a, len_h):
    """计算param_cos的值（表达式为 -len_a²/(2len_h²)，需满足len_h > len_a/√2）"""
    return - (len_a ** 2) / (2 * (len_h ** 2))


# 测试示例
len_a = 2.0
len_h = 4.0

# print(calculate(len_a, len_h))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h)

# Define LaTeX expressions separately to avoid backslashes in f-strings
vec_d = "\\vec{d}"
overrightarrow_AA1 = f"\\overrightarrow{{{point_A}{point_A1}}}"

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_37_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"如图，在三棱柱 {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1} 中：(1) 底面 △{point_A}{point_B}{point_C} 为直角等腰三角形，且 ∠{point_B}{point_A}{point_C}=90°，{point_A}{point_B}={point_A}{point_C}={len_a}>0；(2) 侧棱向量 ${vec_d}={overrightarrow_AA1}$ 满足：长度 |${vec_d}$|={len_h}>0，且 ${vec_d}$ 在底面上的射影把 {point_B}{point_C} 平分（即 {point_A1} 在 {point_B}{point_C} 的中垂线上）；(3) 令 {point_B1}={point_B}+${vec_d}$，{point_C1}={point_C}+${vec_d}$，{point_D} 为线段 {point_B1}{point_C1} 的中点。求二面角 {point_A1}-{point_B}{point_D}-{point_B1} 的余弦值。",
    "en_problem": f"As shown, in triangular prism {point_A}{point_B}{point_C}-{point_A1}{point_B1}{point_C1}: (1) the base △{point_A}{point_B}{point_C} is a right isosceles triangle with ∠{point_B}{point_A}{point_C}=90° and {point_A}{point_B}={point_A}{point_C}={len_a}>0; (2) the lateral edge vector ${vec_d}={overrightarrow_AA1}$ satisfies: length |${vec_d}$|={len_h}>0, and the projection of ${vec_d}$ onto the base bisects {point_B}{point_C} (i.e., {point_A1} lies on the perpendicular bisector of {point_B}{point_C}); (3) let {point_B1}={point_B}+${vec_d}$, {point_C1}={point_C}+${vec_d}$, and {point_D} is the midpoint of segment {point_B1}{point_C1}. Find the cosine of dihedral angle {point_A1}-{point_B}{point_D}-{point_B1}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_37_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}')"}, ensure_ascii=False) + "\n")
