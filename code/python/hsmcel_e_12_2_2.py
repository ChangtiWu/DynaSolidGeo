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
point_S, point_A, point_B, point_C, point_D, point_K, point_M, point_N = random.sample(string.ascii_uppercase, 8)

# Add result calculation code
def calculate():
    """计算R(x)的最小值和最大值"""
    min_r = 1/3
    max_r = 3/8
    return max_r

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_e_12_2_2",
    "type": 5,
    "level": 3,
    "cn_problem": f"设棱锥 ${point_S}\\text{{-}}{point_A}{point_B}{point_C}{point_D}$ 的底面是平行四边形 ${point_A}{point_B}{point_C}{point_D}$。点 ${point_K}$ 为棱 ${point_S}{point_C}$ 的中点。取一平面过顶点 ${point_A}$ 和点 ${point_K}$，分别与棱 ${point_S}{point_B}$、${point_S}{point_D}$ 相交于 ${point_M}$、${point_N}$。定义参数 $x = \\frac{{|{point_S}{point_M}|}}{{|{point_S}{point_B}|}}$，则有约束关系 $y = \\frac{{|{point_S}{point_N}|}}{{|{point_S}{point_D}|}} = \\frac{{x}}{{3x-1}}$，其中 $\\frac{{1}}{{2}} \\leq x \\leq 1$。记体积比 $R(x) = \\frac{{ volume_V_{{{point_S}\\text{{-}}{point_A}{point_M}{point_K}{point_N}}}}}{{ volume_V_{{{point_S}\\text{{-}}{point_A}{point_B}{point_C}{point_D}}}}}$，求 $R(x)$ 的最大值。",
    "en_problem": f"Let pyramid ${point_S}\\text{{-}}{point_A}{point_B}{point_C}{point_D}$ have a parallelogram ${point_A}{point_B}{point_C}{point_D}$ as its base. Point ${point_K}$ is the midpoint of edge ${point_S}{point_C}$. A plane passing through vertex ${point_A}$ and point ${point_K}$ intersects edges ${point_S}{point_B}$ and ${point_S}{point_D}$ at points ${point_M}$ and ${point_N}$ respectively. Define parameter $x = \\frac{{|{point_S}{point_M}|}}{{|{point_S}{point_B}|}}$, then there exists a constraint relationship $y = \\frac{{|{point_S}{point_N}|}}{{|{point_S}{point_D}|}} = \\frac{{x}}{{3x-1}}$, where $\\frac{{1}}{{2}} \\leq x \\leq 1$. Let the volume ratio $R(x) = \\frac{{ volume_V_{{{point_S}\\text{{-}}{point_A}{point_M}{point_K}{point_N}}}}}{{ volume_V_{{{point_S}\\text{{-}}{point_A}{point_B}{point_C}{point_D}}}}}$，find the maximum value of $R(x)$.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_e_12_2_2({mode}, {azimuth}, {elevation}, '{point_S}', '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_K}', '{point_M}', '{point_N}')"}, ensure_ascii=False) + "\n")
