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
point_A, point_B, point_C, point_D = random.sample(string.ascii_uppercase, 4)

# Add result calculation code
import math


def calculate(len_a, arg_theta, arg_phi, arg_delta):
    """
    计算异面直线AB和CD之间的距离

    参数:
    len_a (float): 线段AC的长度
    arg_theta (float): 角BAC的大小（在平面alpha内，AB与AC的夹角）
    arg_phi (float): 角ACD的大小（在平面beta内，AC与CD的夹角）
    arg_delta (float): 二面角alpha-AB-beta的大小

    返回:
    float: 异面直线AB和CD之间的距离
    """
    # 计算分子: len_a * sin(arg_delta)
    numerator = len_a * math.sin(arg_delta)

    # 计算分母中的各项:
    # cot(arg_theta) = cos(arg_theta) / sin(arg_theta)
    cot_theta = math.cos(arg_theta) / math.sin(arg_theta)
    # cot(arg_phi) = cos(arg_phi) / sin(arg_phi)
    cot_phi = math.cos(arg_phi) / math.sin(arg_phi)
    # sin^2(arg_theta)
    sin_theta_sq = math.sin(arg_theta) ** 2
    # cot^2(arg_theta)
    cot_theta_sq = cot_theta ** 2
    # cot^2(arg_phi)
    cot_phi_sq = cot_phi ** 2
    # 2 * cot(arg_theta) * cot(arg_phi) * cos(arg_delta)
    term_2cot_cos = 2 * cot_theta * cot_phi * math.cos(arg_delta)

    # 计算分母: sqrt(sin^2(arg_delta) + cot^2(arg_theta) + cot^2(arg_phi) + 2 * cot(arg_theta) * cot(arg_phi) * cos(arg_delta))
    denominator = math.sqrt(math.sin(arg_delta) ** 2 + cot_theta_sq + cot_phi_sq + term_2cot_cos)

    # 返回分子除以分母的结果
    return numerator / denominator


len_a = 1  # 线段AC的长度
arg_theta = math.pi / 4  # 角BAC的大小，例如设置为pi/4（45度）
arg_phi = math.pi / 4  # 角ACD的大小，例如设置为pi/3（60度）
arg_delta = math.pi / 2   # 二面角alpha-AB-beta的大小，例如设置为pi/2（90度）
#
# # 计算异面直线AB和CD之间的距离
# result = calculate(len_a, arg_theta, arg_phi, arg_delta)
#
# # 打印计算结果，保留6位小数
# print(f"异面直线AB和CD之间的距离: {result:.6f}")
# Generate random lengths

len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, arg_theta, arg_phi, arg_delta)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_s_5_1",
    "type": 3,
    "level": 3,
    "cn_problem": f"在二面角 plain_alpha -{point_A}{point_B}- plain_beta 中，棱为{point_A}{point_B}，平面 plain_alpha 包含{point_A}{point_B}，平面 plain_beta 包含{point_A}{point_B}，二面角大小为{arg_delta}（0 < {arg_delta} < π）。点{point_A} ∈ {point_A}{point_B}，{point_C} ∈  plain_beta ，满足：∠{point_B}{point_A}{point_C} = {arg_theta}（ plain_alpha 内，{point_A}{point_B}与{point_A}{point_C}的夹角），∠{point_A}{point_C}{point_D} = {arg_phi}（ plain_beta 内，{point_A}{point_C}与{point_C}{point_D}的夹角），{point_A}{point_C} = {len_a}（线段长度）。求异面直线{point_A}{point_B}和{point_C}{point_D}之间的距离。",
    "en_problem": f"In a dihedral angle  plain_alpha -{point_A}{point_B}- plain_beta , the edge is {point_A}{point_B}, plane  plain_alpha  contains {point_A}{point_B}, plane  plain_beta  contains {point_A}{point_B}, and the dihedral angle is {arg_delta} (0 < {arg_delta} < π). Point {point_A} ∈ {point_A}{point_B}, {point_C} ∈  plain_beta , satisfying: ∠{point_B}{point_A}{point_C} = {arg_theta} (in  plain_alpha , angle between {point_A}{point_B} and {point_A}{point_C}), ∠{point_A}{point_C}{point_D} = {arg_phi} (in  plain_beta , angle between {point_A}{point_C} and {point_C}{point_D}), {point_A}{point_C} = {len_a} (segment length). Find the distance between the skew lines {point_A}{point_B} and {point_C}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_s_5_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}')"}, ensure_ascii=False) + "\n")
