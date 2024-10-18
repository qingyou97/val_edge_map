import math

def calculate_angle(cx, cy, x, y):
    angle_radians = math.atan2(y - cy, x - cx)
    angle_degrees = math.degrees(angle_radians)
    if angle_degrees < 0:
        angle_degrees += 360
    return angle_degrees

def generate_integer_points_on_line(cx, cy, target_x, target_y, tolerance=0.1):
    points = set()
    dx = target_x - cx
    dy = target_y - cy
    gcd = math.gcd(dx, dy)
    step_x = dx // gcd
    step_y = dy // gcd

    x, y = cx, cy
    while (x, y) != (target_x, target_y):
        points.add((x, y))
        x += step_x
        y += step_y
    points.add((target_x, target_y))

    return list(points)

# 示例用法：
center = (0, 0)
target_point = (2, 1)
angle = calculate_angle(center[0], center[1], target_point[0], target_point[1])
print(f"角度: {angle} 度")

# 生成直线上的整数点
points_on_line = generate_integer_points_on_line(center[0], center[1], target_point[0], target_point[1])
print("直线上的整数点:")
for point in points_on_line:
    print(point)

# 检查是否包含目标点
if target_point in points_on_line:
    print(f"包含目标点: {target_point}")
else:
    print(f"不包含目标点: {target_point}")
