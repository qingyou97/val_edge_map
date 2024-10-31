import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString, Polygon

def extend_line_and_find_intersection(line_points, square_points, slope=None):
    if len(line_points) != 2 and slope is None:
        if len(line_points) > 1:
            # 使用第一个和最后一个点计算斜率
            dx = line_points[-1][0] - line_points[0][0]
            dy = line_points[-1][1] - line_points[0][1]
            slope = dy / dx if dx != 0 else float('inf')
        else:
            # 一个点时，计算垂直向量方向（这里假设垂直方向斜率为正无穷，即竖直线）
            slope = float('inf')

    if slope is not None:
        # 第一个点坐标
        x1, y1 = line_points[0]
        # 如果斜率是无穷大，意味着垂直线，我们直接构建与x平行的线
        if np.isinf(slope):
            extended_line = LineString([(x1, y) for y in range(40, 70)])  # 包含整个可能的y轴范围
        else:
            # 通过第一个点和斜率创建一个扩展的line_string
            def y(x):
                return y1 + slope * (x - x1)
            x_coords = np.linspace(50, 70, 500)  # x范围可以适当调整
            extended_line = LineString([(x, y(x)) for x in x_coords])
    else:
        # 如果有有效的两个点，正常扩展线
        extended_line = LineString(line_points)

    # 创建正方形
    square = Polygon(square_points)

    # 查找交点
    intersection = square.intersection(extended_line)

    return intersection

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
        if intersection.geom_type == 'LineString' or intersection.geom_type == 'Point':
            # 提取 LineString 中的点或单个点
            points = list(intersection.coords)
            min_x_point = min(points, key=lambda point: point[0])
            ax.plot(min_x_point[0], min_x_point[1], 'go', label='Intersection Point')
        else:
            print(f"Unsupported intersection type: {intersection.geom_type}")

    ax.set_xlim(50, 70)
    ax.set_ylim(40, 60)
    ax.set_aspect('equal', 'box')
    plt.legend(loc='upper left')

    plt.title('Line and Intersection with Square')
    plt.show()

# 示例数据
line_points = [(59, 50)]  # 只有一个点
square_points = [(55, 45), (65, 45), (65, 55), (55, 55)]  # 正方形的四个顶点
given_slope = 0.5  # 给定的斜率

# 查找交点
intersection = extend_line_and_find_intersection(line_points, square_points, slope=given_slope)

# 绘制线段和交点
plot_line_and_intersection(line_points, square_points, intersection)
