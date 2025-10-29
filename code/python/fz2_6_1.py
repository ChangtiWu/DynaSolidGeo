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
point_A, point_C, point_B, point_D, point_P = random.sample(string.ascii_uppercase, 5)

# Add result calculation code
import math

def calculate(len_a, len_c, arg_alpha):
    """
    计算三棱锥 P-ABC 的外接球体积

    参数:
    len_a (float): BC 的长度
    len_c (float): AB 的长度
    arg_alpha (float): ∠ABD = ∠BAD 的角度（单位：弧度）

    返回:
    float: 外接球体积
    """
    # 根据题干给出的解答公式:
    # (π / 6) * ( (len_c^2 / (sin(2*arg_alpha))^2) + len_a^2 )^(3/2)
    return (math.pi / 6) * ((len_c ** 2) / (math.sin(2 * arg_alpha) ** 2) + len_a ** 2) ** 1.5


# 定义题干中的参数变量
len_a = 2.0            # BC = 2
len_c = math.sqrt(3)   # AB = √3
arg_alpha = math.radians(30)  # ∠ABD = ∠BAD = 30°

# 验证计算结果（确认与参考答案一致后注释掉）
#result = calculate(len_a, len_c, arg_alpha)
#print(f"计算结果: {result:.6f}")

# Generate random lengths
len_c = round(len_scaling_factor * float(len_c), 2)
len_a = round(len_scaling_factor * float(len_a), 2)

# Calculate the result
result = calculate(len_a, len_c, arg_alpha)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "fz2_6_1",
    "type": 8,
    "level": 1,
    "cn_problem": f"平面四边形{point_A}{point_C}{point_B}{point_D}中，∠{point_A}{point_B}{point_C}=90°，∠{point_A}{point_B}{point_D}= ∠{point_B}{point_A}{point_D}={arg_alpha}，{point_A}{point_B} = {len_c}，{point_B}{point_C} = {len_a}。现将三角形{point_A}{point_B}{point_D}沿{point_A}{point_B}翻折，使点{point_D}移动至点{point_P}，且{point_P}{point_B}⊥{point_B}{point_C}，求三棱锥{point_P} - {point_A}{point_B}{point_C}的外接球的体积。",
    "en_problem": f"In planar quadrilateral {point_A}{point_C}{point_B}{point_D}, ∠{point_A}{point_B}{point_C}=90°, ∠{point_A}{point_B}{point_D}= ∠{point_B}{point_A}{point_D}={arg_alpha}, {point_A}{point_B} = {len_c}, {point_B}{point_C} = {len_a}. Triangle {point_A}{point_B}{point_D} is folded along {point_A}{point_B} so that point {point_D} moves to point {point_P}, and {point_P}{point_B}⊥{point_B}{point_C}. Find the volume of the circumsphere of triangular pyramid {point_P} - {point_A}{point_B}{point_C}.",
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
    f.write(json.dumps({json_data["id"]: f"fz2_6_1({mode}, {azimuth}, {elevation}, '{point_A}', '{point_C}', '{point_B}', '{point_D}', '{point_P}')"}, ensure_ascii=False) + "\n")
