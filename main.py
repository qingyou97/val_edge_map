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
        ax.plot(intersection.x, intersection.y, 'go', label='Intersection Point')
        # 绘制延长线
        extended_x = [line_points[0][0], intersection.x]
        extended_y = [line_points[0][1], intersection.y]
        ax.plot(extended_x, extended_y, 'g-', label='Extended Line')
    
    ax.set_xlim(50, 70)
    ax.set_ylim(40, 60)
    ax.set_aspect('equal', 'box')
    plt.legend(loc='upper left')
    
    plt.title('Line and Intersection with Square')
    plt.show()
