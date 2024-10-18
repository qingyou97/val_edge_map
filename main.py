import math

def calculate_angle(x1, y1, x2, y2):
    delta_x = x2 - x1
    delta_y = y2 - y1
    angle_radians = math.atan2(delta_y, delta_x)
    angle_degrees = math.degrees(angle_radians)
    
    if angle_degrees < 0:
        angle_degrees += 360
    
    final_angle = (360 - angle_degrees) % 360
    return final_angle

# 示例
x1, y1 = 0, 0
x2, y2 = 1, 1
angle = calculate_angle(x1, y1, x2, y2)
print(f"从圆心到点 ({x2}, {y2}) 的角度是: {angle} 度")
