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
point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math


def calculate(len_m, len_n, arg_theta):
    """
    计算给定的几何表达式

    参数:
    len_m (float): AB 与 CD 的长度
    len_n (float): AC 的长度
    arg_theta (float): 折起后 AB 与 CD 的夹角（弧度制）

    返回:
    tuple: 计算结果的两种可能情况 (带 ± 号)
    """
    # 计算 BD 的两种情况
    result_plus = math.sqrt(2 * (len_m ** 2) + (len_n ** 2) + 2 * (len_m ** 2) * math.cos(arg_theta))
    result_minus = math.sqrt(2 * (len_m ** 2) + (len_n ** 2) - 2 * (len_m ** 2) * math.cos(arg_theta))
    return result_minus


# 定义题干参数
len_m = 1.0
len_n = 1.0
arg_theta = math.radians(60)

# 验证输出（与参考答案对比）
#results = calculate(len_m, len_n, arg_theta)
#print(f"计算结果(两种情况): {results[0]:.6f}, {results[1]:.6f}")

# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)
len_n = round(len_scaling_factor * float(len_n), 2)

# Calculate the result
result = calculate(len_m, len_n, arg_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_5",
    "type": 3,
    "level": 1,
    "cn_problem": f"在平行四边形{point_A}{point_B}{point_C}{point_D}中，设{point_A}{point_B}={point_C}{point_D}={len_m}，{point_A}{point_C}={len_n}，且∠{point_A}{point_C}{point_D}=90°。将四边形沿对角线{point_A}{point_C}折起，使{point_A}{point_B}与{point_C}{point_D}成{arg_theta}角，求{point_B}，{point_D}间的距离。",
    "en_problem": f"In parallelogram {point_A}{point_B}{point_C}{point_D}, let {point_A}{point_B}={point_C}{point_D}={len_m}, {point_A}{point_C}={len_n}, and ∠{point_A}{point_C}{point_D}=90°. Fold the quadrilateral along diagonal {point_A}{point_C} so that {point_A}{point_B} and {point_C}{point_D} form angle {arg_theta}. Find the distance between {point_B} and {point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"sup_5({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
