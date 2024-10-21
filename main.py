import matplotlib.pyplot as plt
import numpy as np

# 图像尺寸
img_size = 224

# 创建一个新的图形
fig, ax = plt.subplots(figsize=(8, 8))

# 定义每个区域的角度（弧度）
angles = np.linspace(0, 2 * np.pi, 9)

# 颜色数组
colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow']

# 中心点
center = (img_size / 2, img_size / 2)

# 绘制每一个区域
for i in range(8):
    theta1, theta2 = angles[i], angles[i + 1]
    x1, y1 = center[0] + (img_size / 2) * np.cos(theta1), center[1] + (img_size / 2) * np.sin(theta1)
    x2, y2 = center[0] + (img_size / 2) * np.cos(theta2), center[1] + (img_size / 2) * np.sin(theta2)
    wedge = plt.Polygon([center, (x1, y1), (x2, y2), center], color=colors[i])
    ax.add_patch(wedge)

# 设置坐标轴样式
ax.set_xlim(0, img_size)
ax.set_ylim(0, img_size)
ax.set_aspect('equal')

# 隐藏轴的标签
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# 网格隐藏
ax.grid(False)
ax.axis('off')

# 显示图形
plt.show()
