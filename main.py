import math

def calculate_angle(cx, cy, x, y):
    angle_radians = math.atan2(y - cy, x - cx)
    angle_degrees = math.degrees(angle_radians)
    if angle_degrees < 0:
        angle_degrees += 360
    return angle_degrees

def generate_integer_points_on_ray(cx, cy, angle_degrees, num_points=100, tolerance=0.1):
    angle_radians = math.radians(angle_degrees)
    points = set()

    for i in range(1, num_points + 1):
        x = cx + i * math.cos(angle_radians)
        y = cy + i * math.sin(angle_radians)
        int_x, int_y = round(x), round(y)
        
        # 计算点到直线的距离
        distance = abs((int_y - cy) * math.cos(angle_radians) - (int_x - cx) * math.sin(angle_radians))
        
        if distance <= tolerance:
            points.add((int_x, int_y))

    return list(points)

# 示例用法：
center = (0, 0)
angle = 26.565  # 例如从(0,0)到(2,1)的角度
print(f"角度: {angle} 度")

# 生成射线上的整数点
points_on_ray = generate_integer_points_on_ray(center[0], center[1], angle, num_points=100, tolerance=0.1)
print("射线上的整数点:")
for point in points_on_ray:
    print(point)
