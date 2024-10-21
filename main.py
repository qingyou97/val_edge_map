# 输出圆环的内外直径和圆心点坐标
    for i, ellipse in enumerate(ellipses[:4]):
        center, axes, _ = ellipse
        diameter = max(axes) * 2
        print(f"圆环 {i//2 + 1} 的 {'外' if i % 2 == 0 else '内'}直径: {diameter:.2f}, 圆心点坐标: ({center[0]:.2f}, {center[1]:.2f})")
