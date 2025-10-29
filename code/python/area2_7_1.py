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
len_scaling_factor = round(random.uniform(1, 100.0), 1)

# Add result calculation code
def calculate(len_n):
    """
    计算正六棱台及小棱锥、大棱锥的侧面积比例

    参数:
    len_n (int): 分割高度的比例分母（正整数）

    返回:
    tuple: (大棱锥侧面积比, 小棱锥侧面积比, 棱台侧面积比)
    """
    S_large = (len_n + 1) ** 2
    S_small = 1
    S_frustum = len_n * (len_n + 2)
    return S_large, S_small, S_frustum


# 定义题干中的参数
len_n = 1  # 高的比例 1:len_n

# 验证计算结果
#result = calculate(len_n)
#print(f"侧面积比例: {result}")

# Generate random lengths
len_n = int(len_scaling_factor * float(len_n))

# Calculate the result
result1, result2, result3 = calculate(len_n)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "area2_7_1",
    "type": 4,
    "level": 1,
    "cn_problem": f"正六棱锥被过棱锥高上一点且平行于底面的平面所截，该点分棱锥高的比为 1:{len_n}（{len_n} 为正整数），得到正六棱台和较小的棱锥。求大棱锥、小棱锥、棱台的侧面积之比。",
    "en_problem": f"A regular hexagonal pyramid is cut by a plane parallel to the base passing through a point on the pyramid height, where the point divides the height in the ratio 1:{len_n} ({len_n} is a positive integer), resulting in a regular hexagonal frustum and a smaller pyramid. Find the ratio of lateral surface areas of the large pyramid, small pyramid, and frustum.",
    "solution": f"{result1}:{result2}:{result3}",
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
    f.write(json.dumps({json_data["id"]: f"area2_7_1({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
