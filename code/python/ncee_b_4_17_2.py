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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_P, point_O1, point_O = random.sample(string.ascii_uppercase, 11)

# Add result calculation code
import math


def calculate(len_a, len_h, param_k, len_l):
    """
    计算四棱锥的体积、最大高度和最大体积。

    参数:
        len_a (float): 底面边长AB的长度。
        len_h (float): 四棱锥的高。
        param_k (float): 形状参数。
        len_l (float): 与最大高度相关的基准长度。

    返回:
        tuple: 包含三个浮点数的元组 (V, len_h_max, V_max)，分别对应体积、最大高度、最大体积。
    """
    # 计算体积 V
    V = ((3 * param_k + 1) / 3) * (len_a ** 2) * len_h

    # 计算最大高度 len_h_max
    len_h_max = len_l / math.sqrt(3)

    # 计算最大体积 V_max
    V_max = (4 * (3 * param_k + 1) / (9 * math.sqrt(3))) * (len_l ** 3)

    return len_h_max

len_a = 6.0
len_h = 2
param_k = 4
len_l = 6

# len_h_max = calculate(len_a, len_h, param_k, len_l)
#
# print(f"最大高度 len_h_max = {len_h_max:.4f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)
len_l = round(len_scaling_factor * float(len_l), 2)

# Calculate the result
result = calculate(len_a, len_h, param_k, len_l)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_17_2",
    "type": 3,
    "level": 2,
    "cn_problem": f"设要建造一座仓库，由上下两部分组成：下部为正四棱柱 {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}，底面 {point_A}{point_B}{point_C}{point_D} 为边长为 {len_a}（{len_a}>0）的正方形；上部为正四棱锥 {point_P}-{point_A1}{point_B1}{point_C1}{point_D1}，顶点为 {point_P}，底面与正四棱柱的上底重合。记 {len_h}={point_P}{point_O1}（正四棱锥的高），{point_O}{point_O1}={param_k}*{len_h}（正四棱柱的高与锥高之比），其中 {point_O}、{point_O1} 分别为底面、上底的几何中心。（2）已知正四棱锥的侧棱长为 {len_l}（{len_l}>0），且比例系数 {param_k} 固定，试确定应取的锥高使仓库体积最大。",
    "en_problem": f"Design a warehouse consisting of two parts: the lower part is a square prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} with square base {point_A}{point_B}{point_C}{point_D} of side length {len_a} ({len_a}>0); the upper part is a square pyramid {point_P}-{point_A1}{point_B1}{point_C1}{point_D1} with apex {point_P}, whose base coincides with the upper base of the prism. Let {len_h}={point_P}{point_O1} (height of the square pyramid), {point_O}{point_O1}={param_k}*{len_h} (ratio of prism height to pyramid height), where {point_O}, {point_O1} are the geometric centers of the lower and upper bases respectively. (2) Given that the lateral edge length of the square pyramid is {len_l} ({len_l}>0) and ratio coefficient {param_k} is fixed, determine the pyramid height that maximizes the warehouse volume.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_17_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_P}', '{point_O1}', '{point_O}')"}, ensure_ascii=False) + "\n")
