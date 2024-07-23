# 按照 recall 大小排序
sorted_results = sorted(results_list, key=lambda x: x['recall'], reverse=True)

# 保存排序结果到 log.txt
with open('log.txt', 'w') as f:
    for params in sorted_results:
        f.write(str(params) + '\
')

# 打印 top3 的组
print("Top 3 parameters with highest recall:")
for i, params in enumerate(sorted_results[:3]):
    print(f"Rank {i+1}:")
    for key, value in params.items():
        print(f"{key}: {value}")
    print()  # 空行分隔每组参数
