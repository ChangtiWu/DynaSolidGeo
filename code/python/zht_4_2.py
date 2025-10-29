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
point_A, point_B, point_C, point_D, point_E, point_A_prime = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate():
    """
    计算直线 A'C 与平面 A'DE 的夹角正弦值的最大值

    返回:
    float: 正弦值
    """
    # 结果已知
    return math.sqrt(3) - 1


# 题干给定的数值
len_a = 4.0            # 菱形边长
angle_BAD = math.pi/3   # ∠BAD
# E 为 AB 中点
# 折起得到四棱锥 A'-BCDE
# 二面角 θ ∈ [π/4, 3π/4]

# 验证输出
# result = calculate()
# print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "zht_4_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"已知菱形 {point_A}{point_B}{point_C}{point_D} 的边长为 {len_a}，∠{point_B}{point_A}{point_D} = π/3，{point_E} 为 {point_A}{point_B} 的中点。将 △{point_A}{point_D}{point_E} 沿 {point_D}{point_E} 折起，使点 {point_A} 到达点 {point_A_prime} 的位置，连接 {point_A_prime}{point_B}、{point_A_prime}{point_C}，得到四棱锥 {point_A_prime}-{point_B}{point_C}{point_D}{point_E}。设二面角 {point_A_prime}-{point_D}{point_E}-{point_B} 的平面角为  arg_theta （ arg_theta  ∈ [π/4, 3π/4]），求直线 {point_A_prime}{point_C} 与平面 {point_A_prime}{point_D}{point_E} 的夹角的正弦值的最大值。",
    "en_problem": f"Given a rhombus {point_A}{point_B}{point_C}{point_D} with side length {len_a}, ∠{point_B}{point_A}{point_D} = π/3, {point_E} is the midpoint of {point_A}{point_B}. Fold △{point_A}{point_D}{point_E} along {point_D}{point_E} so that point {point_A} moves to position {point_A_prime}, connect {point_A_prime}{point_B}, {point_A_prime}{point_C} to form a quadrangular pyramid {point_A_prime}-{point_B}{point_C}{point_D}{point_E}. Let the dihedral angle {point_A_prime}-{point_D}{point_E}-{point_B} be  arg_theta  ( arg_theta  ∈ [π/4, 3π/4]), find the maximum value of the sine of the angle between line {point_A_prime}{point_C} and plane {point_A_prime}{point_D}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"zht_4_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_A_prime}')"}, ensure_ascii=False) + "\n")
