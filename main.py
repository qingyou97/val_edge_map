# 提取每个子list中的浮点数
times = [item[1] for item in data]

# 计算平均值
average_time = sum(times) / len(times)

print("平均计算时间为:", average_time)
