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
point_A, point_B, point_C, point_D, point_E, point_A1, point_M, point_S, point_T = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math

def calculate(len_side, len_k):
    """
    计算 A'S / A'D 的值

    参数:
    len_side (float): 正三角形边长
    len_k (float): 面积比 S_{A'ST} / S_{A'BD}

    返回:
    float: A'S / A'D 的值
    """
    # 根据题干给出的解答公式: sqrt(2 * len_k)
    return math.sqrt(2 * len_k)


# 定义题干中的参数变量
len_side = 2.0   # 正三角形边长
len_k = 1/4      # 面积比

# 验证计算结果（确认与参考答案一致后注释掉）
#result = calculate(len_side, len_k)
#print(f"计算结果: {result:.6f}")


# Generate random lengths
len_side = round(len_scaling_factor * float(len_side), 2)

# Calculate the result
result = calculate(len_side, len_k)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz1_10_3",
    "type": 8,
    "level": 2,
    "cn_problem": f"如图，正△{point_A}{point_B}{point_C}边长为{len_side}，{point_D}, {point_E}分别是边{point_A}{point_B}, {point_A}{point_C}的中点，沿着{point_D}{point_E}将△{point_A}{point_D}{point_E}折起，得到四棱锥{point_A1}-{point_B}{point_C}{point_E}{point_D}，点{point_M}为{point_A1}{point_C}中点。过{point_M}{point_E}的平面分别与棱{point_A1}{point_D}, {point_A1}{point_B}相交于点{point_S}, {point_T}，记△{point_A1}{point_S}{point_T}与△{point_A1}{point_B}{point_D}的面积分别为S_{point_A1}{point_S}{point_T}, S_{point_A1}{point_B}{point_D}，若S_{point_A1}{point_S}{point_T}/S_{point_A1}{point_B}{point_D} = {len_k}，求{point_A1}{point_S}/{point_A1}{point_D}的值。",
    "en_problem": f"In the figure, equilateral triangle {point_A}{point_B}{point_C} has side length {len_side}, {point_D}, {point_E} are midpoints of sides {point_A}{point_B}, {point_A}{point_C} respectively. Fold triangle {point_A}{point_D}{point_E} along {point_D}{point_E} to form pyramid {point_A1}-{point_B}{point_C}{point_E}{point_D}, point {point_M} is the midpoint of {point_A1}{point_C}. A plane through {point_M}{point_E} intersects edges {point_A1}{point_D}, {point_A1}{point_B} at points {point_S}, {point_T} respectively. Let the areas of triangles {point_A1}{point_S}{point_T} and {point_A1}{point_B}{point_D} be S_{point_A1}{point_S}{point_T}, S_{point_A1}{point_B}{point_D} respectively. If S_{point_A1}{point_S}{point_T}/S_{point_A1}{point_B}{point_D} = {len_k}, find the value of {point_A1}{point_S}/{point_A1}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"fz1_10_3({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_A1}', '{point_M}', '{point_S}', '{point_T}')"}, ensure_ascii=False) + "\n")
