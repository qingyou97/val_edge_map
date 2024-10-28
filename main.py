import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def plot_ranked_peaks(data, threshold, distance, thresh):
    """
    绘制数据，并标记所有显著的峰值点，同时标记指定名次的峰值点为最终选取点。

    参数:
    data (dict): 包含横坐标和对应强度值的字典。
    threshold (float): 峰值强度的最小阈值。
    distance (int): 峰值之间的最小距离。
    thresh (int): 要最终标记哪个名次的峰值点。
    """

    # 提取横坐标和纵坐标
    x = list(data.keys())
    y = list(data.values())

    # 找到显著的峰值点
    peaks, properties = find_peaks(y, height=threshold, distance=distance)

    # 将峰值点按强度排序
    ranked_peaks = sorted([(y[p], p, x[p]) for p in peaks], reverse=True)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', label='Data')

    # 绘制所有的峰值点并标记它们的名次
    for rank, (intensity, index, x_value) in enumerate(ranked_peaks, start=1):
        plt.plot(x_value, intensity, "gs", label='Peaks' if rank == 1 else "")
        plt.text(x_value, intensity, f'{rank}', color='green', verticalalignment='bottom', horizontalalignment='right', fontsize=8, bbox=dict(facecolor='white', alpha=0.5, edgecolor='green'))
        if rank == thresh:
            plt.plot(x_value, intensity, "ms", markersize=10, label='Selected' if rank == 1 else "")
            plt.text(x_value, intensity, "finally selected", color='purple', verticalalignment='top', horizontalalignment='left', fontsize=10, bbox=dict(facecolor='white', alpha=0.5, edgecolor='purple')) 

    # 设置图表标题和坐标轴标签
    plt.title('Ranked Peaks Plot')
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

# 设置阈值、最小距离、和要选取的峰值名次
threshold = 1000
distance = 2
thresh = 2

# 绘制数据并标记显著的峰值点及最终选取点
plot_ranked_peaks(data, threshold, distance, thresh)
