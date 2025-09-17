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
point_A, point_B, point_C, point_D, point_E, point_A1, point_B1, point_C1, point_D1, point_E1 = random.sample(string.ascii_uppercase, 10)

# Add result calculation code
def calculate():
    return 170

#result=calculate()
#print(result)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_13_17",
    "type": 6,
    "level": 3,
    "cn_problem": f"如图，以正五棱柱{point_A}{point_B}{point_C}{point_D}{point_E}-{point_A1}{point_B1}{point_C1}{point_D1}{point_E1}的顶点为顶点的四棱锥共有多少个？",
    "en_problem": f"As shown in Figure, how many quadrilateral pyramids can be formed using the vertices of regular pentagonal prism {point_A}{point_B}{point_C}{point_D}{point_E}-{point_A1}{point_B1}{point_C1}{point_D1}{point_E1}?",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_13_17({mode}, {azimuth}, {elevation},'{point_A}','{point_B}','{point_C}','{point_D}','{point_E}','{point_A1}','{point_B1}','{point_C1}','{point_D1}','{point_E1}')"}, ensure_ascii=False) + "\n")
