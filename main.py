import math

def generate_points_on_ray(cx, cy, angle_degrees, num_points=10, step_size=1):
    angle_radians = math.radians(angle_degrees)
    points = []
    for i in range(1, num_points + 1):
        x = cx + i * step_size * math.cos(angle_radians)
        y = cy + i * step_size * math.sin(angle_radians)
        points.append((x, y))
    return points

# 示例用法：
center = (0, 0)
angle = calculate_angle(center[0], center[1], 2, 1)
print(f"角度: {angle} 度")

# 生成射线上的点
points_on_ray = generate_points_on_ray(center[0], center[1], angle, num_points=10, step_size=0.5)
print("射线上的点:")
for point in points_on_ray:
    print(point)
