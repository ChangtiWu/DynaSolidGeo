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
point_A, point_B, point_C, point_D, point_A_prime, point_B_prime, point_C_prime, point_D_prime = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
import math


def calculate(len_a, len_b, len_c, arg_alpha, arg_beta, arg_gamma):
    """
    计算给定的几何表达式

    参数:
    len_a (float): AB 的长度
    len_b (float): AD 的长度
    len_c (float): AA' 的长度
    arg_alpha (float): ∠BAD （弧度制）
    arg_beta (float): ∠BAA' （弧度制）
    arg_gamma (float): ∠DAA' （弧度制）

    返回:
    float: 计算结果
    """
    result = math.sqrt(
        len_a ** 2
        + len_b ** 2
        + len_c ** 2
        + 2 * (
            len_a * len_b * math.cos(arg_alpha)
            + len_a * len_c * math.cos(arg_beta)
            + len_b * len_c * math.cos(arg_gamma)
        )
    )
    return result


# 定义题干参数
len_a = 4.0
len_b = 3.0
len_c = 3.0
arg_alpha = math.radians(90)
arg_beta = math.radians(60)
arg_gamma = math.radians(60)

# 验证输出（与参考答案对比）
#result = calculate(len_a, len_b, len_c, arg_alpha, arg_beta, arg_gamma)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c, arg_alpha, arg_beta, arg_gamma)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "sup_8",
    "type": 3,
    "level": 1,
    "cn_problem": f"设平行六面体{point_A}{point_B}{point_C}{point_D}-{point_A_prime}{point_B_prime}{point_C_prime}{point_D_prime}中，棱{point_A}{point_B}={len_a}，{point_A}{point_D}={len_b}，侧棱{point_A}{point_A_prime}={len_c}，夹角满足∠{point_B}{point_A}{point_D}={arg_alpha}，∠{point_B}{point_A}{point_A_prime}={arg_beta}，∠{point_D}{point_A}{point_A_prime}={arg_gamma}。求体对角线{point_A}{point_C_prime}的长度。",
    "en_problem": f"In parallelepiped {point_A}{point_B}{point_C}{point_D}-{point_A_prime}{point_B_prime}{point_C_prime}{point_D_prime}, let edge {point_A}{point_B}={len_a}, {point_A}{point_D}={len_b}, lateral edge {point_A}{point_A_prime}={len_c}, with angles ∠{point_B}{point_A}{point_D}={arg_alpha}, ∠{point_B}{point_A}{point_A_prime}={arg_beta}, ∠{point_D}{point_A}{point_A_prime}={arg_gamma}. Find the length of body diagonal {point_A}{point_C_prime}.",
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
    f.write(json.dumps({json_data["id"]: f"sup_8({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A_prime}', '{point_B_prime}', '{point_C_prime}', '{point_D_prime}')"}, ensure_ascii=False) + "\n")
