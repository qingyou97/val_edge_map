import matplotlib.pyplot as plt

# 假设这个是你的list数据
data = [
    [(220, 116), 284.0633732109791],
    # 其他数据点
]

# 提取数据
coordinates = []
intensities = []

for item in data:
    coordinates.append(item[0])
    intensities.append(item[1])

# 分离坐标x和y
x, y = zip(*coordinates)

# 创建绘图
fig, ax = plt.subplots()

# 散点图
scatter = ax.scatter(x, y, c=intensities, cmap='viridis')

# 添加色条
cbar = plt.colorbar(scatter, ax=ax, label='Intensity')

# 设置标签和标题
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
plt.title('Intensity Map')

# 设置坐标轴范围
ax.set_xlim(0, 223)
ax.set_ylim(0, 223)

# 显示图像
plt.savefig("output.png")  # 输出到文件
plt.show()  # 显示图像
