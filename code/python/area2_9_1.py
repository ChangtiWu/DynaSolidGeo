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

def calculate(len_a, len_b, len_c):
    """
    计算旋转形成圆台后，上底面积、下底面积和侧面积的比值

    参数:
    len_a (float): 上底边长
    len_b (float): 下底边长
    len_c (float): 高

    返回:
    tuple: (上底面积比, 下底面积比, 侧面积比)
    """
    # 上底面积比
    S_upper = len_a ** 2

    # 下底面积比
    S_lower = len_b ** 2

    # 侧面积比
    S_lateral = (len_a + len_b) * math.sqrt((len_b - len_a) ** 2 + len_c ** 2)

    return S_lower / S_lateral


# 定义题干参数
len_a = 2.0
len_b = 4.0
len_c = math.sqrt(5)

# 验证计算结果
#result = calculate(len_a, len_b, len_c)
#print(f"面积比: {result}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_9_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"一个直角梯形上底、下底和高之比为 {len_a} : {len_b} : {len_c} ({len_a}>0, {len_b}>0, {len_c}>0)。将此直角梯形以垂直于底的腰为轴旋转一周形成一个圆台，求这个圆台下底面积和侧面积之比。",
    "en_problem": f"The ratio of the upper base, lower base, and height of a right trapezoid is {len_a} : {len_b} : {len_c} (where {len_a}>0, {len_b}>0, {len_c}>0). The trapezoid is rotated around its leg that is perpendicular to the bases to form a frustum. Find the ratio of the lower base area and the lateral surface area of the frustum.",
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
    f.write(json.dumps({json_data["id"]: f"area2_9_1({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
