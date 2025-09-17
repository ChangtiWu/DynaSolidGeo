


import os
import re
import json
import base64
from tqdm import tqdm

try:
    from openai import OpenAI
    BASE_URL = os.getenv('BASE_URL', 'https://api.openai.com/v1')  # 提供默认值
    API_KEY = os.getenv('API_KEY', 'DONT_FINE_OPENAI_KEY')  # 提供默认值
    MODEL_NAME= os.getenv('MODEL_NAME', 'gpt-4o')  # 提供默认值
    if API_KEY == 'DONT_FINE_OPENAI_KEY':
        raise ValueError("API key for OpenAI is not set. Please set the OPENAI_API_KEY environment variable.")
    client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
except ImportError:
    print("To use openai, please install it first by running `pip install openai`.")


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return f"data:image/jpeg;base64,{base64.b64encode(image_file.read()).decode('utf-8')}"




if __name__ == "__main__":
    input_file = "../data/problem.jsonl"
    output_file = "response.jsonl"
    output_cot_file = "response_cot.jsonl"

    # 如果 output_file 不存在，则新建一个空文件
    if not os.path.exists(output_file):
        with open(output_file, "w", encoding="utf-8") as f:
            pass

    # 如果 output_cot_file 不存在，则新建一个空文件
    if not os.path.exists(output_cot_file):
        with open(output_cot_file, "w", encoding="utf-8") as f:
            pass

    user_prompt = r'''
    Please answer the problem based on the image. The final specific answer MUST be wrapped in \boxed{}.
    '''

    with open(input_file, "r", encoding="utf-8") as fin, \
         open(output_file, "w", encoding="utf-8") as fout, \
         open(output_cot_file, "w", encoding="utf-8") as fout_cot:
        # 先统计总行数以便进度条显示
        fin.seek(0)
        total_lines = sum(1 for _ in fin)
        fin.seek(0)

        processed_count = 0

        for line in tqdm(fin, total=total_lines, desc="Processing"):
            item = json.loads(line)
            cn_problem = item.get("cn_problem", "")
            en_problem = item.get("en_problem", "")
            image_path = item.get("image", "")
            # 将 image_path 转换为相对于 ../data/ 的绝对路径
            if image_path:
                image_path = f"../data/{image_path}"

            if not en_problem:
                item["response"] = ""
                item_cot = item.copy()
                item_cot["response"] = ""
            else:
                content = []
                if image_path:
                    image_base64 = encode_image_to_base64(image_path)
                    content.append({"type": "image_url", "image_url": {"url": image_base64}})
                
                content.append({"type": "text", "text": en_problem+"\n\n"+user_prompt})

                completion = client.chat.completions.create(
                    extra_headers={
                        "HTTP-Referer": "https://www.baidu.com",
                        "X-Title": "My Application",
                    },
                    extra_body={},
                    model="google/gemini-2.5-pro",
                    messages=[{
                        "role": "user",
                        "content": content
                    }],
                    temperature=0.0
                )
                response_text = completion.choices[0].message.content

                item["response"] = extract_final_answer(response_text)
                item_cot = item.copy()
                item_cot["response"] = response_text
            
            fout.write(json.dumps(item, ensure_ascii=False) + "\n")
            fout_cot.write(json.dumps(item_cot, ensure_ascii=False) + "\n")

            # flush to make sure the file is written instantly every 10 items
            processed_count += 1
            if processed_count % 10 == 0:
                fout.flush()
                fout_cot.flush()