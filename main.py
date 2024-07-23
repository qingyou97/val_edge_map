# 初始化最大 recall 和对应的参数组
max_recall = -1
top1_params = {}

# 遍历列表找到 recall 最大的那组参数
for params in results_list:
    if params['recall'] > max_recall:
        max_recall = params['recall']
        top1_params = params

# 打印 recall 最大的那组参数
print("Top 1 parameters with highest recall:")
print(top1_params)
