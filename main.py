def find_min_five_intensities(data):
    """
    从包含坐标和强度值的列表中找到强度值最小的五个及其对应的坐标。
    
    :param data: list of lists, 形如 [[(x, y), intensity], ...]
    :return: list of tuples, 每个元素为 (coordinate, intensity)
    """
    if not data:
        return []

    # 按强度值排序
    sorted_data = sorted(data, key=lambda x: x[1])

    # 取前五个
    min_five = sorted_data[:5]

    return min_five

# 示例用法
data = [[(220, 116), 284.0633732109791], 
        [(215, 122), 180.0567890], 
        [(210, 118), 300.56473820],
        [(225, 120), 150.1234567],
        [(230, 125), 200.9876543],
        [(235, 130), 100.4567890],
        [(240, 135), 250.1234567]]

min_five = find_min_five_intensities(data)
for coordinate, intensity in min_five:
    print(f"强度值: {intensity}, 坐标: {coordinate}")
