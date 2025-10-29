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
point_P, point_A, point_B, point_C = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math


def calculate(arg_alpha, arg_beta, arg_gamma):
    """计算arg_theta和cos(arg_phi)的角度关系表达式"""
    # 计算arg_theta的分子部分（平方根内）
    sqrt_numerator = math.sqrt(
        math.cos(arg_beta) ** 2 +
        math.cos(arg_gamma) ** 2 -
        2 * math.cos(arg_alpha) * math.cos(arg_beta) * math.cos(arg_gamma)
    )
    # 计算arg_theta（反余弦）
    arg_theta = math.acos(sqrt_numerator / math.sin(arg_alpha))


    return arg_theta


# 测试示例
arg_alpha = math.pi / 3
arg_beta = math.pi / 3
arg_gamma = math.pi / 3

# print(calculate(arg_alpha, arg_beta, arg_gamma))

# Generate random lengths

# Calculate the result
result = calculate(arg_alpha, arg_beta, arg_gamma)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_s_11_1_1",
    "type": 2,
    "level": 3,
    "cn_problem": f"从点 ${point_P}$ 出发的三条射线 ${point_P}{point_A}$、${point_P}{point_B}$、${point_P}{point_C}$ 两两所成的角分别为 $\\angle {point_A}{point_P}{point_B} = {arg_alpha}$，$\\angle {point_B}{point_P}{point_C} = {arg_beta}$，$\\angle {point_C}{point_P}{point_A} = {arg_gamma}$。求：(1) 直线 ${point_P}{point_C}$ 与平面 ${point_P}{point_A}{point_B}$ 所成的角 $ arg_theta $。",
    "en_problem": f"From point ${point_P}$, three rays ${point_P}{point_A}$, ${point_P}{point_B}$, ${point_P}{point_C}$ form pairwise angles $\\angle {point_A}{point_P}{point_B} = {arg_alpha}$, $\\angle {point_B}{point_P}{point_C} = {arg_beta}$, $\\angle {point_C}{point_P}{point_A} = {arg_gamma}$. Find: (1) the angle $ arg_theta $ between line ${point_P}{point_C}$ and plane ${point_P}{point_A}{point_B}$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_s_11_1_1({mode}, {azimuth}, {elevation}, '{point_P}', '{point_A}', '{point_B}', '{point_C}')"}, ensure_ascii=False) + "\n")
