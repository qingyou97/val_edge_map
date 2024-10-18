import math

def find_point_on_line(x1, y1, angle_degrees, distance=1):
    # 将角度转换为弧度
    angle_radians = math.radians(angle_degrees)
    
    # 计算点的坐标
    x = x1 + distance * math.cos(angle_radians)
    y = y1 - distance * math.sin(angle_radians)  # 注意这里是减去，因为y轴向下为正方向
    
    return x, y

# 示例
x1, y1 = 0, 0
angle_degrees = 26.56505
point_x, point_y = find_point_on_line(x1, y1, angle_degrees)
print(f"经过圆心 ({x1}, {y1}) 并且与水平向右方向成 {angle_degrees} 度的线经过的点是: ({point_x}, {point_y})")
