# 找到前两个最大的值
sorted_values = sorted(result.items(), key=lambda x: x[1], reverse=True)
top_two_values = sorted_values[:2]

# 找到对应的点
top_two_points = [(point, value) for point, value in top_two_values]
