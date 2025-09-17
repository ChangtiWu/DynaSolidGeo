import os
import subprocess
import argparse
from tqdm import tqdm
def run_all_python_files(mode=0, seed=0):
    # Files to skip
    skip_files = []
    
    code_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../code/python'))
    # py_files = [f for f in os.listdir(code_dir) if f.endswith('.py')]
    py_files = [f for f in os.listdir(code_dir) if f.endswith('.py') and f not in skip_files]
    for filename in tqdm(py_files, desc="Running Python files"):
        file_path = os.path.join(code_dir, filename)
        cmd = ['python', file_path, '--mode', str(mode), '--seed', str(seed)]
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running {filename}: {e}")
        except Exception as e:
            print(f"Unexpected error running {filename}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch run all python files in ../code/python with mode and seed arguments.")
    parser.add_argument('--mode', type=int, default=0, help='Mode parameter (default: 0)')
    parser.add_argument('--seed', type=int, default=0, help='Seed parameter (default: 0)')
    args = parser.parse_args()
    run_all_python_files(mode=args.mode, seed=args.seed)