import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# 给定点的坐标
x, y = 51, 57
side_length = 20
angle = 25  # 逆时针旋转角度

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

# 创建绘图
fig, ax = plt.subplots()

# 创建未旋转的正方形
original_square = patches.Polygon(points, closed=True, edgecolor='gray', facecolor='none', linestyle='--')
ax.add_patch(original_square)

# 创建旋转后的正方形
rotated_square = patches.Polygon(rotated_points, closed=True, edgecolor='blue', facecolor='none')
ax.add_patch(rotated_square)

# 绘制点
plt.plot(x, y, 'ro')  # 'ro' 表示红色的圆点

# 设置绘图范围
plt.xlim(x - side_length, x + side_length)
plt.ylim(y - side_length, y + side_length)

# 保持比例
ax.set_aspect('equal', 'box')

# 显示绘图
plt.xlabel("X坐标")
plt.ylabel("Y坐标")
plt.title("旋转前后的正方形与给定点")
plt.show()
