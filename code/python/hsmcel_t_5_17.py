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
point_A, point_B, point_C, point_D, point_P, point_Q = random.sample(string.ascii_uppercase, 6)

# Add result calculation code
import math

def calculate(len_m: float, len_n: float, len_p: float) -> float:
    """
    题意：矩形 ABCD，P 在平面外且 PA ⟂ 平面 ABCD，Q 为 PA 的中点。
          AB = len_m, BC = len_n, PA = len_p。求点 P 到平面 QBD 的距离。

    推导（在函数中按步骤实现，不直接一行套最终公式）：
    1) 由对称性：dist(P, 平面QBD) = dist(A, 平面QBD)。
    2) 设 E 为 A 到 BD 的垂足，则面(QAE) ⟂ 面(QBD)，交线 QE。
       因此 dist(A, 平面QBD) = AH，其中 AH ⟂ QE。
    3) 计算相关量：
       QA = len_p / 2
       BD = sqrt(len_m^2 + len_n^2)
       AE = 面积(ABCD)/BD = (len_m * len_n)/BD
       QE = sqrt(QA^2 + AE^2)
    4) 由 Rt△QAE 的面积守恒：
       (1/2)*QA*AE = (1/2)*QE*AH  ⇒  AH = (QA*AE)/QE
    5) 这即为所求距离。
    """
    if len_m <= 0 or len_n <= 0 or len_p <= 0:
        raise ValueError("len_m, len_n, len_p 必须为正数。")

    # Step 1: 基本量
    QA = 0.5 * len_p
    BD = math.hypot(len_m, len_n)                 # √(m^2 + n^2)
    AE = (len_m * len_n) / BD                     # A 到 BD 的距离
    QE = math.hypot(QA, AE)                       # √(QA^2 + AE^2)

    # Step 2: 面积法得到的垂距
    AH = (QA * AE) / QE

    # Step 3: 由对称性 dist(P, 平面QBD) = dist(A, 平面QBD) = AH
    return AH


# =========================
# 题干参数变量定义（端点变量不需要定义）
# 注：本题未给具体数值，以下为示例值，便于本地自检；若有原题数值，请替换。
# =========================
len_m = 3.0   # 示例：AB
len_n = 4.0   # 示例：BC
len_p = 5.0   # 示例：PA

# =========================
# 验证与输出（验证通过后按流程应注释）
# =========================
#result = calculate(len_m=len_m, len_n=len_n, len_p=len_p)
# # 对照：化简公式  AH = (p*m*n) / sqrt(p^2*(m^2+n^2) + 4*m^2*n^2)
#expected = (len_p * len_m * len_n) / math.sqrt((len_p**2)*(len_m**2 + len_n**2) + 4*(len_m**2)*(len_n**2))
#print(f"距离(推导实现) = {result:.10f}")
#print(f"对照(化简闭式) = {expected:.10f}")
#print("是否一致：", math.isclose(result, expected, rel_tol=1e-12, abs_tol=1e-12))

# Generate random lengths
len_m = round(len_scaling_factor * float(len_m), 2)
len_n = round(len_scaling_factor * float(len_n), 2)
len_p = round(len_scaling_factor * float(len_p), 2)

# Calculate the result
result = calculate(len_m, len_n, len_p)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_5_17",
    "type": 3,
    "level": 2,
    "cn_problem": f"已知矩形{point_A}{point_B}{point_C}{point_D}，点{point_P}在平面{point_A}{point_B}{point_C}{point_D}外，且{point_P}{point_A} ⊥ 平面{point_A}{point_B}{point_C}{point_D}。{point_Q}为{point_P}{point_A}的中点，设{point_A}{point_B} = {len_m}，{point_B}{point_C} = {len_n}，{point_P}{point_A} = {len_p}，求点{point_P}到平面{point_Q}{point_B}{point_D}的距离。",
    "en_problem": f"Given rectangle {point_A}{point_B}{point_C}{point_D}, point {point_P} is outside plane {point_A}{point_B}{point_C}{point_D}, and {point_P}{point_A} ⊥ plane {point_A}{point_B}{point_C}{point_D}. {point_Q} is the midpoint of {point_P}{point_A}. Let {point_A}{point_B} = {len_m}, {point_B}{point_C} = {len_n}, {point_P}{point_A} = {len_p}. Find the distance from point {point_P} to plane {point_Q}{point_B}{point_D}.",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_5_17({mode}, {azimuth}, {elevation}, '{point_A}', '{point_B}', '{point_C}', '{point_D}', '{point_P}', '{point_Q}')"}, ensure_ascii=False) + "\n")
