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
point_A = random.sample(string.ascii_uppercase, 1)[0]

# Add result calculation code
def calculate(len_a: float) -> float:
    """计算 volume_O 的平方（公式：volume_O² = 3·len_a⁶ / 32）"""
    return (3 * (len_a ** 6)) / 32



len_a = 4.0
len_b = 8.0

# result = calculate(len_a)
# print(f"volume_O² = {result:.6f}")
# Generate random lengths
len_a = round(len_scaling_factor * float(len_a), 2)
len_b = round(len_scaling_factor * float(len_b), 2)

# Calculate the result
result = calculate(len_a)

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "aops_15_aimeII_9",
    "type": 5,
    "level": 1,
    "cn_problem": f"一个圆柱木桶装满水，圆柱底面半径为 {len_a}>0，高充足（足以保证不会溢出）。现把一边长为 {len_b}\\ ({len_b}> {len_a}\\sqrt{3/2})$ 的实心正方体缓缓放入桶中，方式如下：立方体的体对角线竖直朝下；立方体最低的那个顶点 {point_A} 先接触水面后继续下沉，直至立方体与桶内壁恰好在 {point_A} 处相切——此时桶壁与立方体仅在从 {point_A} 发出的三条棱上各切于一点；三个切点在同一水平截面上，构成等边三角形。设被排开的水体积为 volume_O。求 volume_O^2 。",
    "en_problem": f"A cylindrical wooden barrel is filled with water, with the cylinder base radius {len_a}>0 and sufficient height (to ensure no overflow). A solid cube with edge length {len_b}\\ ({len_b}> {len_a}\\sqrt{3/2}) is slowly placed into the barrel as follows: the cube's body diagonal is vertically downward; the lowest vertex {point_A} of the cube first touches the water surface and continues to sink until the cube is tangent to the barrel's inner wall at {point_A}—at this point, the barrel wall and cube are tangent only at one point on each of the three edges emanating from {point_A}; the three tangent points lie in the same horizontal cross-section, forming an equilateral triangle. Let the volume of displaced water be volume_O. Find volume_O^2.",
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
    f.write(json.dumps({json_data["id"]: f"aops_15_aimeII_9({mode}, {azimuth}, {elevation}, '{point_A}')"}, ensure_ascii=False) + "\n")
