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
point_A, point_B, point_C, point_D, point_E, point_F, point_R, point_T, point_S = random.sample(string.ascii_uppercase, 9)

# Add result calculation code
import math

def calculate(len_a, len_b, len_c):
    """
    计算多面体体积

    参数:
    len_a (float): AB = BC
    len_b (float): AF = CD
    len_c (float): AR = RF = TC = TD

    返回:
    float: 多面体体积
    """
    return len_b * (3 * len_a - len_b) * math.sqrt(len_c**2 - (len_b**2) / 4) / 2


# 题干给定的数值
len_a = 8.0       # AB = BC
len_b = 4.0       # AF = CD
len_c = 5/2       # AR = RF = TC = TD

# 验证输出
#volume = calculate(len_a, len_b, len_c)
#print(f"多面体体积: {volume:.6f}")

# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)
len_c = round(len_scaling_factor * float(len_c), 2)

# Calculate the result
result = calculate(len_a, len_b, len_c)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee25_5_1",
    "type": 5,
    "level": 2,
    "cn_problem": f"某科技兴趣小组通过3D打印机的一个零件可以抽象为如图所示的多面体，其中{point_A}{point_B}{point_C}{point_D}{point_E}{point_F}是一个平行多边形，平面{point_A}{point_R}{point_F}⊥平面{point_A}{point_B}{point_C}，平面{point_T}{point_C}{point_D}⊥平面{point_A}{point_B}{point_C}，{point_A}{point_B}⊥{point_B}{point_C}，{point_A}{point_B}//{point_R}{point_S}//{point_E}{point_F}//{point_C}{point_D}，{point_A}{point_F}//{point_S}{point_T}//{point_B}{point_C}//{point_E}{point_D}，若{point_A}{point_B}={point_B}{point_C}={len_a}，{point_A}{point_F}={point_C}{point_D}={len_b}，{point_A}{point_R}={point_R}{point_F}={point_T}{point_C}={point_T}{point_D}={len_c}，则该多面体的体积为_________。",
    "en_problem": f"A part from a 3D printer by a technology interest group can be abstracted as the polyhedron shown in the figure, where {point_A}{point_B}{point_C}{point_D}{point_E}{point_F} is a parallelogram, plane {point_A}{point_R}{point_F}⊥plane {point_A}{point_B}{point_C}, plane {point_T}{point_C}{point_D}⊥plane {point_A}{point_B}{point_C}, {point_A}{point_B}⊥{point_B}{point_C}, {point_A}{point_B}//{point_R}{point_S}//{point_E}{point_F}//{point_C}{point_D}, {point_A}{point_F}//{point_S}{point_T}//{point_B}{point_C}//{point_E}{point_D}, if {point_A}{point_B}={point_B}{point_C}={len_a}, {point_A}{point_F}={point_C}{point_D}={len_b}, {point_A}{point_R}={point_R}{point_F}={point_T}{point_C}={point_T}{point_D}={len_c}, then find the volume of this polyhedron.",
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
    f.write(json.dumps({json_data["id"]: f"ncee25_5_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_E}', '{point_F}', '{point_R}', '{point_T}', '{point_S}')"}, ensure_ascii=False) + "\n")
