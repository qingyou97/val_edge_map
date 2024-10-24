import cv2
import numpy as np
import math

def distance_point_to_circle(px, py, cx, cy, r):
    # 计算点 (px, py) 到圆心 (cx, cy) 的欧氏距离
    center_distance = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
    # 垂直距离是欧氏距离减去圆的半径
    return abs(center_distance - r), center_distance

def find_nearest_circle(px, py, circles):
    # 储存最小距离和最近圆的索引
    min_distance = float('inf')
    nearest_circle_idx = -1
    center_distance = 0
    for idx, (cx, cy, r) in enumerate(circles):
        dist, center_dist = distance_point_to_circle(px, py, cx, cy, r)
        if dist < min_distance:
            min_distance = dist
            nearest_circle_idx = idx
            center_distance = center_dist
    return nearest_circle_idx, min_distance, center_distance

def adjust_circle_radius(circles, nearest_circle_idx, min_distance, center_distance, px, py):
    if nearest_circle_idx == 0 and center_distance > circles[0][2] and min_distance <= 5:
        circles[0] = (circles[0][0], circles[0][1], circles[0][2] + 5)
    elif nearest_circle_idx == 1 and center_distance < circles[0][2] and min_distance <= 5:
        circles[1] = (circles[1][0], circles[1][1], circles[1][2] - 5)
    elif nearest_circle_idx == 2 and center_distance > circles[2][2] and min_distance <= 5:
        circles[2] = (circles[2][0], circles[2][1], circles[2][2] + 5)
    elif nearest_circle_idx == 3 and center_distance < circles[2][2] and min_distance <= 5:
        circles[3] = (circles[3][0], circles[3][1], circles[3][2] - 5)
    return circles

def plot_circles_and_point(px, py, circles, filename='output.png'):
    # 创建一个224x224的白色图像
    img = np.ones((224, 224, 3), dtype=np.uint8) * 255
    
    for (cx, cy, r) in circles:
        # 画圆
        cv2.circle(img, (cx, cy), r, (0, 0, 0), 1)
    
    # 标记给定的点
    cv2.circle(img, (px, py), 3, (255, 0, 0), -1) # 使用蓝色点标记
    
    # 保存图像
    cv2.imwrite(filename, img)
    
    # 显示图像
    cv2.imshow('Circles and Point', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def main(px, py, circles):
    nearest_circle_idx, min_distance, center_distance = find_nearest_circle(px, py, circles)
    nearest_circle = circles[nearest_circle_idx]
    cx, cy, r = nearest_circle
    
    if center_distance < r:
        position = "圆内"
    else:
        position = "圆外"
    
    print(f"点到最近圆的垂直距离为 {min_distance:.2f} 像素")
    print(f"最近的圆是: 圆心 ({cx}, {cy}), 半径 {r}")
    print(f"点在最近的圆的{position}")
    print(f"最近的圆是列表中的第 {nearest_circle_idx} 个圆")
    
    # 调整圆的半径
    circles = adjust_circle_radius(circles, nearest_circle_idx, min_distance, center_distance, px, py)
    
    plot_circles_and_point(px, py, circles)
    return circles

# 输入给定的点和四个圆的数据
px = 100  # 给出的点的x坐标
py = 150  # 给出的点的y坐标
circles = [(50, 50, 20), (50, 50, 30), (80, 180, 25), (80, 180, 35)]

# 调用主函数并获取更新后的圆列表
updated_circles = main(px, py, circles)
print(f"更新后的圆列表: {updated_circles}")
