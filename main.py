# 动态设置图表的 x 和 y 限制，并增加一些边距
    margin = 5  # 边距
    ax.set_xlim(min(x_coords) - margin, max(x_coords) + margin)
    ax.set_ylim(min(y_coords) - margin, max(y_coords) + margin)
