if slope is not None:
        # 第一个点坐标
        x1, y1 = line_points[0]
        # 如果斜率是无穷大，意味着垂直线，我们直接构建与x平行的线
        if np.isinf(slope):
            extended_line = LineString([(x1, y) for y in range(40, 70)])  # 包含整个可能的y轴范围
        else:
            # 通过第一个点和斜率创建一个扩展的line_string
            def y(x):
                return y1 + slope * (x - x1)
            x_coords = np.linspace(50, 70, 500)  # x范围可以适当调整
            extended_line = LineString([(x, y(x)) for x in x_coords])
    else:
        # 如果有有效的两个点，正常扩展线
        extended_line = LineString(line_points)
