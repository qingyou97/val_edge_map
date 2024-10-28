import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def plot_peaks_with_specific_value(data, specific_value):
    """
    绘制数据，并标记所有显著的峰值点，同时标记特定值对应的点。

    参数:
    data (dict): 包含横坐标和对应强度值的字典。
    specific_value (float): 要标记的特定值。
    """

    # 提取横坐标和纵坐标
    x = list(data.keys())
    y = list(data.values())

    # 找到显著的峰值点
    peaks, _ = find_peaks(y)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', label='Data')

    # 绘制所有的峰值点
    for p in peaks:
        plt.plot(x[p], y[p], "gs", label='Peaks' if p == peaks[0] else "")

    # 标记特定值对应的点
    if specific_value in y:
        index = y.index(specific_value)
        plt.plot(x[index], y[index], "ys", markersize=10, label='Specific Value')

    # 设置图表标题和坐标轴标签
    plt.title('Peaks Plot with Specific Value')
    plt.xlabel('X-axis')
    plt.ylabel('Intensity')

    # 显示图例
    plt.legend()

    # 显示网格
    plt.grid(True)

    # 显示图表
    plt.show()

# 示例数据
data = {
    54: 449.3646893061633, 55: 1297.3446535116513, 56: 1805.3129851344728, 57: 1154.4329930468359,
    58: 326.8625193847768, 59: 88.41092178101773, 60: 51.0890213776857, 61: 624.067918662831,
    62: 1831.24690567159, 63: 1961.3456440598800, 64: 817.753806314575, 65: 213.5667589003967,
    66: 582.423872761227, 67: 942.5185305268745, 68: 1038.215331320959, 69: 1127.561087995556,
    70: 801.99001515015, 71: 261.089817516190, 72: 101.204167635102
}

# 设置要标记的特定值
specific_value = 1805.3129851344728

# 绘制数据并标记显著的峰值点及特定值对应的点
plot_peaks_with_specific_value(data, specific_value)
