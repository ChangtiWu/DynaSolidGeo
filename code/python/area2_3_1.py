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
def calculate(len_a, len_h):
    """
    计算正四棱锥冷水塔塔顶的侧面积

    参数:
    len_a (float): 底面边长
    len_h (float): 高

    返回:
    float: 侧面积
    """
    import math
    # 根据题解公式 S = len_a * sqrt(4 * len_h^2 + len_a^2)
    return len_a * math.sqrt(4 * len_h ** 2 + len_a ** 2)


# 定义题干中的参数
len_a = 1.5   # 底面边长
len_h = 0.85  # 高

# 验证计算结果
#result = calculate(len_a, len_h)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, len_h)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_3_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"设计一个正四棱锥形冷水塔塔顶，高为 {len_h}，底面的边长为 {len_a}，求制造这种塔顶需要的铁板面积（即求正四棱锥的侧面积）。",
    "en_problem": f"Design a regular square pyramid-shaped cooling tower top with height {len_h} and base side length {len_a}. Find the area of iron plate needed to manufacture this tower top (i.e., find the lateral surface area of the regular square pyramid).",
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
    f.write(json.dumps({json_data["id"]: f"area2_3_1({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
