import os
import json
from tqdm import tqdm
import matlab.engine

# 构造matlab_cmd.jsonl的路径
# 获取当前文件的上一级目录作为项目的根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
jsonl_path = os.path.join(base_dir, 'data', 'matlab_cmd.jsonl')

matlab_code_dir = os.path.join(base_dir, 'code', 'matlab')
os.chdir(matlab_code_dir)
print(matlab_code_dir)

# 读取所有命令
cmds = []
with open(jsonl_path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
            for v in entry.values():
                cmds.append(v)
        except Exception as e:
            print(f"Error parsing line: {line}\n{e}")

if not cmds:
    print("No commands found.")
else:
    # Only execute commands starting with 'sup'
    # cmds = [cmd for cmd in cmds if cmd.startswith('hsmcel')]

    eng = matlab.engine.start_matlab()
    for cmd in tqdm(cmds, desc="Executing MATLAB commands"):
        try:
            eng.eval(cmd, nargout=0)
        except Exception as e:
            print(f"Error executing: {cmd}\n{e}")
    eng.quit()

