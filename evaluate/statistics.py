import json

filename = "response_with_res.jsonl"
total = 0
count_res_1 = 0

with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        entry = json.loads(line)
        total += 1
        if entry.get("res") == 1:
            count_res_1 += 1

if total > 0:
    ratio = count_res_1 / total
else:
    ratio = 0.0

print(ratio)