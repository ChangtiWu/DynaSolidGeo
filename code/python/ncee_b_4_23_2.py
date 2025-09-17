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
len_scaling_factor = round(random.uniform(0.1, 10.0), 1)

# Generate random point names
point_P, point_A, point_B, point_C, point_D, point_E, point_F = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_t, val_v, len_p):
    """
    计算方程 $x = \sqrt{\dfrac{9\text{len\_t}^2 \pm \sqrt{81\text{len\_t}^4 - \dfrac{11664\text{val\_v}^2}{49(\text{len\_p}^2 - \text{len\_t}^2)}}}{2}}$ 的实解。

    参数:
        len_t (float): 长度参数（需满足 $\text{len\_p}^2 \neq \text{len\_t}^2$）。
        val_v (float): 数值参数（影响根号内条件）。
        len_p (float): 长度参数（需满足 $\text{len\_p}^2 \neq \text{len\_t}^2$）。

    返回:
        tuple: 包含两个实解的元组 $(x_+, x_-)$，分别对应±号的解。

    异常:
        ValueError: 若 $\text{len\_p}^2 = \text{len\_t}^2$（分母为零）或无实解（根号内为负）。
    """
    # 检查分母是否为零（len_p² - len_t² ≠ 0）
    denominator = 49 * (len_p ** 2 - len_t ** 2)
    if denominator == 0:
        raise ValueError("分母为零：len_p² 不能等于 len_t²")

    # 计算实解条件：81len_t⁴ ≥ 11664val_v²/(49(len_p² - len_t²))
    left_side = 81 * (len_t ** 4)
    right_side = (11664 * (val_v ** 2)) / denominator
    if left_side < right_side:
        raise ValueError("无实解：81len_t⁴ < 11664val_v²/(49(len_p² - len_t²))")

    # 计算内部平方根项
    inside_sqrt = math.sqrt(left_side - right_side)

    # 计算分子的两种情况（±号）
    numerator_plus = 9 * (len_t ** 2) + inside_sqrt
    numerator_minus = 9 * (len_t ** 2) - inside_sqrt

    # 计算两个实解（确保分子非负，因条件已保证）
    x_plus = math.sqrt(numerator_plus / 2)
    x_minus = math.sqrt(numerator_minus / 2)

    return x_plus, x_minus

len_t = 2
val_v = 7
len_p = 4

# x_plus, x_minus = calculate(len_t, val_v, len_p)
# print(f"x₊ = {x_plus:.4f}, x₋ = {x_minus:.4f}")
# Generate random lengths
len_t = round(len_scaling_factor * float(len_t), 2)
len_p = round(len_scaling_factor * float(len_p), 2)
val_v = round((len_scaling_factor**3) * float(val_v), 2)

# Calculate the result
result = calculate(len_t, val_v, len_p)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_23_2",
    "type": 3,
    "level": 3,
    "cn_problem": f"在三棱锥 {point_P}-{point_A}{point_B}{point_C} 中：\n- 平面 {point_P}{point_A}{point_C} ⟂ 平面 {point_A}{point_B}{point_C}，且 ∠{point_A}{point_B}{point_C}=π/2；\n- 设 {point_D}、{point_E} 在线段 {point_A}{point_C} 上，满足 {point_A}{point_D}={point_D}{point_E}={point_E}{point_C}={len_t}（{len_t}>0）；\n- {point_P}{point_D}={point_P}{point_C}={len_p}（{len_p}>{len_t}）；\n- 取 {point_F} 于 {point_A}{point_B}，满足 {point_E}{point_F} ∥ {point_B}{point_C}。\n若四棱锥 {point_P}-{point_D}{point_F}{point_B}{point_C} 的体积为 {val_v}（{val_v}>0），求棱长 {point_B}{point_C}。",
    "en_problem": f"In tetrahedron {point_P}-{point_A}{point_B}{point_C}:\n- Plane {point_P}{point_A}{point_C} is perpendicular to plane {point_A}{point_B}{point_C}, and ∠{point_A}{point_B}{point_C}=π/2.\n- Points {point_D}, {point_E} lie on {point_A}{point_C} with {point_A}{point_D}={point_D}{point_E}={point_E}{point_C}={len_t} ({len_t}>0).\n- {point_P}{point_D}={point_P}{point_C}={len_p} ({len_p}>{len_t}).\n- Point {point_F} lies on {point_A}{point_B} such that {point_E}{point_F} ∥ {point_B}{point_C}.\nIf the volume of quadrilateral pyramid {point_P}-{point_D}{point_F}{point_B}{point_C} equals {val_v} ({val_v}>0), find {point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_23_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
