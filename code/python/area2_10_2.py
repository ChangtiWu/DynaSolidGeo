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
point_S, point_O = random.sample(string.ascii_uppercase, 2)

# Add result calculation code
import math

def calculate(len_r, len_h):
    """
    计算圆锥 SO 的表面积

    参数:
    len_r (float): 底面半径 r
    len_h (float): 高 h

    返回:
    float: 圆锥表面积
    """
    # 根据题干给出的解答公式:
    # S = π * r * (sqrt(h^2 + r^2) + r)
    return math.pi * len_r * (math.sqrt(len_h ** 2 + len_r ** 2) + len_r)


# 定义题干中的参数变量
len_r = 2.0  # 由 SO = OB = 2 得底面半径 OB = 2
len_h = 2.0  # 高 SO = 2

# 验证计算结果（确认与参考答案一致后注释掉）
#result = calculate(len_r, len_h)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_r = round(len_scaling_factor * float(len_r), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_r, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_10_2",
    "type": 4,
    "level": 1,
    "cn_problem": f"设圆锥 {point_S}{point_O} 的底面半径为 {len_r}，高为 {len_h}，求圆锥 {point_S}{point_O} 的表面积。",
    "en_problem": f"Given a cone {point_S}{point_O} with base radius {len_r} and height {len_h}, find the surface area of cone {point_S}{point_O}.",
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
    f.write(json.dumps({json_data["id"]: f"area2_10_2({mode}, {azimuth}, {elevation}, '{point_S}', '{point_O}')"}, ensure_ascii=False) + "\n")
