# 将所有点坐标输入B函数，并存到新的list中，同时记录坐标
results_with_coords = [(B(x, y), (x, y)) for (x, y) in red_points]

# 计算结果list的最小值及其对应的坐标
min_value, min_coords = min(results_with_coords, key=lambda item: item[0])

print(f"最小值：{min_value}, 对应的坐标：{min_coords}")
