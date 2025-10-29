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
point_M, point_A = random.sample(string.ascii_uppercase, 2)

# Add result calculation code
import math

def calculate(len_r1, len_r2, len_s):
    """
    计算圆台上底面圆周上的点到绳子的最短距离

    参数:
    len_r1 (float): 上底半径
    len_r2 (float): 下底半径 (len_r2 > len_r1)
    len_s (float): 侧母线长（斜高）

    返回:
    float: 最短距离
    """
    k = len_s / (len_r2 - len_r1)  # 相当于前面版本里的比例系数

    numerator = (len_r2 * (len_r1 + len_r2) / 2) * math.sin(2 * math.pi / k)
    denominator = math.sqrt(
        len_r2**2 +
        ((len_r1 + len_r2)**2) / 4 -
        len_r2 * (len_r1 + len_r2) * math.cos(2 * math.pi / k)
    )
    return k * (numerator / denominator - len_r1)


# ====== 验证题目给的数据 ======
len_r1 = 5.0   # 上底半径
len_r2 = 10.0  # 下底半径
len_s = 20.0   # 母线



# Generate random lengths
len_r1 = round(len_scaling_factor * float(len_r1), 2)
len_r2 = round(len_scaling_factor * float(len_r2), 2)
len_s = round(len_scaling_factor * float(len_s), 2)

# Calculate the result
result = calculate(len_r1, len_r2, len_s)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fp_10_2",
    "type": 3,
    "level": 1,
    "cn_problem": f"设圆台的上、下底半径分别为{len_r1}（上）与{len_r2}（下），{len_r2} > {len_r1}，侧母线（上缘到下缘的斜高）为{len_s}。取母线中点{point_M}，从{point_M}拉绳子绕圆台侧面到点{point_A}。求上底面圆周上的点到绳子的最短距离。",
    "en_problem": f"Let a frustum have upper and lower base radii {len_r1} (upper) and {len_r2} (lower) respectively, with {len_r2} > {len_r1}, and lateral generatrix (slant height from upper edge to lower edge) {len_s}. Take the midpoint {point_M} of the generatrix, and draw a rope from {point_M} around the lateral surface of the frustum to point {point_A}. Find the shortest distance from points on the upper base circle to the rope.",
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
    f.write(json.dumps({json_data["id"]: f"fp_10_2({mode}, {azimuth}, {elevation}, '{point_M}', '{point_A}')"}, ensure_ascii=False) + "\n")
