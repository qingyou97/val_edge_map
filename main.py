def cal_magnitude(point):
    # 这是一个示例函数，需要你自己定义
    # 根据 (x, y) 点返回一个值
    x, y = point
    return x * y  # 举例：返回 x*y, 你可以换成实际的计算方式

def calculate_average(points):
    if not points:
        return 0  # 如果列表为空，返回0
    
    total_magnitude = 0
    for point in points:
        magnitude = cal_magnitude(point)
        total_magnitude += magnitude
    
    average_magnitude = total_magnitude / len(points)
    return average_magnitude

# 示例用法：
points_list = [(3, 2), (3, 3), (4, 2), (4, 3)]
average = calculate_average(points_list)
print(average)
