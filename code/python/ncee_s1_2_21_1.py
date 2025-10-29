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
point_O, point_E, point_F, point_G, point_H, point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1 = random.sample(string.ascii_uppercase, 13)

# Add result calculation code
def calculate(len_rho, len_a, len_h):
    """计算质量（公式：11*len_rho*len_a²*len_h / 12）"""
    return (11 * len_rho * (len_a ** 2) * len_h) / 12


# 测试示例
len_rho = 0.9
len_a = 6.0
len_h = 4.0

# print(calculate(len_rho, len_a, len_h))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)
len_rho = round(len_scaling_factor * float(len_rho), 2)

# Calculate the result
result = calculate(len_rho, len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_s1_2_21_1",
    "type": 5,
    "level": 1,
    "cn_problem": f"利用3D打印技术制作模型。该模型为长方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}挖去四棱锥{point_O}-{point_E}{point_F}{point_G}{point_H}后所得的几何体，其中{point_O}为长方体的中心，{point_E},{point_F},{point_G},{point_H}分别为所在棱的中点。设{point_A}{point_B}={point_B}{point_C}={len_a}，{point_A}{point_A1}={len_h}，3D打印所用原料密度为{len_rho}。求制作该模型所需原料的质量。",
    "en_problem": f"A 3D printing model is created. The model is a geometric body obtained by removing a quadrilateral pyramid {point_O}-{point_E}{point_F}{point_G}{point_H} from a rectangular prism {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}, where {point_O} is the center of the prism and {point_E},{point_F},{point_G},{point_H} are the midpoints of the respective edges. Given {point_A}{point_B}={point_B}{point_C}={len_a}, {point_A}{point_A1}={len_h}, and the 3D printing material density is {len_rho}. Find the mass of material needed to create this model.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_s1_2_21_1({mode}, {azimuth}, {elevation}, '{point_O}', '{point_E}', '{point_F}', '{point_G}', '{point_H}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}')"}, ensure_ascii=False) + "\n")
