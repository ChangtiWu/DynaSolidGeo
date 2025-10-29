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
point_V, point_A, point_B, point_C, point_E, point_F = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_l: float, arg_alpha: float) -> float:
    """
    题意：正三棱锥 V-ABC，侧棱 VA, VB, VC 两两夹角均为 arg_alpha（度），侧棱长度均为 len_l。
         过点 A 作截面 AEF，E∈VB, F∈VC，求三角形 AEF 的周长最小值。

    推导要点（展开 + 等腰三角形 + 余弦定理）：
    1) 将三侧面沿 VA 展开，A 在展开后对应到 A'，有 ∠AVA' = 3*arg_alpha（度）。
    2) 在等腰三角形 ΔVAA' 中，VA = VA' = len_l，夹角为 3*arg_alpha。
       设底边 AA' 的长度为 L，则周长最小值 P_min = AA' = L。
    3) 由余弦定理：L^2 = len_l^2 + len_l^2 - 2*len_l^2*cos(3*arg_alpha)
                   = 2*len_l^2*(1 - cos(3*arg_alpha))
       注意角度需转弧度后再取 cos。

    参数:
        len_l (float): 侧棱长（>0）
        arg_alpha (float): 侧棱夹角（度制，要求 3*arg_alpha < 180）

    返回:
        float: 截面 △AEF 的最小周长
    """
    if len_l <= 0:
        raise ValueError("len_l 必须为正数。")
    if 3 * arg_alpha >= 180 or arg_alpha <= 0:
        raise ValueError("需满足 0 < arg_alpha 且 3*arg_alpha < 180（度）。")

    # 计算 3α（弧度）
    triple_alpha_rad = math.radians(3.0 * arg_alpha)

    # 余弦定理计算 AA'（即最小周长）
    # L^2 = 2*l^2*(1 - cos(3α))
    L_squared = 2.0 * (len_l ** 2) * (1.0 - math.cos(triple_alpha_rad))
    L = math.sqrt(L_squared)

    return L


# =========================
# 题干参数定义（端点变量不需要定义）
# =========================
# 侧棱长 2√3，侧棱夹角 40°
len_l = 2.0 * math.sqrt(3.0)
arg_alpha = 40.0  # 单位：度

# =========================
# 验证与输出（验证通过后按流程应注释）
# =========================
#result = calculate(len_l=len_l, arg_alpha=arg_alpha)
    # # 结论公式：P_min = 2 * len_l * sin(3α/2)
#expected_formula = 2.0 * len_l * math.sin(math.radians(1.5 * arg_alpha * 2))  # 等价于 2*l*sin(3α/2)
    # # 题干具体数值下，参考答案应为 6
#expected_numeric = 6.0
#print(f"最小周长(余弦定理推导) = {result:.10f}")
#print(f"对照(结论公式 2*l*sin(3α/2)) = {expected_formula:.10f}")
#print("与结论公式是否一致：",
#math.isclose(result, expected_formula, rel_tol=1e-12, abs_tol=1e-12))
#print("与题干具体数值的参考答案 6 是否一致：",
#math.isclose(result, expected_numeric, rel_tol=1e-12, abs_tol=1e-12))

# Generate random lengths
len_l = round(len_scaling_factor * float(len_l), 2)

# Calculate the result
result = calculate(len_l, arg_alpha)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_5_12",
    "type": 3,
    "level": 2,
    "cn_problem": f"在侧棱长为{len_l}的正三棱锥{point_V}-{point_A}{point_B}{point_C}中，若侧棱间的夹角满足∠{point_A}{point_V}{point_B} = ∠{point_B}{point_V}{point_C} = ∠{point_C}{point_V}{point_A} = {arg_alpha}°（其中3*{arg_alpha}° < 180°），过点{point_A}作截面{point_A}{point_E}{point_F}与侧棱{point_V}{point_B}、{point_V}{point_C}分别交于{point_E}、{point_F}，求截面△{point_A}{point_E}{point_F}的周长的最小值。",
    "en_problem": f"In a regular triangular pyramid {point_V}-{point_A}{point_B}{point_C} with lateral edge length {len_l}, where the angles between lateral edges satisfy ∠{point_A}{point_V}{point_B} = ∠{point_B}{point_V}{point_C} = ∠{point_C}{point_V}{point_A} = {arg_alpha}° (with 3*{arg_alpha}° < 180°), and a plane through point {point_A} intersects lateral edges {point_V}{point_B} and {point_V}{point_C} at points {point_E} and {point_F} respectively, find the minimum perimeter of triangle {point_A}{point_E}{point_F}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_5_12({mode}, {azimuth}, {elevation}, '{point_V}', '{point_A}', '{point_B}', '{point_C}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
