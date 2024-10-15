def extract_points_magnitude_and_angle(magnitude, direction, points, shape):
    new_magnitude = np.zeros(shape)
    new_angle = np.zeros(shape)

    for point in points:
        new_magnitude[point[1], point[0]] = magnitude[point[1], point[0]]
        new_angle[point[1], point[0]] = direction[point[1], point[0]]
    
    return new_magnitude, new_angle

# 使用例子
img_path = 'your_image.jpg'
points = [(x1, y1), (x2, y2), ..., (xn, yn)]  # 替换为实际坐标点列表

magnitude, angle, color_image, image = caculate_magnitude_and_direction(img_path)
new_magnitude, new_angle = extract_points_magnitude_and_angle(magnitude, angle, points, magnitude.shape)

# 保存结果图像或进行其他处理
cv2.imwrite('new_magnitude_image.jpg', new_magnitude)
cv2.imwrite('new_angle_image.jpg', new_angle)
