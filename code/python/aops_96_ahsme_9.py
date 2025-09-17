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
point_A, point_B, point_P, point_C, point_D = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math


def calculate(len_a: float, len_c: float) -> float:
    """计算 len_d 的值（公式：len_d = √(len_a² + len_c²)）"""
    return math.sqrt(len_a ** 2 + len_c ** 2)


len_a = 3.0
len_b = 4.0
len_c = 5.0

# result = calculate(len_a, len_c)
# print(f"len_d = {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_96_ahsme_9",
    "type": 3,
    "level": 1,
    "cn_problem": f"设直线 ${point_A}{point_B}$ 为两相互垂直平面的交线：在平面 $plane_pi1$ 内作三角形 ${point_P}{point_A}{point_B}$，已知 ${point_P}{point_A}={len_a}, ${point_P}{point_B}={len_b}, ${point_A}{point_B}={len_c}\\;({len_a},{len_b},{len_c}>0)$。在垂直的平面 $plane_pi2$ 内，以 ${point_A}{point_B}$ 为一边作正方体的一个面 ${point_A}{point_B}{point_C}{point_D}$，故 ${point_A}{point_D}={point_A}{point_B}={len_c}$。求点 ${point_P}$ 与点 ${point_D}$ 间的距离。",
    "en_problem": f"Let line ${point_A}{point_B}$ be the intersection of two mutually perpendicular planes: in plane $plane_pi1$, construct triangle ${point_P}{point_A}{point_B}$ with ${point_P}{point_A}={len_a}, ${point_P}{point_B}={len_b}, ${point_A}{point_B}={len_c}\\;({len_a},{len_b},{len_c}>0)$. In the perpendicular plane $plane_pi2$, construct square ${point_A}{point_B}{point_C}{point_D}$ with ${point_A}{point_B}$ as one side, so ${point_A}{point_D}={point_A}{point_B}={len_c}$. Find the explicit expression for the distancebetween points ${point_P}$ and ${point_D}$.",
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
    f.write(json.dumps({json_data["id"]: f"aops_96_ahsme_9({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_P}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
