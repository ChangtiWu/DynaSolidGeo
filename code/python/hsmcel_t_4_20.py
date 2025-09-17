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
point_P, point_A, point_B, point_C, point_H = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import numpy as np

def calculate(len_u: np.ndarray, len_v: np.ndarray, len_w: np.ndarray) -> np.ndarray:
    """
    计算向量 PH：
        PH = ( |v|^2|w|^2 * u + |u|^2|w|^2 * v + |u|^2|v|^2 * w )
             / ( |u|^2|v|^2 + |u|^2|w|^2 + |v|^2|w|^2 )

    参数:
        len_u: 向量 PA（与 len_v、len_w 两两垂直）
        len_v: 向量 PB（与 len_u、len_w 两两垂直）
        len_w: 向量 PC（与 len_u、len_v 两两垂直）

    返回:
        向量 PH（np.ndarray, 形如 [x, y, z]）
    """
    su = float(len_u @ len_u)  # |u|^2
    sv = float(len_v @ len_v)  # |v|^2
    sw = float(len_w @ len_w)  # |w|^2

    denom = su * sv + su * sw + sv * sw
    if denom == 0.0:
        raise ValueError("非法输入：|u|^2|v|^2 + |u|^2|w|^2 + |v|^2|w|^2 不能为 0")

    numer = (sv * sw) * len_u + (su * sw) * len_v + (su * sv) * len_w
    return numer / denom


# =========================
# 题干参数变量定义（端点变量不定义）
# 注意：这里赋值为一组“彼此正交”的示例向量，便于本地自检。
# 若有原题数值，请在此处替换为题干给定的原始数值。
# =========================
# 向量 PA = len_u，PB = len_v，PC = len_w（两两垂直）
len_u = np.array([3.0, 0.0, 0.0])  # 示例：长度为 3 的 x 轴向量
len_v = np.array([0.0, 4.0, 0.0])  # 示例：长度为 4 的 y 轴向量
len_w = np.array([0.0, 0.0, 5.0])  # 示例：长度为 5 的 z 轴向量

# =========================
# 运行与校验（验证通过后按流程需注释掉）
# =========================
# result = calculate(len_u=len_u, len_v=len_v, len_w=len_w)
# print("PH 向量 =", result)
#
# ---- 可选自检：检验 PH ⟂ AB 与 PH ⟂ BC ----
# AB = PB - PA = len_v - len_u
# BC = PC - PB = len_w - len_v
# AB = len_v - len_u
# BC = len_w - len_v
# print("PH·AB =", float(result @ (len_v - len_u)))
# print("PH·BC =", float(result @ (len_w - len_v)))

# Generate random lengths
len_u = np.round(len_scaling_factor * len_u, 2)
len_v = np.round(len_scaling_factor * len_v, 2)
len_w = np.round(len_scaling_factor * len_w, 2)

# Calculate the result
result = calculate(len_u, len_v, len_w)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_4_20",
    "type": 3,
    "level": 2,
    "cn_problem": f"设点{point_P}为三角形{point_A}{point_B}{point_C}所在平面外一点，向量vector_PA = {len_u}，vector_PB = {len_v}，vector_PC = {len_w}，且{len_u}、{len_v}、{len_w}两两垂直，{point_H}为三角形{point_A}{point_B}{point_C}的垂心。求vector_PH。",
    "en_problem": f"Let point {point_P} be a point outside the plane of triangle {point_A}{point_B}{point_C}, with vectors vector_PA = {len_u}, vector_PB = {len_v}, vector_PC = {len_w}, where {len_u}, {len_v}, {len_w} are mutually perpendicular. Let {point_H} be the orthocenter of triangle {point_A}{point_B}{point_C}. Express vector vector_PH in terms of {len_u}, {len_v}, {len_w}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_4_20({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_H}')"}, ensure_ascii=False) + "\n")
