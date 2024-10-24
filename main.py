def find_non_white_points(image, points):
    non_white_points = []
    for point in points:
        x, y = point
        if image[y, x] != 255:  # 检查点是否不是白色
            non_white_points.append(point)
    return non_white_points

# Example usage:
hoops = [[111, 110, 136], [111, 110, 98], [110, 111, 70], [110, 111, 65]]
image = draw_hoops(hoops)

points = [(50, 50), (111, 110), (120, 120), (200, 200)]
non_white_points = find_non_white_points(image, points)
print(non_white_points)
