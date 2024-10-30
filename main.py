def extend_line_to_intersect(line_points, square_points):
    # 创建正方形的左侧边
    left_side = LineString([square_points[0], square_points[3]])
    
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
    intersection = extended_line.intersection(left_side)
    
    if not intersection.is_empty:
        print(f"交点坐标: {intersection}")
        return intersection
    else:
        print("线段与左侧边没有交点。")
        return None
