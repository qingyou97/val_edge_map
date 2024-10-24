import matplotlib.pyplot as plt
import numpy as np
import math

def distance_point_to_circle(px, py, cx, cy, r):
    # 计算点 (px, py) 到圆心 (cx, cy) 的欧氏距离
    center_distance = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
    # 垂直距离是欧氏距离减去圆的半径
    return abs(center_distance - r)

def find_nearest_circle(px, py, circles):
    # 储存最小距离和最近圆的索引
    min_distance = float('inf')
    nearest_circle_idx = -1
    for idx, (cx, cy, r) in enumerate(circles):
        dist = distance_point_to_circle(px, py, cx, cy, r)
        if dist < min_distance:
            min_distance = dist
            nearest_circle_idx = idx
    return nearest_circle_idx, min_distance

def plot_circles_and_point(px, py, circles, nearest_circle_idx):
    plt.figure(figsize=(4, 4))
    ax = plt.gca()
    ax.set_xlim([0, 224])
    ax.set_ylim([0, 224])
    
    for (cx, cy, r) in circles:
        circle = plt.Circle((cx, cy), r, fill=False)
        ax.add_patch(circle)
    
    # 标记给定的点
    plt.plot(px, py, 'bo') # 使用蓝色点标记
    
    # 画出默线
    nearest_circle = circles[nearest_circle_idx]
    cx, cy, r = nearest_circle
    vector = [(px - cx, py - cy) for _ in range(1)]
    unit_vector = (vector[0][0] / np.linalg.norm(vector), vector[0][1] / np.linalg.norm(vector))
    edge_point_x = cx + unit_vector[0] * r
    edge_point_y = cy + unit_vector[1] * r
    plt.plot([px, edge_point_x], [py, edge_point_y], 'r-') # 红线作为垂直距离
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    
def main(px, py, circles):
    nearest_circle_idx, min_distance = find_nearest_circle(px, py, circles)
    print(f"点到最近圆的垂直距离为 {min_distance:.2f}")
    print(f"最近的圆是: 圆心 ({circles[nearest_circle_idx][0]}, {circles[nearest_circle_idx][1]}), 半径 {circles[nearest_circle_idx][2]}")
    plot_circles_and_point(px, py, circles, nearest_circle_idx)

# 输入给定的点和四个圆的数据
px = 100  # 给出的点的x坐标
py = 150  # 给出的点的y坐标
circles = [(50, 50, 20), (160, 160, 30), (80, 180, 25), (200, 200, 15)]

# 调用主函数
main(px, py, circles)
