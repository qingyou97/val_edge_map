def find_two_peak_y_values(sum_by_y):
    # 将字典按值排序，得到一个列表，元素为 (y, strength) 元组
    sorted_items = sorted(sum_by_y.items(), key=lambda item: item[1], reverse=True)
    
    # 取出前两个极大值点的 y 值
    peak_y_values = [sorted_items[0][0], sorted_items[1][0]]
    
    return peak_y_values

# 示例数据字典
coords_dict = {(20, 37): 9.055385138137417, (20, 38): 47.01063709417264, 
               (20, 39): 77.05841939723393, (20, 40): 65.06919393998976, 
               (21, 26): 0.0}

# 计算每个 y 的强度总和
sum_by_y = sum_strengths_by_y(coords_dict)

# 找到两个峰值的极大值点
peak_y_values = find_two_peak_y_values(sum_by_y)

print(peak_y_values)
