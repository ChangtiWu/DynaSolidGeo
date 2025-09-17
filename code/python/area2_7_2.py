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

def calculate(len_a, len_l):
    """
    计算正六棱台的侧面积和表面积

    参数:
    len_a (float): 小棱锥的底面边长
    len_l (float): 大棱锥的侧棱长

    返回:
    tuple: (侧面积, 表面积)
    """
    # 计算侧面积 S_侧 = (9 * len_a / 2) * sqrt(len_l^2 - len_a^2)
    lateral_area = (9 * len_a / 2) * math.sqrt(len_l ** 2 - len_a ** 2)

    # 计算表面积 S_表 = S_侧 + (15 * sqrt(3) / 2) * len_a^2
    total_area = lateral_area + (15 * math.sqrt(3) / 2) * len_a ** 2

    return lateral_area, total_area


# 定义题干中的参数
len_a = 4.0    # 小棱锥的底面边长
len_l = 12.0   # 大棱锥的侧棱长

# 验证计算结果
#lateral, total = calculate(len_a, len_l)
#print(f"侧面积: {lateral:.6f}, 表面积: {total:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_l = round(len_scaling_factor * float(len_l), 2)

# Calculate the result
result = calculate(len_a, len_l)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_7_2",
    "type": 4,
    "level": 1,
    "cn_problem": f"已知正六棱锥被过其高的中点且平行于底面的平面所截，得到正六棱台。若小棱锥的底面边长为 {len_a}，大棱锥的侧棱长为 {len_l}，求截得的棱台的侧面积和表面积。",
    "en_problem": f"A regular hexagonal pyramid is cut by a plane parallel to the base passing through the midpoint of its height, resulting in a regular hexagonal frustum. Given that the base side length of the small pyramid is {len_a} and the lateral edge length of the large pyramid is {len_l}, find the lateral surface area and total surface area of the resulting frustum.",
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
    f.write(json.dumps({json_data["id"]: f"area2_7_2({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
