import os
import json
from tqdm import tqdm
from datasets import Dataset, Features, Image, Value, Sequence

DATA_ROOT = os.path.join(os.path.dirname(__file__), "..", "data")
SEEDS = [f"seed_{i}" for i in range(5)]  # seed_0 ... seed_4
PROBLEM_FILE = "problem.jsonl"
OUTPUT_PARQUET = os.path.join(os.path.dirname(__file__), "..", "seed0_4_exported.parquet")

def path_to_bytes(path: str) -> dict | None:
    """读入图片并返回 {'bytes': <bytes>, 'path': <relative>}；不存在返回 None"""
    if not os.path.exists(path):
        print(f"警告: 图像不存在: {path}")
        return None
    try:
        with open(path, "rb") as f:
            return {"bytes": f.read(), "path": os.path.relpath(path, start=os.path.join(DATA_ROOT))}
    except Exception as e:
        print(f"读取图像失败: {path} -> {e}")
        return None

def load_seed_items(seed_dir: str) -> list[dict]:
    items = []
    jsonl_path = os.path.join(seed_dir, PROBLEM_FILE)
    if not os.path.exists(jsonl_path):
        print(f"警告: 缺少 {jsonl_path}，跳过该seed")
        return items

    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                # 兼容偶发的注释或无效行
                continue

            # 组装输出字段（与给定示例保持相同字段名）
            cn = obj.get("cn_problem", "")
            en = obj.get("en_problem", "")
            problem_text = en or cn or ""
            problem = "<image>" + problem_text

            # 解析图片（数据里通常是单图）
            rel_img = obj.get("image", "")  # 如: images/xxx.png
            images = []
            if rel_img:
                full_path = os.path.join(seed_dir, rel_img)
                img_rec = path_to_bytes(full_path)
                if img_rec:
                    images.append(img_rec)

            answer = str(obj.get("solution", ""))

            items.append({
                "problem": problem,
                "images": images,
                "answer": answer
            })
    return items

def convert_to_parquet():
    all_rows: list[dict] = []

    # 汇总 seed_0 ~ seed_4
    print(f"开始汇总数据于: {DATA_ROOT}")
    for seed in SEEDS:
        seed_dir = os.path.join(DATA_ROOT, seed)
        print(f"- 处理 {seed_dir}")
        rows = load_seed_items(seed_dir)
        all_rows.extend(rows)

    print(f"总题目数: {len(all_rows)}")

    # 定义 schema（与示例脚本一致）
    schema = Features({
        "problem": Value("string"),
        "images": Sequence(Image(decode=False)),
        "answer": Value("string"),
    })

    if not all_rows:
        print("没有可导出的数据")
        return

    ds = Dataset.from_list(all_rows).cast(schema)
    print(f"创建的数据集: {ds}")
    print(f"开始保存为 parquet -> {OUTPUT_PARQUET}")
    ds.to_parquet(OUTPUT_PARQUET)
    print(f"✅ 已保存: {OUTPUT_PARQUET}")

def verify_parquet():
    try:
        from datasets import load_dataset
        if not os.path.exists(OUTPUT_PARQUET):
            print("未找到导出的 parquet 文件")
            return
        ds = load_dataset("parquet", data_files=OUTPUT_PARQUET)["train"]
        print(ds.features)
        if len(ds) > 0 and ds[0]["images"]:
            first_img = ds[0]["images"][0]
            path = first_img.get("path", "<no-path>")
            b = first_img.get("bytes", b"")
            print(f"首条记录图像: path={path}, bytes={len(b)} 字节")
        print(f"样例: {ds[0] if len(ds)>0 else '空数据'}")
    except Exception as e:
        print(f"验证失败: {e}")

if __name__ == "__main__":
    convert_to_parquet()
    print("\n开始验证生成的 parquet 文件...")
    verify_parquet()