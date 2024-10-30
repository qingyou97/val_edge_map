import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point, Polygon, LineString

# 定义函数绘制正方形和点
def plot_square_and_lines(rotated_square, points_inside):
    # 计算正方形左右边的中点向量以获得垂直向量
    left_side_midpoint = ((rotated_square[0][0] + rotated_square[3][0]) / 2,
                          (rotated_square[0][1] + rotated_square[3][1]) / 2)
    right_side_midpoint = ((rotated_square[1][0] + rotated_square[2][0]) / 2,
                           (rotated_square[1][1] + rotated_square[2][1]) / 2)
                          
    # 计算方向向量，为垂直于正方形左右边线的单位向量
    side_dir = (right_side_midpoint[0] - left_side_midpoint[0], right_side_midpoint[1] - left_side_midpoint[1])
    perpendicular_dir = (-side_dir[1], side_dir[0]) 

    # 创建画布
    fig, ax = plt.subplots()
    # 绘制正方形
    square = plt.Polygon(rotated_square, closed=True, fill=None, edgecolor='blue')
    ax.add_patch(square)
    
    polygon = Polygon(rotated_square)
    lines_points_dicts = []
    
    for x, y in points_inside:
        current_line_points = []
        # 创建一条线，即在右方向的足够长度
        line = LineString([Point(x - 1000*perpendicular_dir[0], y - 1000*perpendicular_dir[1]),
                           Point(x + 1000*perpendicular_dir[0], y + 1000*perpendicular_dir[1])])
        
        # 检查线在哪些点处，也是对所有的点集进行削减观察
        line_points = {}
        for px, py in points_inside:
            
            if line.distance(Point(px, py)) < 1e-9:  # 当距离足够小认为位于同一线上
                if px != x or py != y:  # 不计其自身点
                    line_points[(px, py)] = line_points.get((px, py),0) + 1

        
        if line_points and line_points not in lines_points_dicts:
            # 如果这条线没有统计过则绘制
            lines_points_dicts.append(line_points)
            ax.plot([line.coords[0][0], line.coords[1][0]], [line.coords[0][1], line.coords[1][1]],
                    '--', label=f"Crosses {', '.join(str(pt) for pt in line_points)}")
            
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
