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

# Add result calculation code
def calculate():
    return 6

#result=calculate()
#print(result)

# Calculate the result
result = calculate()

# ─── 1. save JSON ─────────────────────────────── 
json_data = {
    "id": "hsmcel_t_13_14",
    "type": 6,
    "level": 3,
    "cn_problem": f"若干个正方体形状的积木按图所示摆成塔形，上面正方体中下底面的四个顶点是下面正方体上底面各边的中点，最下面的正方体的棱长为1，且平放于桌面上。如果所有正方体直接看到的表面积超过8.8，则所有正方体的个数至少是______个。",
    "en_problem": f"Several cube-shaped blocks are stacked in a tower formation as shown in Figure. The four vertices of the bottom face of each upper cube are the midpoints of the edges of the top face of the cube below it. The bottom cube has edge length 1 and lies flat on the table. If the total visible surface area of all cubes exceeds 8.8, what is the minimum number of cubes? ______",
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
    f.write(json.dumps({json_data["id"]: f"hsmcel_t_13_14({mode}, {azimuth}, {elevation})"}, ensure_ascii=False) + "\n")
