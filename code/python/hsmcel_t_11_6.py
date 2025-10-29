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
point_A, point_B, point_C, point_M = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math

def calculate(len_b, len_d):
    """
    计算三棱锥 A-BCM 的体积

    参数:
    len_b (float): AC 边长
    len_d (float): 折起后 AB 的长度

    返回:
    float: 三棱锥体积
    """
    return (len_b**2 * len_d) / 12


# 题干给定的数值
len_b = 2.0     # AC
arg_theta = math.radians(30)  # ∠B = 30°
len_d = 2 * math.sqrt(2)  # AB 折起后的长度

# 验证输出
#volume = calculate(len_b, len_d)
#print(f"三棱锥体积: {volume:.6f}")

# Generate random lengths
len_b = round(len_scaling_factor * float(len_b), 2)
len_d = round(len_scaling_factor * float(len_d), 2)

# Calculate the result
result = calculate(len_b, len_d)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_11_6",
    "type": 8,
    "level": 2,
    "cn_problem": f"在△{point_A}{point_B}{point_C}中，∠{point_C} = 90°，∠{point_B} = {arg_theta}，{point_A}{point_C} = {len_b}，{point_M}是{point_A}{point_B}的中点。将△{point_A}{point_C}{point_M}沿{point_C}{point_M}折起，使{point_A}、{point_B}两点间的距离为{len_d}，求此时三棱锥{point_A}—{point_B}{point_C}{point_M}的体积。",
    "en_problem": f"In triangle {point_A}{point_B}{point_C}, ∠{point_C} = 90°, ∠{point_B} = {arg_theta}, {point_A}{point_C} = {len_b}, and {point_M} is the midpoint of {point_A}{point_B}. Triangle {point_A}{point_C}{point_M} is folded along {point_C}{point_M}, making the distance between points {point_A} and {point_B} equal to {len_d}. Find the volume of the triangular pyramid {point_A}—{point_B}{point_C}{point_M}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_11_6({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_M}')"}, ensure_ascii=False) + "\n")
