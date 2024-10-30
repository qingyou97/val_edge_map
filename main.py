def points_in_square(square_center, size, points_list):
    # 计算正方形的边界
    left = square_center[0]
    top = square_center[1] - size // 2
    right = left + size
    bottom = top + size
    
    # 找出在正方形内的点
    points_in_square = [
        (x, y) for (x, y) in points_list
        if left <= x < right and top <= y < bottom
    ]
    
    return points_in_square

# 示例使用
square_center = (57, 51)
size = 5
points_list = [(2, 3), (4, 5), (57, 50), (58, 51), (59, 52)]
result = points_in_square(square_center, size, points_list)
print(result)
