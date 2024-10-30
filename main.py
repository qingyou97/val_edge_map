def plot_line_and_intersection(line_points, square_points, intersection):
    fig, ax = plt.subplots()
    
    # 绘制正方形
    square = plt.Polygon(square_points, closed=True, fill=None, edgecolor='blue')
    ax.add_patch(square)
    
    # 绘制线段
    x, y = zip(*line_points)
    ax.plot(x, y, 'r--', label='Original Line')
    
    # 如果有交点，绘制交点
    if intersection:
        if intersection.geom_type == 'LineString':
            # 提取 LineString 中的点
            points = list(intersection.coords)
            # 找到 x 坐标更小的点
            min_x_point = min(points, key=lambda point: point[0])
            ax.plot(min_x_point[0], min_x_point[1], 'go', label='Intersection Point')
            # 绘制延长线
            extended_x = [line_points[0][0], min_x_point[0]]
            extended_y = [line_points[0][1], min_x_point[1]]
            ax.plot(extended_x, extended_y, 'g-', label='Extended Line')
        else:
            print("交点类型不支持。")
    
    ax.set_xlim(50, 70)
    ax.set_ylim(40, 60)
    ax.set_aspect('equal', 'box')
    plt.legend(loc='upper left')
    
    plt.title('Line and Intersection with Square')
    plt.show()
