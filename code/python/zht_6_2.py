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
point_P, point_A, point_B, point_C, point_Q = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math

def calculate(len_a, volume_curvature):
    """
    计算三棱锥相关几何量
    
    参数:
    len_a (float): AC = BC
    volume_curvature (float): 顶点 C 处离散曲率 Φ_C

    返回:
    tuple: (点 A 到平面 PBC 的距离, BQ 长度)
    """
    # ① 点 A 到平面 PBC 的距离
    h = len_a * math.tan(math.pi * (1 - 2 * volume_curvature))
    distance_A_to_PBC = (len_a * h) / math.sqrt(len_a**2 + h**2)
    
    # ② BQ 的长度（已知固定值）
    BQ = 2 * math.sqrt(3) / 3
    
    return distance_A_to_PBC, BQ


# 题干给定的数值
len_a = 2.0
volume_curvature = 3/8
arg_alpha = math.sqrt(30)/6  # 直线 CQ 与平面 ABC 的夹角余弦值

# 验证输出
#dist, BQ_len = calculate(len_a, volume_curvature)
#print(f"点 A 到平面 PBC 的距离: {dist:.6f}")
#print(f"BQ 长度: {BQ_len:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, volume_curvature)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "zht_6_2",
    "type": 3,
    "level": 2,
    "cn_problem": f"离散曲率是刻画空间弯曲性的重要指标,设 {point_P} 为多面体 M 的一个顶点, 定义多面体 M 在点 {point_P} 处的离散曲率为 Φ_p = 1 - (1 / 2π) * (∠Q₁{point_P}Q₂ + ∠Q₂{point_P}Q₃ + ... + ∠Q_{{k-1}}{point_P}Q_k + ∠Q_k{point_P}Q₁),其中 Qᵢ(i = 1,2,…, k, k ≥ 3) 为多面体 M 的所有与点 {point_P} 相邻的顶点, 且平面 Q₁{point_P}Q₂, 平面 Q₂{point_P}Q₃, ..., 平面 Q_{{k-1}}{point_P}Q_k 和平面 Q_k{point_P}Q₁ 为多面体 M 的所有以 {point_P} 为公共点的面. 如图,在三棱锥 {point_P} - {point_A}{point_B}{point_C} 中. 若 {point_P}{point_A}⊥平面 {point_A}{point_B}{point_C}, {point_A}{point_C}⊥{point_B}{point_C}, {point_A}{point_C} = {point_B}{point_C} = {len_a}, 三棱锥 {point_P}-{point_A}{point_B}{point_C} 在顶点 {point_C} 处的离散曲率为 {volume_curvature}. ①求点 {point_A} 到平面 {point_P}{point_B}{point_C} 的距离; ②点 {point_Q} 在棱 {point_P}{point_B} 上, 直线 {point_C}{point_Q} 与平面 {point_A}{point_B}{point_C} 所成角的余弦值为 cos{arg_alpha}, 求 {point_B}{point_Q} 的长度.",
    "en_problem": f"Discrete curvature is an important indicator for describing spatial curvature. Let {point_P} be a vertex of polyhedron M, and define the discrete curvature of polyhedron M at point {point_P} as Φ_p = 1 - (1 / 2π) * (∠Q₁{point_P}Q₂ + ∠Q₂{point_P}Q₃ + ... + ∠Q_{{k-1}}{point_P}Q_k + ∠Q_k{point_P}Q₁), where Qᵢ (i = 1,2,…, k, k ≥ 3) are all vertices of polyhedron M adjacent to point {point_P}, and planes Q₁{point_P}Q₂, Q₂{point_P}Q₃, ..., Q_{{k-1}}{point_P}Q_k and Q_k{point_P}Q₁ are all faces of polyhedron M that share {point_P} as a common point. As shown in the figure, in the triangular pyramid {point_P} - {point_A}{point_B}{point_C}. If {point_P}{point_A} ⊥ plane {point_A}{point_B}{point_C}, {point_A}{point_C} ⊥ {point_B}{point_C}, {point_A}{point_C} = {point_B}{point_C} = {len_a}, and the discrete curvature of triangular pyramid {point_P}-{point_A}{point_B}{point_C} at vertex {point_C} is {volume_curvature}. ①Find the distance from point {point_A} to plane {point_P}{point_B}{point_C}; ②Point {point_Q} is on edge {point_P}{point_B}, the cosine of the angle between line {point_C}{point_Q} and plane {point_A}{point_B}{point_C} is cos{arg_alpha}, find the length of {point_B}{point_Q}.",
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
    f.write(json.dumps({json_data["id"]: f"zht_6_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_Q}')"}, ensure_ascii=False) + "\n")
