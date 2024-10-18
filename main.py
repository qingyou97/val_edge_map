import math

def calculate_angle(cx, cy, x, y):
    angle_radians = math.atan2(y - cy, x - cx)
    angle_degrees = math.degrees(angle_radians)
    # Ensure the angle is in the range [0, 360)
    if angle_degrees < 0:
        angle_degrees += 360
    return angle_degrees

def coordinate_from_angle(cx, cy, angle_degrees, radius):
    angle_radians = math.radians(angle_degrees)
    x = cx + radius * math.cos(angle_radians)
    y = cy + radius * math.sin(angle_radians)
    return (x, y)

# 示例用法：
center = (0, 0)
point = (2, 1)
angle = calculate_angle(center[0], center[1], point[0], point[1])
print(f"角度: {angle} 度")

# 验证我们能否从该角度获取到原点，这里设置半径为点(2, 1)离圆心的距离
radius = math.hypot(point[0] - center[0], point[1] - center[1])
calculated_point = coordinate_from_angle(center[0], center[1], angle, radius)
print(f"坐标: {calculated_point}")
