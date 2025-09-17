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
point_P, point_A, point_B, point_C, point_M = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_a):
    """
    计算给定的几何表达式

    参数:
    len_a (float): 已知边长

    返回:
    float: 计算结果
    """
    # 根据题干解法，h = (len_a * sqrt(2)) / 2
    result = (len_a * math.sqrt(2)) / 2
    return result


# 定义题干参数
len_a = 2.0

# 验证输出（与参考答案对比）
#result = calculate(len_a)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_6",
    "type": 3,
    "level": 1,
    "cn_problem": f"在我国古代数学名著《九章算术》中，四个面都为直角三角形的三棱锥称为鳖臑。已知在鳖臑{point_P}-{point_A}{point_B}{point_C}中，{point_P}{point_A}⊥平面{point_A}{point_B}{point_C}，{point_P}{point_A}={point_A}{point_B}={point_B}{point_C}={len_a}，{point_M}为{point_P}{point_C}的中点，求点{point_P}到平面{point_M}{point_A}{point_B}的距离。",
    "en_problem": f"In the ancient Chinese mathematical text \"Nine Chapters on the Mathematical Art\", a triangular pyramid with four right triangles as faces is called a \"turtle nose\". In turtle nose {point_P}-{point_A}{point_B}{point_C}, {point_P}{point_A}⊥plane {point_A}{point_B}{point_C}, {point_P}{point_A}={point_A}{point_B}={point_B}{point_C}={len_a}, and {point_M} is the midpoint of {point_P}{point_C}. Find the distance from point {point_P} to plane {point_M}{point_A}{point_B}.",
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
    f.write(json.dumps({json_data["id"]: f"sup_6({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_M}')"}, ensure_ascii=False) + "\n")
