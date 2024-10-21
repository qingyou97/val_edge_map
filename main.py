import matplotlib.pyplot as plt
import numpy as np

# 创建一个新的图形
fig, ax = plt.subplots(figsize=(8, 8))

# 定义每个区域的角度（弧度）
angles = np.linspace(0, 2 * np.pi, 9)

# 颜色数组
colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow']

# 绘制每一个区域
for i in range(8):
    theta1, theta2 = angles[i], angles[i + 1]
    wedge = plt.Polygon([(0,0), 
                         (np.cos(theta1), np.sin(theta1)), 
                         (np.cos(theta2), np.sin(theta2)), 
                         (0,0)],
                        color=colors[i])
    ax.add_patch(wedge)

# 设置坐标轴样式
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

# 隐藏轴的标签
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# 网格隐藏
ax.grid(False)
ax.axis('off')

# 显示图形
plt.show()
