import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon
import numpy as np

def plot_square_and_lines(rotated_square, points_inside):
    fig, ax = plt.subplots()
    square = plt.Polygon(rotated_square, closed=True, fill=None, edgecolor='blue')
    ax.add_patch(square)
    
    polygon = Polygon(rotated_square)
    top_side_vector = (rotated_square[1][0] - rotated_square[0][0], rotated_square[1][1] - rotated_square[0][1])
    perpendicular_vector = (-top_side_vector[1], top_side_vector[0])
    
    lines = []
    lines_points_dicts = []
    
    for x, y in points_inside:
        line = LineString([(x - 1000 * perpendicular_vector[0], y - 1000 * perpendicular_vector[1]),
                           (x + 1000 * perpendicular_vector[0], y + 1000 * perpendicular_vector[1])])
        
        line_points = []
        for px, py in points_inside:
            if line.distance(Point(px, py)) < 1e-9:
                line_points.append((px, py))
        
        if line_points and line_points not in lines_points_dicts:
            lines.append(line)
            lines_points_dicts.append(line_points)
    
    # 计算每对直线之间的距离
    min_distance = float('inf')
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            distance = lines[i].distance(lines[j])
            if distance < min_distance:
                min_distance = distance
    
    # 设置合并阈值，增大一些
    merge_threshold = min_distance * 2.0  # 增大阈值以合并更多点
    
    # 合并直线
    merged_lines_points = []
    used = [False] * len(lines)
    
    for i in range(len(lines)):
        if used[i]:
            continue
        current_line_points = set(lines_points_dicts[i])
        for j in range(i + 1, len(lines)):
            if not used[j] and lines[i].distance(lines[j]) < merge_threshold:
                current_line_points.update(lines_points_dicts[j])
                used[j] = True
        merged_lines_points.append(list(current_line_points))
        used[i] = True
    
    # 绘制合并后的线
    for line_points in merged_lines_points:
        if len(line_points) > 1:
            x_coords, y_coords = zip(*line_points)
            ax.plot(x_coords, y_coords, '--', label=f"Crosses {line_points}")
    
    # 绘制点
    x_coords, y_coords = zip(*points_inside)
    ax.scatter(x_coords, y_coords, color='red')

    ax.set_xlim(50, 70)
    ax.set_ylim(40, 60)
    ax.set_aspect('equal', 'box')
    plt.legend(loc='upper left')
    
    plt.title('Merged Perpendicular Lines Inside Rotated Square')
    plt.show()
    return merged_lines_points

# 示例数据
rotated_square = [(55, 45), (65, 45), (65, 55), (55, 55)]
points_inside = [(60, 50), (62, 52), (58, 48), (61, 51)]

# 调用函数
merged_lines_data = plot_square_and_lines(rotated_square, points_inside)
print("Merged lines passing through these points:", merged_lines_data)
