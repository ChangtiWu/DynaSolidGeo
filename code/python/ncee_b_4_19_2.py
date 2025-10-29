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
point_O, point_O1, point_A, point_C, point_A1, point_B1 = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math


def calculate(len_h, len_r, ang_phi, ang_theta):
    """
    计算给定参数对应的cosθ值。

    参数:
        len_h (float): 长度参数（分子部分）。
        len_r (float): 长度参数（影响分母的正弦项）。
        ang_phi (float): 角度参数（弧度制，与ang_theta的差值参与正弦计算）。
        ang_theta (float): 角度参数（弧度制，与ang_phi的差值参与正弦计算）。

    返回:
        float: 计算得到的cosθ值。

    注意:
        输入角度需为弧度制；分母根号内表达式需非负（否则会抛出数学错误）。
    """
    # 计算角度差的一半（弧度制）
    angle_diff_half = (ang_phi - ang_theta) / 2

    # 计算正弦平方项：sin²(angle_diff_half)
    sin_sq = math.sin(angle_diff_half) ** 2

    # 计算分母的根号内部分：len_h² + 4*len_r²*sin_sq
    denominator_inside = len_h ** 2 + 4 * (len_r ** 2) * sin_sq

    # 计算分母的平方根
    denominator = math.sqrt(denominator_inside)

    # 计算cosθ：分子/分母
    cos_theta = len_h / denominator

    return cos_theta


len_h = 1.0
len_r = 1.0
ang_phi = math.pi / 3
ang_theta = math.pi / 3 * 2

# cos_theta = calculate(len_h, len_r, ang_phi, ang_theta)
# print(f"cosθ = {cos_theta:.4f}")
# Generate random lengths
len_h = round(len_scaling_factor * float(len_h), 2)
len_r = round(len_scaling_factor * float(len_r), 2)

# Calculate the result
result = calculate(len_h, len_r, ang_phi, ang_theta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "ncee_b_4_19_2",
    "type": 2,
    "level": 2,
    "cn_problem": f"如图，在圆柱体中：下底面圆心 {point_O}(0,0,0)，上底面圆心 {point_O1}(0,0,{len_h})，其底面半径为 {len_r}、高为 {len_h}（{len_r},{len_h}>0）。在下底圆上取点 {point_A}({len_r},0,0)，{point_C}({len_r}·cos {ang_theta},{len_r}·sin {ang_theta},0)，其中 0<{ang_theta}<2π；在上底圆上取点 {point_A1}({len_r},0,{len_h})，{point_B1}({len_r}·cos {ang_phi},{len_r}·sin {ang_phi},{len_h})，其中 0<{ang_phi}<2π，且 {point_B1} 与 {point_C} 位于平面 {point_A}{point_A1}{point_O1}{point_O} 的同侧。求异面直线 {point_B1}{point_C} 与 {point_A}{point_A1} 所成锐角 θ 的余弦值。",
    "en_problem": f"As shown, in a right circular cylinder: the lower base center is {point_O}(0,0,0) and the upper base center is {point_O1}(0,0,{len_h}). The cylinder has radius {len_r} and height {len_h} ({len_r},{len_h}>0). On the lower base circle take points {point_A}({len_r},0,0) and {point_C}({len_r}·cos {ang_theta},{len_r}·sin {ang_theta},0) with 0<{ang_theta}<2π. On the upper base circle take points {point_A1}({len_r},0,{len_h}) and {point_B1}({len_r}·cos {ang_phi},{len_r}·sin {ang_phi},{len_h}) with 0<{ang_phi}<2π, and {point_B1} lies on the same side of the plane {point_A}{point_A1}{point_O1}{point_O} as {point_C}. Find the acute angle θ between skew lines {point_B1}{point_C} and {point_A}{point_A1}.",
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
    f.write(json.dumps({json_data["id"]: f"ncee_b_4_19_2({mode}, {azimuth}, {elevation}, '{point_O}', '{point_O1}', '{point_A}', '{point_C}', '{point_A1}', '{point_B1}')"}, ensure_ascii=False) + "\n")
