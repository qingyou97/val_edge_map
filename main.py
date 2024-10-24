import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def find_first_peak(data, threshold):
    """
    找到数据中第一个显著的峰值点，并返回其横坐标。

    参数:
    data (dict): 包含横坐标和对应强度值的字典。
    threshold (float): 峰值强度的最小阈值。

    返回:
    int: 第一个显著峰值点的横坐标。
    """
    # 提取横坐标和纵坐标
    x = list(data.keys())
    y = list(data.values())

    # 使用find_peaks找到峰值，并设置高度阈值
    peaks, properties = find_peaks(y, height=threshold)

    # 如果找到峰值，返回第一个峰值点的横坐标
    if peaks.size > 0:
        return x[peaks[0]]
    else:
        return None

def plot_data_with_peaks(data, threshold):
    """
    绘制数据并标记显著的峰值点。

    参数:
    data (dict): 包含横坐标和对应强度值的字典。
    threshold (float): 峰值强度的最小阈值。
    """
    # 提取横坐标和纵坐标
    x = list(data.keys())
    y = list(data.values())

    # 使用find_peaks找到峰值，并设置高度阈值
    peaks, properties = find_peaks(y, height=threshold)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    plt.plot([x[p] for p in peaks], [y[p] for p in peaks], "x")  # 标记峰值点

    # 设置图表标题和坐标轴标签
    plt.title('Peaks Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Intensity')

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

# 设置阈值
threshold = 1000

# 找到第一个显著的峰值点
first_peak_x = find_first_peak(data, threshold)
print("The first significant peak is at x-value:", first_peak_x)

# 绘制数据并标记显著的峰值点
plot_data_with_peaks(data, threshold)
