def sum_strengths_by_x(coordinates_dict):
    sum_by_x = {}
    
    # 遍历字典中的每个元素
    for (x, y), strength in coordinates_dict.items():
        # 如果 x 没有在结果字典中，初始化为0
        if x not in sum_by_x:
            sum_by_x[x] = 0.0
        
        # 将当前强度值加到对应 x 的总和中
        sum_by_x[x] += strength
    
    return sum_by_x
