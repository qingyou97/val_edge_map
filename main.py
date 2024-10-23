def find_min_intensity(data):
    """
    从包含坐标和强度值的列表中找到强度值的最小值及其对应的坐标。
    
    :param data: list of lists, 形如 [[(x, y), intensity], ...]
    :return: (tuple, float), 最小强度值和对应的坐标
    """
    if not data:
        return None, None

    min_intensity = float('inf')
    min_coordinate = None

    for item in data:
        coordinate, intensity = item
        if intensity < min_intensity:
            min_intensity = intensity
            min_coordinate = coordinate

    return min_coordinate, min_intensity

# 示例用法
data = [[(220, 116), 284.0633732109791], 
        [(215, 122), 180.0567890], 
        [(210, 118), 300.56473820]]

coordinate, min_intensity = find_min_intensity(data)
print(f"最小强度值为: {min_intensity}, 对应的坐标为: {coordinate}")
