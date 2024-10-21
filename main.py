import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
font_path = "C:/Windows/Fonts/simsun.ttc"  # 你可以根据实际情况修改路径
font_prop = FontProperties(fname=font_path)

inner_radius = 2  # 内半径
outer_radius = 5  # 外半径
theta = np.linspace(0, 2 * np.pi, 1000)  # 角度分段

# 创建圆环
inner_circle_x = inner_radius * np.cos(theta)
inner_circle_y = inner_radius * np.sin(theta)
outer_circle_x = outer_radius * np.cos(theta)
outer_circle_y = outer_radius * np.sin(theta)

# 创建矩形边界
rect_height = outer_radius - inner_radius
rect_width = 2 * np.pi * outer_radius

# 展开圆环，并显示对应点
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# 绘制圆环
ax1.plot(inner_circle_x, inner_circle_y, label='内圆')
ax1.plot(outer_circle_x, outer_circle_y, label='外圆')
ax1.set_aspect('equal', 'box')
ax1.set_title('圆环', fontproperties=font_prop)
ax1.legend()

# 在矩形的左侧边界上画出原圆环左侧
left_side_y = np.linspace(inner_radius, outer_radius, 1000)
left_side = np.zeros_like(left_side_y)

# 在矩形的右侧边界上画出原圆环右侧
right_side_y = np.linspace(inner_radius, outer_radius, 1000)
right_side = np.ones_like(right_side_y) * rect_width

# 给左右的每个点添加颜色来表示一一对应关系（使用渐变色）
cmap = plt.get_cmap('viridis')
colors = cmap(np.linspace(0, 1, len(left_side_y)))

# 绘制两侧点以及它们的一一对应的连接线
for i in range(len(left_side_y)):
    ax2.plot([left_side[i], right_side[i]], [left_side_y[i], right_side_y[i]],
             color=colors[i], linestyle='-', linewidth=0.5)

# 设置矩形的显示
ax2.set_xlim(0, rect_width)
ax2.set_ylim(inner_radius, outer_radius)
ax2.set_xlabel('展开后的圆环外周长', fontproperties=font_prop)
ax2.set_ylabel('半径差值', fontproperties=font_prop)
ax2.set_title('圆环展开后的矩形表示及配对关系', fontproperties=font_prop)

plt.tight_layout()
plt.show()
