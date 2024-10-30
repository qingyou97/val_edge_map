import matplotlib.pyplot as plt
import numpy as np

# 正方形的边长
side_length = 100

# 初始正方形的左侧边缘中心点
original_point = (0, side_length / 2)

# 旋转角度
angle = 14  # 90 - 76
angle_rad = np.radians(angle)

# 旋转矩阵
rotation_matrix = np.array([
    [np.cos(angle_rad), -np.sin(angle_rad)],
    [np.sin(angle_rad), np.cos(angle_rad)]
])

# 计算旋转后的点
rotated_point = np.dot(rotation_matrix, original_point)

# 画图函数
def draw_square(ax, center, side, angle, label):
    half_side = side / 2
    # 计算正方形的四个顶点
    corners = np.array([
        [-half_side, -half_side],
        [half_side, -half_side],
        [half_side, half_side],
        [-half_side, half_side]
    ])
    
    # 旋转正方形
    rotated_corners = np.dot(corners, rotation_matrix.T)
    
    # 平移到中心
    rotated_corners += center
    
    # 绘制正方形
    square = plt.Polygon(rotated_corners, fill=None, edgecolor='r')
    ax.add_patch(square)
    
    # 绘制点
    ax.plot(center[0], center[1], 'bo')
    ax.text(center[0], center[1], f' {label}', verticalalignment='bottom', horizontalalignment='right')

# 创建图和轴
fig, ax = plt.subplots()

# 绘制初始正方形和旋转后的正方形
draw_square(ax, original_point, side_length, 0, 'Original')
draw_square(ax, rotated_point, side_length, angle, 'Rotated')

# 设置图形范围
buffer = 20
ax.set_xlim(-side_length, side_length + buffer)
ax.set_ylim(-side_length, side_length + buffer)

# 设置轴比例相等
ax.set_aspect('equal', 'box')

# 显示结果
plt.grid(True)
plt.title('Square Rotation Example')
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.show()
