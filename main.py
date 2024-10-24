def find_farthest_point(points_list, B):
    max_distance = float('-inf')
    result = None

    for point in points_list:
        distance, position, nearest_circle_idx = B(point)
        if distance > max_distance:
            max_distance = distance
            result = (point, distance, position, nearest_circle_idx)
            
    return result

# 示例用法
# 假设你的列表是points_list，B函数已经定义
# points_list = [(x1, y1), (x2, y2), ...]
# B = lambda point: (distance, position, nearest_circle_idx)

# result = find_farthest_point(points_list, B)
# print(result)
