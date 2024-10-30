import matplotlib.pyplot as plt
from shapely.geometry import LineString, Polygon

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

# 示例数据
line_points = [(59, 50), (63, 49)]  # Line 5 的点
square_points = [(55, 45), (65, 45), (65, 55), (55, 55)]  # 正方形的四个顶点

# 查找交点
intersection = extend_line_and_find_intersection(line_points, square_points)

# 绘制线段和交点
plot_line_and_intersection(line_points, square_points, intersection)
