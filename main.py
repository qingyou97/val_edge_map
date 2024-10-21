def find_y_with_max_value(coords_and_intensities):
    # 用一个字典来存储每个 y 的强度值总和
    y_intensity_dict = {}
    
    # 遍历整个列表
    for item in coords_and_intensities:
        coord, intensity = item
        x, y = coord
        
        if y not in y_intensity_dict:
            y_intensity_dict[y] = 0
        
        y_intensity_dict[y] += intensity
    
    # 找到五分之一强度值之和最大的 y
    max_value = 0
    max_y = None
    
    for y, total_intensity in y_intensity_dict.items():
        average_intensity = total_intensity / 5
        if average_intensity > max_value:
            max_value = average_intensity
            max_y = y
    
    return max_y

# 示例列表
coords_and_intensities = [[(1, 1), 3], [(1, 2), 3], [(2, 2), 3]]

# 调用函数并打印结果
print(find_y_with_max_value(coords_and_intensities))
