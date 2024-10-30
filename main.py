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
    
    # 计算正方形上边的方向向量
    top_side_vector = (rotated_square[1][0] - rotated_square[0][0], rotated_square[1][1] - rotated_square[0][1])
    # 计算垂直于上边的方向向量
    perpendicular_vector = (-top_side_vector[1], top_side_vector[0])
    
    # 存储每条线经过的点
    lines_points_dicts = []
    
    # 遍历每个点
    for x, y in points_inside:
        # 创建一条与正方形左右边垂直的线
        line = LineString([(x - 1000 * perpendicular_vector[0], y - 1000 * perpendicular_vector[1]),
                           (x + 1000 * perpendicular_vector[0], y + 1000 * perpendicular_vector[1])])
        
        # 检查线经过的点
        line_points = []
        for px, py in points_inside:
            if line.distance(Point(px, py)) < 1e-9:  # 判断点是否在直线上
                line_points.append((px, py))
        
        # 如果这条线没有统计过则绘制
        if line_points and line_points not in lines_points_dicts:
            lines_points_dicts.append(line_points)
            ax.plot([line.coords[0][0], line.coords[1][0]], [line.coords[0][1], line.coords[1][1]], '--', label=f"Crosses {line_points}")
    
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

# 示例数据
rotated_square = [(55, 45), (65, 45), (65, 55), (55, 55)]
points_inside = [(60, 50), (62, 52), (58, 48)]

# 调用函数
lines_data = plot_square_and_lines(rotated_square, points_inside)
print("Lines passing through these points:", lines_data)
