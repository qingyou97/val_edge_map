def find_max_distance_point(points, B):
    max_distance = -1
    max_distance_point_data = {}
    
    for point in points:
        distance, position, nearest_circle_idx = B(point)
        
        if distance > max_distance:
            max_distance = distance
            max_distance_point_data = {
                'point': point,
                'distance': distance,
                'position': position,
                'nearest_circle_idx': nearest_circle_idx
            }
    
    return max_distance_point_data

# 用法举例：
# points = [(x1, y1), (x2, y2), ..., (xn, yn)]
# B函数应接收一个点（坐标）作为输入，返回 (distance, position, nearest_circle_idx)

# 示例函数B：
# def B(point):
#     # 示例实现，实际你可以定义自己的逻辑
#     x, y = point
#     distance = x**2 + y**2  # 示例计算距离（其实是距离平方）
#     position = (x, y)
#     nearest_circle_idx = ...  # 这里你需要给出你的实际逻辑
#     return (distance, position, nearest_circle_idx)

# 调用示例
# points = [(1, 2), (2, 3), (4, 5)]
# result = find_max_distance_point(points, B)
# print(result)
