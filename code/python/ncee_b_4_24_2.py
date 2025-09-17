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
point_A, point_B, point_C, point_D, point_G, point_E = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_x, ang_alpha, val_V):
    """
    Calculate the lateral surface area based on given parameters.

    Parameters:
    - len_x: Length parameter (optional)
    - ang_alpha: Angle in radians (required)
    - val_V: Volume parameter (optional)

    Returns:
    - The calculated lateral surface area

    Note: Either len_x or val_V must be provided, but not both.
    """
    if ang_alpha is None:
        raise ValueError("ang_alpha must be provided")

    # Calculate the common expression part
    cos_alpha = math.cos(ang_alpha)
    common_part = (1 - cos_alpha) / 2 + math.sqrt(1 - cos_alpha - cos_alpha ** 2)

    if len_x is not None and val_V is not None:
        raise ValueError("Provide either len_x or val_V, not both")
    elif len_x is not None:
        # First part of the equation
        S_lateral = len_x ** 2 * common_part
    elif val_V is not None:
        # Second part of the equation
        numerator = 6 * val_V
        denominator = math.sin(ang_alpha) * math.sqrt(-cos_alpha)
        S_lateral = (numerator / denominator) ** (2 / 3) * common_part
    else:
        raise ValueError("Either len_x or val_V must be provided")

    return S_lateral

len_x = 2.0
ang_alpha = math.pi / 3 * 2  # 120度
# result1 = calculate(len_x, ang_alpha)
# print(f"当len_x={len_x}, ang_alpha={ang_alpha}时, S_lateral={result1}")

# Generate random lengths
len_x = round(len_scaling_factor * float(len_x), 2)


# Calculate the result
result = calculate(len_x, ang_alpha, None)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_24_2",
    "type": 4,
    "level": 2,
    "cn_problem": f"已知菱形 {point_A}{point_B}{point_C}{point_D} 的边长为 {len_x}（{len_x}>0），顶角 ∠{point_A}{point_B}{point_C}={ang_alpha}°（90°<{ang_alpha}<180°）。\n设 {point_G} 为两条对角线的交点。空间一点 {point_E} 满足 {point_B}{point_E} ⟂ 平面 {point_A}{point_B}{point_C}{point_D}，且 {point_A}{point_E} ⟂ {point_E}{point_C}。\n已知四面体 {point_E}-{point_A}{point_C}{point_D} 的体积为 val_V（val_V>0）。求该四面体的侧面积。",
    "en_problem": f"Let {point_A}{point_B}{point_C}{point_D} be a rhombus with side length {len_x} ({len_x}>0) and vertex angle ∠{point_A}{point_B}{point_C}={ang_alpha}° where 90°<{ang_alpha}<180°. Denote {point_G} as the intersection of diagonals. A point {point_E} in space satisfies {point_B}{point_E} ⟂ plane {point_A}{point_B}{point_C}{point_D} and {point_A}{point_E} ⟂ {point_E}{point_C}. If the volume of tetrahedron {point_E}-{point_A}{point_C}{point_D} is val_V (val_V>0), find the lateral surface area of the triangular pyramid.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_24_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_G}', '{point_E}')"}, ensure_ascii=False) + "\n")
