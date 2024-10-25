def sum_strengths_by_y(coordinates_dict):
    sum_by_y = {}
    
    # 遍历字典中的每个元素
    for (x, y), strength in coordinates_dict.items():
        # 如果 y 没有在结果字典中，初始化为0
        if y not in sum_by_y:
            sum_by_y[y] = 0.0
        
        # 将当前强度值加到对应 y 的总和中
        sum_by_y[y] += strength
    
    return sum_by_y

# 示例数据字典
coords_dict = {(20, 37): 9.055385138137417, (20, 38): 47.01063709417264, 
               (20, 39): 77.05841939723393, (20, 40): 65.06919393998976, 
               (21, 26): 0.0}

# 调用函数并打印结果
result = sum_strengths_by_y(coords_dict)
print(result)
