import matplotlib.pyplot as plt

def plot_peaks_with_specific_values(data, specific_x, value_list):
    """
    绘制数据，并根据特定条件标记点，并在右上角添加指示。

    参数:
    data (dict): 包含横坐标和对应强度值的字典。
    specific_x (int): 要用黄色标记的特定横坐标。
    value_list (list): 要用红色标记的横坐标列表。
    """

    # 提取横坐标和纵坐标
    x = list(data.keys())
    y = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', label='Data')

    # 标记特定横坐标对应的点
    yellow_label_added = False
    red_label_added = False
    green_label_added = False

    for i in range(len(x)):
        if x[i] == specific_x:
            if not yellow_label_added:
                plt.plot(x[i], y[i], "ys", markersize=10, markerfacecolor='none', markeredgewidth=2, label='finally selected')
                yellow_label_added = True
            else:
                plt.plot(x[i], y[i], "ys", markersize=10, markerfacecolor='none', markeredgewidth=2)
        elif x[i] in value_list:
            if not red_label_added:
                plt.plot(x[i], y[i], "rs", markersize=10, markerfacecolor='none', markeredgewidth=2, label='not in ai result')
                red_label_added = True
            else:
                plt.plot(x[i], y[i], "rs", markersize=10, markerfacecolor='none', markeredgewidth=2)
        else:
            if not green_label_added:
                plt.plot(x[i], y[i], "gs", markersize=10, markerfacecolor='none', markeredgewidth=2, label='in ai result')
                green_label_added = True
            else:
                plt.plot(x[i], y[i], "gs", markersize=10, markerfacecolor='none', markeredgewidth=2)

    # 设置图表标题和坐标轴标签
    plt.title('Peaks Plot with Specific Values')
    plt.xlabel('X-axis')
    plt.ylabel('Intensity')

    # 显示图例
    plt.legend(loc='upper right')

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

# 设置要标记的特定横坐标
specific_x = 56

# 设置要用红色标记的横坐标列表
value_list = [55, 57, 60]

# 绘制数据并标记显著的峰值点及特定横坐标对应的点
plot_peaks_with_specific_values(data, specific_x, value_list)
