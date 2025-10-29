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
point_A, point_B, point_C, point_D, point_A1, point_B1, point_C1, point_D1, point_E, point_F = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
import math

def calculate(len_m: float) -> float:
    """
    题意：在棱长为 len_m 的正方体 ABCD-A1B1C1D1 中，
          E 为面 BCC1B1 的中心，F 为面 ABCD 的中心。
          求异面直线 EF 与 A1C1 的距离。

    推导与实现（坐标法 + 叉乘公式）：
    1) 取标准坐标（单位：len_m）：
       A(0,0,0), B(m,0,0), C(m,m,0), D(0,m,0)
       A1(0,0,m), B1(m,0,m), C1(m,m,m), D1(0,m,m)
       其中 m = len_m

    2) 面 BCC1B1：x = m，其中心 E = (m, m/2, m/2)
       面 ABCD：z = 0，其中心 F = (m/2, m/2, 0)

    3) 方向向量：
       u = ->A1C1 = C1 - A1 = (m, m, 0)
       v = ->EF  = F - E  = (-m/2, 0, -m/2)

    4) 公式：dist = | (A1 - E) · (u × v) | / ||u × v||
       计算可得 dist = (sqrt(3)/3) * m
       但此函数内按步骤数值计算，不直接写成简式，以体现“如何推出”。

    参数:
        len_m (float): 正方体棱长 m

    返回:
        float: 距离数值
    """
    m = float(len_m)

    # 点坐标
    A1 = (0.0, 0.0, m)
    C1 = (m,   m,   m)
    E  = (m,   m/2, m/2)
    F  = (m/2, m/2, 0.0)

    # 向量运算的辅助函数
    def sub(p, q):  # p - q
        return (p[0]-q[0], p[1]-q[1], p[2]-q[2])

    def dot(x, y):
        return x[0]*y[0] + x[1]*y[1] + x[2]*y[2]

    def cross(x, y):
        return (x[1]*y[2] - x[2]*y[1],
                x[2]*y[0] - x[0]*y[2],
                x[0]*y[1] - x[1]*y[0])

    def norm(x):
        return math.sqrt(dot(x, x))

    # 方向向量
    u = sub(C1, A1)   # A1C1
    v = sub(F,  E)    # EF
    w = sub(A1, E)    # (r0 - s0) 取 r0 = A1, s0 = E

    u_cross_v = cross(u, v)
    numerator = abs(dot(w, u_cross_v))
    denominator = norm(u_cross_v)
    if denominator == 0.0:
        raise ValueError("方向向量共线，无法计算异面直线距离（输入不应使两线平行）。")

    return numerator / denominator

len_m = 2.0 

#result = calculate(len_m=len_m)
#expected = (math.sqrt(3) / 3) * len_m
#print(f"距离(向量法) = {result:.10f}")
#print(f"参考值(√3/3·m) = {expected:.10f}")
#print("是否一致：", math.isclose(result, expected, rel_tol=1e-12, abs_tol=1e-12))

# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)

# Calculate the result
result = calculate(len_m)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_5_6",
    "type": 3,
    "level": 2,
    "cn_problem": f"在棱长为{len_m}的正方体{point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1}中，{point_E}、{point_F}分别是面{point_B}{point_C}{point_C1}{point_B1}和{point_A}{point_B}{point_C}{point_D}的中心，求异面直线{point_E}{point_F}与{point_A1}{point_C1}的距离。",
    "en_problem": f"In a cube {point_A}{point_B}{point_C}{point_D}-{point_A1}{point_B1}{point_C1}{point_D1} with edge length {len_m}, where {point_E} and {point_F} are the centers of faces {point_B}{point_C}{point_C1}{point_B1} and {point_A}{point_B}{point_C}{point_D} respectively, find the distance between skew lines {point_E}{point_F} and {point_A1}{point_C1}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_5_6({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_A1}', '{point_B1}', '{point_C1}', '{point_D1}', '{point_E}', '{point_F}')"}, ensure_ascii=False) + "\n")
