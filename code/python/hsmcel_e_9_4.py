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
point_A, point_B, point_C, point_A1, point_B1, point_C1, point_D = random.sample(string.ascii_uppercase, 7)

# Add result calculation code
import math


def calculate(len_a):
    """计算三角形BC₁D的面积"""
    return (3 * math.sqrt(3) / 8) * (len_a ** 2)


# 测试示例
len_a = 1.0

# print(calculate(len_a))

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_9_4",
    "type": 4,
    "level": 3,
    "cn_problem": f"设 ${point_A}{point_B}{point_C}$-${point_A1}{point_B1}{point_C1}$ 为正三棱柱，其一切棱长均为 ${len_a}>0$；过侧棱 ${point_B}{point_C1}$ 的中点 ${point_D}$ 作动平面 $\\pi$，该平面分别与底面 ${point_A}{point_B}{point_C}$、三个侧面 ${point_A}{point_B}{point_B1}{point_A1}$、${point_A}{point_C}{point_C1}{point_A1}$、${point_B}{point_C}{point_C1}{point_B1}$ 的交线所成二面角依次记为 $arg_alpha_1$、$arg_alpha_2$、$arg_alpha_3$、$arg_alpha_4$。已知 $\\cos{{arg_alpha_1}}+\\cos{{arg_alpha_2}}=\\cos{{arg_alpha_3}}+\\cos{{arg_alpha_4}}$。设平面 $\\pi$ 在侧面 ${point_B}{point_C1}{point_D}$ 上截得三角形 $\\triangle {point_B}{point_C1}{point_D}$。求 $area_S_{{\\triangle {point_B}{point_C1}{point_D}}}$。",
    "en_problem": f"Let ${point_A}{point_B}{point_C}$-${point_A1}{point_B1}{point_C1}$ be a regular triangular prism with all edge lengths equal to ${len_a}>0$. Through the midpoint ${point_D}$ of lateral edge ${point_B}{point_C1}$, construct a movable plane $\\pi$ that intersects the base ${point_A}{point_B}{point_C}$ and the three lateral faces ${point_A}{point_B}{point_B1}{point_A1}$, ${point_A}{point_C}{point_C1}{point_A1}$, ${point_B}{point_C}{point_C1}{point_B1}$ to form dihedral angles denoted as $arg_alpha_1$, $arg_alpha_2$, $arg_alpha_3$, $arg_alpha_4$ respectively. Given that $\\cos{{arg_alpha_1}}+\\cos{{arg_alpha_2}}=\\cos{{arg_alpha_3}}+\\cos{{arg_alpha_4}}$. Let plane $\\pi$ intersect the lateral face ${point_B}{point_C1}{point_D}$ to form triangle $\\triangle {point_B}{point_C1}{point_D}$. Find that $area_S_{{\\triangle {point_B}{point_C1}{point_D}}} $ .",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_9_4({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D}')"}, ensure_ascii=False) + "\n")
