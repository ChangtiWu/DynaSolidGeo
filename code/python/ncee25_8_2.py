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
point_P, point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math

def calculate():
    """
    计算直线 AB 与平面 PCD 所成角的正弦值

    返回:
    float: 正弦值
    """
    # 已知结果
    return math.sqrt(3) / 3


# 题干给定的数值
len_a = 1.0  # AD = CD = a，比例任意可选
# AB = AC = √2 * a
# PA ⊥ 面 ABCD，PA = AC = √2 * a

# 验证输出
# result = calculate()
# print(f"正弦值: {result:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee25_8_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"四棱锥{point_P}-{point_A}{point_B}{point_C}{point_D}中，△{point_A}{point_C}{point_D}与△{point_A}{point_B}{point_C}为等腰直角三角形，∠ {point_A}{point_D}{point_C}=90^\\circ，∠ {point_B}{point_A}{point_C}=90^\\circ。设{point_A}{point_D}={point_C}{point_D}={len_a}（{len_a}>0），则{point_A}{point_C}=\\sqrt{{{point_A}{point_D}^2+{point_C}{point_D}^2}}=\\sqrt{{2}}{len_a}；由△{point_A}{point_B}{point_C}为等腰直角三角形，得{point_A}{point_B}={point_A}{point_C}=\\sqrt{{2}}{len_a}。又{point_P}{point_A}⊥面{point_A}{point_B}{point_C}{point_D}，且{point_P}{point_A}={point_A}{point_C}=\\sqrt{{2}}{len_a}，求{point_A}{point_B}与面{point_P}{point_C}{point_D}所成角的正弦值。",
    "en_problem": f"In the quadrangular pyramid {point_P}-{point_A}{point_B}{point_C}{point_D}, △{point_A}{point_C}{point_D} and △{point_A}{point_B}{point_C} are isosceles right triangles, ∠ {point_A}{point_D}{point_C}=90^\\circ, ∠ {point_B}{point_A}{point_C}=90^\\circ. Let {point_A}{point_D}={point_C}{point_D}={len_a} ({len_a}>0), then {point_A}{point_C}=\\sqrt{{{point_A}{point_D}^2+{point_C}{point_D}^2}}=\\sqrt{{2}}{len_a}; since △{point_A}{point_B}{point_C} is an isosceles right triangle, {point_A}{point_B}={point_A}{point_C}=\\sqrt{{2}}{len_a}. Also {point_P}{point_A}⊥plane {point_A}{point_B}{point_C}{point_D}, and {point_P}{point_A}={point_A}{point_C}=\\sqrt{{2}}{len_a}, find the sine of the angle between {point_A}{point_B} and plane {point_P}{point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee25_8_2({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
