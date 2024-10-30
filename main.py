import matplotlib.pyplot as plt
import numpy as np

# 初始点（位于正方形左边缘中间）
initial_point = np.array([57, 51])

def draw_square(center, edge_length, angle, style, label):
    # 正方形的角点计算
    half_length = edge_length / 2
    square = np.array([
        [-half_length, -half_length],
        [half_length, -half_length],
        [half_length, half_length],
        [-half_length, half_length],
    ])

    # 旋转矩阵
    rad_angle = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(rad_angle), -np.sin(rad_angle)],
        [np.sin(rad_angle), np.cos(rad_angle)]
    ])
    
    # 旋转正方形
    rotated_square = square.dot(rotation_matrix) + center
    
    # 画旋转后的正方形
    plt.plot(*zip(*rotated_square, rotated_square[0]), style, label=label)

# 显示图形
plt.figure(figsize=(8, 8))

# 初始正方形的中心和尺寸
square_edge = 102  # 假设正方形边长
initial_center = initial_point + np.array([square_edge / 2, 0])

# 画初始正方形
draw_square(initial_center, square_edge, 0, 'r-', 'Initial Square')

# 旋转后的正方形
rotation_angle = 25

# 计算旋转后的正方形中心
# 由于旋转后点仍在左侧边中间，我们需要计算新的中心
half_edge = square_edge / 2
offset_x = half_edge * np.cos(np.radians(rotation_angle))
offset_y = half_edge * np.sin(np.radians(rotation_angle))
rotated_center = initial_point + np.array([offset_x, -offset_y])

# 计算旋转后的正方形中心
# 旋转后，左侧边中点仍然是 initial_point
# 计算中心点
center_offset = np.array([
    half_edge * np.cos(np.radians(rotation_angle + 90)),
    half_edge * np.sin(np.radians(rotation_angle + 90))
])
rotated_center = initial_point + center_offset

# 画旋转后的正方形
draw_square(rotated_center, square_edge, rotation_angle, 'b--', 'Rotated Square')

# 标记变换前后的中点
plt.scatter(*initial_point, color='red', zorder=5)
plt.text(initial_point[0], initial_point[1], 'Fixed Point', fontsize=9, verticalalignment='bottom')

# 图形设置
plt.xlim(0, 160)
plt.ylim(0, 160)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title('Rotating a Square with Fixed Left Midpoint')
plt.grid(True)
plt.show()
