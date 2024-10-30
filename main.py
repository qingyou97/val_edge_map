from PIL import Image, ImageDraw
import numpy as np
from matplotlib.path import Path

def find_points_in_rotated_square(x, y, side_length, angle, coordinate_list):
    # 计算正方形左上角的坐标（未旋转时）
    square_top_left_x = x
    square_top_left_y = y - side_length / 2

    # 计算旋转后的正方形的四个顶点
    def rotate_point(px, py, cx, cy, angle):
        # 将角度转换为弧度
        rad = np.radians(angle)
        # 计算旋转后的坐标
        qx = cx + np.cos(rad) * (px - cx) - np.sin(rad) * (py - cy)
        qy = cy + np.sin(rad) * (px - cx) + np.cos(rad) * (py - cy)
        return qx, qy

    # 计算正方形的四个顶点
    points = [
        (square_top_left_x, square_top_left_y),
        (square_top_left_x, square_top_left_y + side_length),
        (square_top_left_x + side_length, square_top_left_y + side_length),
        (square_top_left_x + side_length, square_top_left_y)
    ]

    # 旋转每个顶点
    rotated_points = [rotate_point(px, py, x, y, angle) for px, py in points]

    # 创建旋转后的正方形路径
    polygon_path = Path(rotated_points)

    # 找到在旋转后的正方形内的点
    points_inside = [point for point in coordinate_list if polygon_path.contains_point(point)]

    # 返回在正方形内的点和旋转后的正方形顶点
    return points_inside, rotated_points

def draw_square_and_points(image_path, rotated_points, points_inside):
    # 打开图像
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # 绘制旋转后的正方形
    draw.polygon(rotated_points, outline="red")

    # 绘制在正方形内的点
    for point in points_inside:
        draw.ellipse((point[0] - 1, point[1] - 1, point[0] + 1, point[1] + 1), fill="green")

    # 显示图像
    img.show()

# 使用示例
x, y = 51, 57
side_length = 20
angle = 25
coordinate_list = [(1, 2), (3, 9), (50, 56), (52, 58), (60, 60)]

points_inside, rotated_points = find_points_in_rotated_square(x, y, side_length, angle, coordinate_list)
print("在旋转后的正方形内的点:", points_inside)
print("旋转后的正方形顶点:", rotated_points)

# 假设有一个图像路径
image_path = "your_image_path_here.jpg"

# 绘制旋转后的正方形和点
draw_square_and_points(image_path, rotated_points, points_inside)
