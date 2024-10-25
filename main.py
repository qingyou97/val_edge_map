import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def find_significant_peaks(data, threshold, distance):
    """
    找到数据中所有显著的峰值点，并返回其横坐标，按照横轴从小到大排列。

    参数:
    data (dict): 包含横坐标和对应强度值的字典。
    threshold (float): 峰值强度的最小阈值。
    distance (int): 峰值之间的最小距离。

    返回:
    list: 所有显著峰值点的横坐标，按照横轴从小到大排列。
    """
    # 提取横坐标和纵坐标
    x = list(data.keys())
    y = list(data.values())

    # 使用find_peaks找到峰值，并设置高度阈值和最小距离
    peaks, properties = find_peaks(y, height=threshold, distance=distance)

    # 返回所有显著峰值点的横坐标，按照横轴从小到大排列
    return sorted([x[p] for p in peaks])

def plot_data_with_peaks(data, threshold, distance):
    """
    绘制数据并标记显著的峰值点。

    参数:
    data (dict): 包含横坐标和对应强度值的字典。
    threshold (float): 峰值强度的最小阈值。
    distance (int): 峰值之间的最小距离。
    """
    # 提取横坐标和纵坐标
    x = list(data.keys())
    y = list(data.values())

    # 找到显著的峰值点
    peaks = find_significant_peaks(data, threshold, distance)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', label='Data')
    plt.plot(peaks, [data[p] for p in peaks], "x", label='Peaks')  # 标记峰值点

    # 设置图表标题和坐标轴标签
    plt.title('Peaks Plot')
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
    54: 449.3646893061633, 55: 1297.34465165651155, 56: 1805.3129851341728, 57: 1154.4329935468359,
    58: 326.8625193847768, 59: 88.410921781012733, 60: 51.08902684585762, 61: 624.0675913836851,
    62: 1831.2469056712966, 63: 1961.3456440528098, 64: 817.7538061704564, 65: 213.56610930077673,
    66: 582.4233078671347, 67: 942.5185305268745, 68: 1038.215331300595, 69: 1127.5610874995525,
    70: 801.99001550009673, 71: 261.0890344860568, 72: 101.20416736553082
}

# 设置阈值和最小距离
threshold = 1000
distance = 2

# 找到所有显著峰值点的横坐标
significant_peaks = find_significant_peaks(data, threshold, distance)
print(f"Significant peaks are at x = {significant_peaks}")

# 绘制数据并标记显著的峰值点
plot_data_with_peaks(data, threshold, distance)
