# 输出圆环的内外直径和圆心点坐标
    for i, ellipse in enumerate(ellipses[:4]):
        center, axes, _ = ellipse
        diameter = int(max(axes) * 2)
        center_x, center_y = int(center[0]), int(center[1])
        print(f"圆环 {i//2 + 1} 的 {'外' if i % 2 == 0 else '内'}直径: {diameter}, 圆心点坐标: ({center_x}, {center_y})")
