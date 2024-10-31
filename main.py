# 计算x和y的边界，并增加边距
    all_x = x + tuple(pt[0] for pt in square_points)
    all_y = y + tuple(pt[1] for pt in square_points)
    
    min_x, max_x = min(all_x), max(all_x)
    min_y, max_y = min(all_y), max(all_y)

    # 增加10个像素点的边距
    border_x = 10 / fig.dpi
    border_y = 10 / fig.dpi

    ax.set_xlim(min_x - border_x, max_x + border_x)
    ax.set_ylim(min_y - border_y, max_y + border_y)
