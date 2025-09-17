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
point_P, point_A, point_B, point_C, point_O, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_l, len_h, ang_phi):
    """计算param_sin的值（表达式为√[1 - (分子/分母)²]，其中分子含三角函数和长度参数，分母为两个平方根的乘积）"""
    # 计算分子部分：3*(len_l² - len_h²)*sin(ang_phi)*cos(ang_phi)
    numerator = 3 * (len_l ** 2 - len_h ** 2) * math.sin(ang_phi) * math.cos(ang_phi)

    # 计算分母的两个平方根部分
    denominator1 = math.sqrt(len_h ** 2 + (len_l ** 2 - len_h ** 2) * (math.sin(ang_phi)) ** 2)
    denominator2 = math.sqrt(len_h ** 2 + 9 * (len_l ** 2 - len_h ** 2) * (math.cos(ang_phi)) ** 2)
    denominator = denominator1 * denominator2

    # 计算分数的平方
    fraction_squared = (numerator / denominator) ** 2

    # 计算最终结果
    return math.sqrt(1 - fraction_squared)


# 测试示例
len_l = 5.0
len_h = 3.0
ang_phi = math.pi / 6

# print(calculate(len_l, len_h, ang_phi))

# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)
len_l = round(len_scaling_factor * float(len_l), 2)

# Calculate the result
result = calculate(len_l, len_h, ang_phi)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_7_10_2",
    "type": 2,
    "level": 3,
    "cn_problem": f"如图，在四面体 {point_P}-{point_A}{point_B}{point_C} 中：(1) {point_P}{point_O}⊥△{point_A}{point_B}{point_C}，且 {point_P}{point_O}={len_h}>0（{point_O} 为垂足）；(2) {point_P}{point_A}={point_P}{point_B}={len_l}（{len_l}>{len_h}）；(3) {point_A}{point_B}⊥{point_A}{point_C}；(4) 设 ∠{point_A}{point_B}{point_O}=∠{point_C}{point_B}{point_O}={ang_phi}（0<{ang_phi}<90°）；(5) 点 {point_E} 为棱 {point_P}{point_B} 的中点。求二面角 {point_C}-{point_A}{point_E}-{point_B} 的正弦值。",
    "en_problem": f"As shown, in tetrahedron {point_P}-{point_A}{point_B}{point_C}: (1) {point_P}{point_O}⊥△{point_A}{point_B}{point_C} with {point_P}{point_O}={len_h}>0 ({point_O} is the foot); (2) {point_P}{point_A}={point_P}{point_B}={len_l} ({len_l}>{len_h}); (3) {point_A}{point_B}⊥{point_A}{point_C}; (4) let ∠{point_A}{point_B}{point_O}=∠{point_C}{point_B}{point_O}={ang_phi} (0<{ang_phi}<90°); (5) point {point_E} is the midpoint of edge {point_P}{point_B}. Find the sine of dihedral angle {point_C}-{point_A}{point_E}-{point_B}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_7_10_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_O}', '{point_E}')"}, ensure_ascii=False) + "\n")
