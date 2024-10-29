import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

def find_peak_x_coordinates(data):
    # 将数据转换为numpy数组
    x = np.array(list(data.keys()))
    y = np.array(list(data.values()))

    # 查找峰值
    peaks, _ = find_peaks(y)

    # 提取对应的x坐标
    peak_x_coordinates = x[peaks]

    # 打印峰值点对应的x坐标
    print('峰值点对应的x坐标:', peak_x_coordinates)

    # 可视化展示
    plt.plot(x, y, label='数据')
    plt.plot(x[peaks], y[peaks], "x", label='峰值点')
    plt.xlabel('X 轴坐标')
    plt.ylabel('强度值')
    plt.title('峰值检测')
    plt.legend()
    plt.show()

    return peak_x_coordinates

# 使用示例
data = {
    54: 449.3646893061633, 55: 1297.3446535116513, 56: 1805.3129851344728, 
    57: 1154.4329930468359, 58: 326.8625193847768, 59: 88.41092178101773,
    60: 51.0890213776857, 61: 624.067918662831, 62: 1831.24690567159, 
    63: 1961.34564405988, 64: 817.753806314575, 65: 213.5667589003967,
    66: 582.423872761227, 67: 942.5185305268745, 68: 11038.215331320959,
    69: 1127.561087995556, 70: 801.99001515015, 71: 261.08981751619,
    72: 101.204167635102
}

peak_x_coordinates = find_peak_x_coordinates(data)
