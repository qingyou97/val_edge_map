def generate_integer_points_on_ray(cx, cy, angle_degrees, target_point, num_points=100):
    angle_radians = math.radians(angle_degrees)
    points = set()
    target_x, target_y = target_point
    found_target = False

    for i in range(1, num_points + 1):
        x = cx + i * math.cos(angle_radians)
        y = cy + i * math.sin(angle_radians)
        int_x, int_y = round(x), round(y)
        points.add((int_x, int_y))
        if (int_x, int_y) == (target_x, target_y):
            found_target = True

    if not found_target:
        points.add((target_x, target_y))

    return list(points)

# 示例用法：
center = (0, 0)
target_point = (2, 1)
angle = calculate_angle(center[0], center[1], target_point[0], target_point[1])
print(f"角度: {angle} 度")

# 生成射线上的整数点
points_on_ray = generate_integer_points_on_ray(center[0], center[1], angle, target_point, num_points=100)
print("射线上的整数点:")
for point in points_on_ray:
    print(point)

# 检查是否包含目标点
if target_point in points_on_ray:
    print(f"包含目标点: {target_point}")
else:
    print(f"不包含目标点: {target_point}")
