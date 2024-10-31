def get_all_points(vertices):
    # 提取所有 x 和 y 坐标
    x_coords = [vertex[0] for vertex in vertices]
    y_coords = [vertex[1] for vertex in vertices]
    
    # 确定边界
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)
    
    # 用列表推导式来生成所有整点坐标
    points = [(x, y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1)]
    
    return points

# 示例顶点输入（格式为(行, 列))
vertices = [(2, 2), (2, 5), (5, 2), (5, 5)]

result_points = get_all_points(vertices)
print(result_points)
