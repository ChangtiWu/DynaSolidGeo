import os
import re
import json
import base64
import argparse
import asyncio
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

try:
    from openai import AsyncOpenAI
    BASE_URL = os.getenv('BASE_URL', 'https://api.openai.com/v1')  # 提供默认值
    API_KEY = os.getenv('API_KEY', 'DONT_FINE_OPENAI_KEY')  # 提供默认值
    MODEL_NAME= os.getenv('MODEL_NAME', 'gpt-4o')  # 提供默认值
    if API_KEY == 'DONT_FINE_OPENAI_KEY':
        raise ValueError("API key for OpenAI is not set. Please set the API_KEY environment variable.")
    client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)
except ImportError:
    print("To use openai, please install it first by running `pip install openai`.")

USER_PROMPT = r'''
Please answer the problem based on the image or video.

Answering Format:
1. You may include reasoning steps before the final answer.
2. The final specific answer MUST be placed on the last line only.
3. The final specific answer MUST be wrapped in \boxed{}.
4. Do NOT include variable names, equal signs, or extra text inside \boxed{}.
   - For example, write \boxed{5}, NOT \boxed{a = 5}.

Example:
Q: Solve for x: 2x = 10.
A: Dividing both sides by 2, we get x = 5.
\boxed{5}
'''.strip()

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return f"data:image/jpeg;base64,{base64.b64encode(image_file.read()).decode('utf-8')}"

def load_completed_ids(output_file):
    """读取已完成的题目ID列表"""
    completed_ids = set()
    if os.path.exists(output_file):
        try:
            with open(output_file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        data = json.loads(line)
                        if "id" in data:
                            completed_ids.add(data["id"])
        except Exception as e:
            print(f"Warning: Error reading existing output file: {e}")
    return completed_ids

async def process_single_item(item, input_file_dir, model_name, semaphore):
    """处理单个题目的异步函数"""
    async with semaphore:  # 限制并发数
        try:
            item_id = item.get("id", "NOT_FOUND")
            en_problem = item.get("en_problem", "NOT_FOUND")
            image_path = item.get("image", "NOT_FOUND")
            solution = item.get("solution", "NOT_FOUND")  # 获取GT解答

            if item_id == "NOT_FOUND" or en_problem == "NOT_FOUND" or image_path == "NOT_FOUND" or solution == "NOT_FOUND":
                raise ValueError(f"Missing required fields for item {item_id}")
            
            full_image_path = os.path.join(input_file_dir, image_path)
            if not os.path.exists(full_image_path):
                raise FileNotFoundError(f"Image file {full_image_path} does not exist for item {item_id}")
            
            image_base64 = encode_image_to_base64(full_image_path)
            
            completion = await client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "https://github.com/ChangtiWu/DynaSolidGeo",
                    "X-Title": "DynaSolidGeo Evaluation",
                },
                extra_body={},
                model=model_name,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "image_url", "image_url": {"url": image_base64}},
                            {"type": "text", "text": en_problem + "\n\n-----\n\n" + USER_PROMPT},
                        ]
                    }
                ],
                temperature=0.0
            )
            response_text = completion.choices[0].message.content
            
            return {
                "id": item_id,
                "response": response_text,
                "solution": solution  # 添加GT解答
            }
            
        except Exception as e:
            print(f"Error processing item {item.get('id', 'NOT_FOUND')}: {e}")
            return {
                "id": item.get("id", "NOT_FOUND"),
                "response": f"ERROR: {str(e)}",
                "solution": item.get("solution", "NOT_FOUND")  # 即使出错也返回GT
            }

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, help="Path to the input JSONL file.")
    parser.add_argument("--output_file", default=None, type=str, help="Path to the output JSONL file for final answers.")
    parser.add_argument("--model_name", type=str, default=None, help="The model name to use for generation.")
    parser.add_argument("--max_concurrent", type=int, default=5, help="Maximum number of concurrent requests.")
    return parser.parse_args()

async def main():
    args = parse_args()
    input_file = args.input_file
    output_file = args.output_file
    model_name = args.model_name if args.model_name else MODEL_NAME
    max_concurrent = args.max_concurrent
    
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist.")
    input_file_dir = os.path.dirname(input_file)
    
    if not output_file:
        output_file = os.path.join(input_file_dir, "response.jsonl")
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # 读取已完成的题目ID
    completed_ids = load_completed_ids(output_file)
    print(f"Found {len(completed_ids)} already completed items.")
    
    # 读取所有输入数据
    all_items = []
    with open(input_file, "r", encoding="utf-8") as fin:
        for line in fin:
            if line.strip():
                item = json.loads(line)
                # 跳过已完成的题目
                if item.get("id") not in completed_ids:
                    all_items.append(item)
    
    print(f"Total items to process: {len(all_items)}")
    
    if not all_items:
        print("No new items to process.")
        return
    
    # 创建信号量来限制并发数
    semaphore = asyncio.Semaphore(max_concurrent)
    
    # 创建异步任务
    tasks = [process_single_item(item, input_file_dir, model_name, semaphore) for item in all_items]
    
    # 以追加模式打开输出文件
    with open(output_file, "a", encoding="utf-8") as fout:
        # 使用asyncio.as_completed处理异步任务，配合tqdm显示进度
        completed_count = 0
        with tqdm(total=len(tasks), desc="Processing") as pbar:
            for coro in asyncio.as_completed(tasks):
                result_data = await coro
                fout.write(json.dumps(result_data, ensure_ascii=False) + "\n")
                fout.flush()  # 立即写入文件
                completed_count += 1
                pbar.update(1)

if __name__ == "__main__":
    asyncio.run(main())