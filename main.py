import matplotlib.pyplot as plt
import numpy as np

# 初始化正方形边长和点的位置
side_length = 100
original_center = (57, 51)

# 创建一个90 - 76度逆时针旋转矩阵
angle_rot = np.radians(90 - 76)
cos_theta, sin_theta = np.cos(angle_rot), np.sin(angle_rot)
rotation_matrix = np.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]])

# 算出旋转后的正方形中心点
new_center_x = original_center[0] * rotation_matrix[0, 0] + original_center[1] * rotation_matrix[0, 1]
new_center_y = original_center[0] * rotation_matrix[1, 0] + original_center[1] * rotation_matrix[1, 1]
new_center = (new_center_x, new_center_y)

# 画图函数
def draw_square_with_point(ax, center, side, label):
    half_side = side / 2
    square = plt.Rectangle((center[0] - half_side, center[1] - half_side), side, side, fill=None, edgecolor='r')
    ax.add_patch(square)
    ax.plot(center[0], center[1], 'bo')  # 点的位置
    ax.text(center[0], center[1], f' {label}', verticalalignment='bottom', horizontalalignment='right')

# 创建图和轴
fig, ax = plt.subplots()

# 绘制初始和旋转后的正方形及点
draw_square_with_point(ax, original_center, side_length, 'P1')
draw_square_with_point(ax, new_center, side_length, 'P2 (rotated)')

# 设置图形范围
buffer = 20
ax.set_xlim(0 - buffer, side_length + buffer)
ax.set_ylim(0 - buffer, side_length + buffer)

# 设置轴比例相等
ax.set_aspect('equal', 'box')

# 显示结果
plt.grid(True)
plt.title('Square Rotation Example')
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.show()
