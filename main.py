import matplotlib.pyplot as plt
from scipy.signal import find_peaks

data = {
    54: 449.3646893061633, 55: 1297.34465165651155, 56: 1805.3129851341728, 57: 1154.4329935468359,
    58: 326.8625193847768, 59: 88.410921781012733, 60: 51.08902684585762, 61: 624.0675913836851,
    62: 1831.2469056712966, 63: 1961.3456440528098, 64: 817.7538061704564, 65: 213.56610930077673,
    66: 582.4233078671347, 67: 942.5185305268745, 68: 1038.215331300595, 69: 1127.5610874995525,
    70: 801.99001550009673, 71: 261.0890344860568, 72: 101.20416736553082
}

# 提取横坐标和纵坐标
x = list(data.keys())
y = list(data.values())

# 设置一个阈值来筛选显著的峰值
threshold = 1000

# 使用find_peaks找到峰值，并设置高度阈值
peaks, properties = find_peaks(y, height=threshold)

plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o')
plt.plot([x[p] for p in peaks], [y[p] for p in peaks], "x")  # 标记峰值点

# 标注峰值点
for p in peaks:
    plt.text(x[p], y[p], f'({x[p]}, {y[p]:.2f})', fontsize=9, ha='right')

# 设置图表标题和坐标轴标签
plt.title('Peaks Plot')
plt.xlabel('X-axis')
plt.ylabel('Intensity')

# 显示网格
plt.grid(True)

# 显示图表
plt.show()

# 打印峰值点
print("Peaks at x-values:", [x[p] for p in peaks])
print("Peak intensities:", [y[p] for p in peaks])
