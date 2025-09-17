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
point_S, point_A, point_B, point_C, point_D, point_O = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
def calculate(len_a, len_h):
    """
    计算正四棱锥的表面积

    参数:
    len_a (float): 底面边长
    len_h (float): 顶点到底面中心的距离（高）

    返回:
    float: 表面积
    """
    # 根据题解公式 S = len_a^2 + len_a * sqrt(len_a^2 + 4 * len_h^2)
    import math
    return len_a ** 2 + len_a * math.sqrt(len_a ** 2 + 4 * len_h ** 2)


# 定义题干中的参数
len_a = 4.0   # 底面边长
len_h = 4.0   # 顶点到底面中心的距离（高）

# 验证计算结果
#result = calculate(len_a, len_h)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_h = round(len_scaling_factor * float(len_h), 2)

# Calculate the result
result = calculate(len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_2_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"设正四棱锥 {point_S} - {point_A}{point_B}{point_C}{point_D} 的底面边长为 {len_a}，顶点 {point_S} 到底面中心 {point_O} 的距离（高）为 {len_h}，求该正四棱锥的表面积。",
    "en_problem": f"Given a regular square pyramid {point_S} - {point_A}{point_B}{point_C}{point_D} with base side length {len_a} and height {len_h} from vertex {point_S} to the base center {point_O}, find the surface area of the pyramid.",
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
    f.write(json.dumps({json_data["id"]: f"area2_2_1({mode}, {azimuth}, {elevation}, '{point_S}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_O}')"}, ensure_ascii=False) + "\n")
