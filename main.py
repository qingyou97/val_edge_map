import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 给定点的坐标
x, y = 51, 57
side_length = 20

# 计算正方形左上角的坐标
square_top_left_x = x
square_top_left_y = y - side_length / 2

# 创建绘图
fig, ax = plt.subplots()

# 创建正方形
square = patches.Rectangle((square_top_left_x, square_top_left_y), side_length, side_length, edgecolor='blue', facecolor='none')

# 将正方形添加到绘图中
ax.add_patch(square)

# 绘制点
plt.plot(x, y, 'ro')  # 'ro' 表示红色的圆点

# 设置绘图范围
plt.xlim(x - 5, x + side_length + 5)
plt.ylim(y - side_length / 2 - 5, y + side_length / 2 + 5)

# 保持比例
ax.set_aspect('equal', 'box')

# 显示绘图
plt.xlabel("X坐标")
plt.ylabel("Y坐标")
plt.title("正方形与给定点")
plt.show()
