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
point_A, point_B, point_C, point_D, point_E, point_P = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算三棱锥 P-CDE 外接球的体积

    参数:
    len_a (float): 等腰梯形底边 CD 的长度

    返回:
    float: 外接球体积
    """
    return (math.sqrt(6) * math.pi * len_a**3) / 8


# 题干给定的数值
len_a = 1.0  # CD 边长（AB = 2CD = 2）

# 验证输出
# volume = calculate(len_a)
# print(f"外接球体积: {volume:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_11_12",
    "type": 8,
    "level": 2,
    "cn_problem": f"在等腰梯形{point_A}{point_B}{point_C}{point_D}中，{point_A}{point_B} = 2*{len_a}，{point_C}{point_D} = {len_a}，∠{point_D}{point_A}{point_B} = 60°，{point_E}为{point_A}{point_B}的中点。将△{point_A}{point_D}{point_E}和△{point_B}{point_C}{point_E}分别沿{point_D}{point_E}、{point_C}{point_E}折起，使{point_A}、{point_B}重合于点{point_P}，求三棱锥{point_P}—{point_C}{point_D}{point_E}的外接球的体积。",
    "en_problem": f"In isosceles trapezoid {point_A}{point_B}{point_C}{point_D}, {point_A}{point_B} = 2*{len_a}, {point_C}{point_D} = {len_a}, ∠{point_D}{point_A}{point_B} = 60°, and {point_E} is the midpoint of {point_A}{point_B}. Triangles {point_A}{point_D}{point_E} and {point_B}{point_C}{point_E} are folded along {point_D}{point_E} and {point_C}{point_E} respectively, so that {point_A} and {point_B} coincide at point {point_P}. Find the volume of the circumsphere of triangular pyramid {point_P}—{point_C}{point_D}{point_E}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_11_12({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_P}')"}, ensure_ascii=False) + "\n")
