 # 采样并检查所有在正方形内的点
    all_points_inside = []
    x_points = np.arange(x_min, x_max, step)
    y_points = np.arange(y_min, y_max, step)

    for x in x_points:
        for y in y_points:
            if polygon_path.contains_point((x, y)):
                all_points_inside.append((x, y))
