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
initial_center = initial_point + np.array([0, 0]) 
square_edge = 102  # 从点位置推算整条边长

# 旋转后的边缘中点和中心
rotation_angle = 14
transformed_center = initial_point + np.array([0, square_edge / 2])

# 画正方形
draw_square(initial_center, square_edge, 0, 'r-', 'Initial Square')
draw_square(transformed_center, square_edge, rotation_angle, 'b--', 'Rotated Square')

# 标记变换前后的中点
plt.scatter(*initial_point, color='red')
plt.scatter(*initial_point, color='blue')

# 图形设置
plt.xlim(10, 160)
plt.ylim(0, 180)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title('Rotating a Square')
plt.grid(True)
plt.show()
