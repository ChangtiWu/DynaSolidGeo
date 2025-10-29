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

# Add result calculation code
import math

def calculate(len_H, len_R):
    """
    计算圆锥内接圆柱的最大全面积及对应底面半径

    参数:
    len_H (float): 圆锥高
    len_R (float): 圆锥底面半径

    返回:
    tuple: (圆柱底面半径 len_x, 最大全面积 S_max)
    """
    # 最优圆柱底面半径
    len_x = (len_H * len_R) / (2 * (len_H - len_R))
    # 最大全面积
    S_max = math.pi * (len_H ** 2) * len_R / (2 * (len_H - len_R))
    return S_max


# 定义题干中的参数
len_H = 3.0   # 圆锥高
len_R = 1.0   # 圆锥底面半径

# 验证计算结果
#result_x, result_S = calculate(len_H, len_R)
#print(f"最优底面半径: {result_x:.6f}, 最大全面积: {result_S:.6f}")

# Generate random lengths
len_R = round(len_scaling_factor * float(len_R), 2)
len_H = round(len_scaling_factor * float(len_H), 2)


# Calculate the result
result = calculate(len_H, len_R)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_11_3",
    "type": 4,
    "level": 2,
    "cn_problem": f"已知圆锥的底面半径为 {len_R}，高为 {len_H}（{len_H} > {len_R} > 0），圆锥内有一个底面半径为 len_x 的内接圆柱。求：圆柱的最大全面积为多少？",
    "en_problem": f"Given a cone with base radius {len_R} and height {len_H} (where {len_H} > {len_R} > 0), and an inscribed cylinder with base radius len_x. Find: What is the maximum total surface area of the cylinder?",
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
    f.write(json.dumps({json_data["id"]: f"area2_11_3({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
