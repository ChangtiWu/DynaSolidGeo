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
point_A, point_B, point_C, point_D, point_E, point_A1 = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_a):
    """
    计算四棱锥 A'-BCED 的表面积

    参数:
    len_a (float): 正三角形边长 a

    返回:
    float: 表面积
    """
    # 根据题干给出的解答公式: (len_a^2 * (2 + sqrt(3))) / 4
    return (len_a ** 2 * (2 + math.sqrt(3))) / 4


# 定义题干中的参数变量
len_a = 2.0  # 正三角形边长 = 2

# 验证计算结果（确认与参考答案一致后注释掉）
#result = calculate(len_a)
#print(f"计算结果: {result:.6f}")


# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_10_2",
    "type": 8,
    "level": 2,
    "cn_problem": f"设正△{point_A}{point_B}{point_C}的边长为{len_a}，{point_D}，{point_E}分别是边{point_A}{point_B}，{point_A}{point_C}的中点，现沿着{point_D}{point_E}将△{point_A}{point_D}{point_E}折起，得到四棱锥{point_A1}-{point_B}{point_C}{point_E}{point_D}。若{point_A1}{point_B} = (√2/2){len_a}，求四棱锥{point_A1}-{point_B}{point_C}{point_E}{point_D}的表面积。",
    "en_problem": f"Let equilateral triangle {point_A}{point_B}{point_C} have side length {len_a}, {point_D}, {point_E} are midpoints of sides {point_A}{point_B}, {point_A}{point_C} respectively. Fold triangle {point_A}{point_D}{point_E} along {point_D}{point_E} to form pyramid {point_A1}-{point_B}{point_C}{point_E}{point_D}. If {point_A1}{point_B} = (√2/2){len_a}, find the surface area of pyramid {point_A1}-{point_B}{point_C}{point_E}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_10_2({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_A1}')"}, ensure_ascii=False) + "\n")
