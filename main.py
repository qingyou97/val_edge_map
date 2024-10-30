def extend_line_and_find_intersection(line_points, square_points):
    # 创建正方形
    square = Polygon(square_points)
    
    # 创建线段
    line = LineString(line_points)
    
    # 获取线段的方向向量
    start, end = line_points
    direction = (end[0] - start[0], end[1] - start[1])
    
    # 延长线段
    extended_line = LineString([
        (start[0] - 1000 * direction[0], start[1] - 1000 * direction[1]),
        (end[0] + 1000 * direction[0], end[1] + 1000 * direction[1])
    ])
    
    # 计算交点
    intersections = extended_line.intersection(square)
    
    if intersections.is_empty:
        print("线段与正方形没有交点。")
        return None
    else:
        # 如果有多个交点，找到 x 坐标更小的点
        if intersections.geom_type == 'MultiPoint':
            intersection_points = list(intersections)
            min_x_point = min(intersection_points, key=lambda point: point.x)
        else:
            min_x_point = intersections
        
        print(f"交点坐标: {min_x_point}")
        return min_x_point
