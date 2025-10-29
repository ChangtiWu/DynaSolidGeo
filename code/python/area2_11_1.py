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

def calculate(len_R, len_H):
    """
    计算圆锥的表面积与体积

    参数:
    len_R (float): 圆锥的底面半径
    len_H (float): 圆锥的高

    返回:
    tuple: (表面积, 体积)
    """
    # 表面积: S = πR^2 + πR√(R^2 + H^2)
    S = math.pi * len_R ** 2 + math.pi * len_R * math.sqrt(len_R ** 2 + len_H ** 2)
    
    # 体积: V = (1/3)πR^2H
    V = (1 / 3) * math.pi * len_R ** 2 * len_H
    
    return V


# 定义题干中的参数变量
len_R = 1.0  # 底面半径
len_H = 3.0  # 高

# 验证计算结果（确认与参考答案一致后注释掉）
#S, V = calculate(len_R, len_H)
#print(f"表面积: {S:.6f}, 体积: {V:.6f}")

# Generate random lengths
len_R = round(len_scaling_factor * float(len_R), 2)
len_H = round(len_scaling_factor * float(len_H), 2)

# Calculate the result
result = calculate(len_R, len_H)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_11_1",
    "type": 5,
    "level": 1,
    "cn_problem": f"设圆锥的底面半径为 {len_R}，高为 {len_H}，求此圆锥的体积。",
    "en_problem": f"Given a cone with base radius {len_R} and height {len_H}, find the volume of this cone.",
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
    f.write(json.dumps({json_data["id"]: f"area2_11_1({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
