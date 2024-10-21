def find_corresponding_left_point(right_x_input, right_y_input):
    if right_y_input < inner_radius or right_y_input > outer_radius:
        raise ValueError("输入的y坐标超出范围")
    
    # 计算角度
    angle = right_x_input / outer_radius
    if angle < 0:
        angle += 2 * np.pi
    
    # 计算在圆环中的x和y坐标
    circle_x = right_y_input * np.cos(angle)
    circle_y = right_y_input * np.sin(angle)
    
    return circle_x, circle_y
