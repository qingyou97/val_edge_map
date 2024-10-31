def plot_and_find_max(data):
    # 提取横坐标和纵坐标
    x = list(data.keys())
    y = list(data.values())

    # 绘制图
    plt.plot(x, y, marker='o')

    # 找到最大值点
    max_index = max(data, key=data.get)
    max_value = data[max_index]

    # 标注最大值点
    plt.annotate(f'Max: ({max_index}, {max_value})', 
                 xy=(max_index, max_value), 
                 xytext=(max_index, max_value + 5),
                 arrowprops=dict(facecolor='black', shrink=0.05), 
                 fontsize=10)

    # 添加标签和标题
    plt.xlabel('横坐标')
    plt.ylabel('强度值')
    plt.title('峰值图')

    # 显示图表
    plt.show()

    # 返回最大值的key和value
    return max_index, max_value
