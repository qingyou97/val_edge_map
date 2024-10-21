def get_surrounding_points(x, y):
    if isinstance(x, float):
        x_floor, x_ceil = int(x // 1), int(x // 1 + 1)
    else:
        x_floor, x_ceil = x, x

    if isinstance(y, float):
        y_floor, y_ceil = int(y // 1), int(y // 1 + 1)
    else:
        y_floor, y_ceil = y, y

    surrounding_points = {
        (x_floor, y_floor),
        (x_floor, y_ceil),
        (x_ceil, y_floor),
        (x_ceil, y_ceil)
    }

    return list(surrounding_points)

# 示例
x = 3.6
y = 2.4
points = get_surrounding_points(x, y)
print(points)  # 输出: [(3, 2), (3, 3), (4, 2), (4, 3)]
