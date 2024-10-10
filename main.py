import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def closest_point(input_point, points):
    distances = [calculate_distance(input_point, point) for point in points]
    min_distance = min(distances)
    closest_point_index = distances.index(min_distance)
    return points[closest_point_index]

# 示例用法
input_point = (x, y)  # 替换成你的输入点坐标
points = [(61, 67), (65, 71), (68, 74)]
nearest = closest_point(input_point, points)
print("最近的点是:", nearest)
