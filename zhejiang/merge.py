
import json  
  
# 假设有三个JSONL文件：file1.jsonl, file2.jsonl, file3.jsonl  
files = ['input_data/82/zhejiang/train_processed.jsonl', 'input_data/82/zhejiang/val_processed.jsonl', 'input_data/82/zhejiang/test_processed.jsonl']  
merged_data = []  

  
# 读取并解析每个文件的内容  
for file in files:  
    with open(file, 'r', encoding='utf-8') as f:  
        for line in f: 
            merged_data.append(json.loads(line.strip()))


# ## 将合并后的数据转换回JSONL格式并写入新文件  
# with open('input_data/82/zhejiang/all.json', 'w', encoding='utf-8') as f:  
#     # for item in merged_data:  
#     f.write(json.dumps(merged_data, ensure_ascii=False) + '\n')

# 将JSON对象列表写入一个新的JSON文件  
with open('input_data/82/zhejiang/all.json', 'w', encoding='utf-8') as f:  
    json.dump(merged_data, f, ensure_ascii=False, indent=4)