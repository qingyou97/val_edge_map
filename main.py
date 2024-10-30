import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon

# 定义函数绘制正方形和线
def plot_square_and_lines(rotated_square, points_inside):
    # 创建画布
    fig, ax = plt.subplots()
    # 绘制正方形
    square = plt.Polygon(rotated_square, closed=True, fill=None, edgecolor='blue')
    ax.add_patch(square)
    
    # 创建多边形对象
    polygon = Polygon(rotated_square)
    
    # 存储每条线经过的点
    lines_points_dicts = []
    
    # 遍历每个点
    for x, y in points_inside:
        # 创建一条垂直线
        line = LineString([(x, polygon.bounds[1] - 10), (x, polygon.bounds[3] + 10)])
        
        # 检查线经过的点
        line_points = []
        for px, py in points_inside:
            if line.distance(Point(px, py)) < 1e-9:  # 判断点是否在直线上
                line_points.append((px, py))
        
        # 如果这条线没有统计过则绘制
        if line_points and line_points not in lines_points_dicts:
            lines_points_dicts.append(line_points)
            ax.plot([x, x], [polygon.bounds[1] - 10, polygon.bounds[3] + 10], '--', label=f"Crosses {line_points}")
    
    # 绘制点
    x_coords, y_coords = zip(*points_inside)
    ax.scatter(x_coords, y_coords, color='red')

    ax.set_xlim(50, 70)
    ax.set_ylim(40, 60)
    ax.set_aspect('equal', 'box')
    plt.legend(loc='upper left')
    
    plt.title('Perpendicular Lines Inside Rotated Square')
    plt.show()
    return lines_points_dicts

# 调用函数
lines_data = plot_square_and_lines(rotated_square, points_inside)
print("Lines passing through these points:", lines_data)
