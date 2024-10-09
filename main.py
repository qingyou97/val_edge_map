def find_color_points(image_path, target_color):
    # 读取图像
    image = cv2.imread(image_path)
    
    # 确保图像读取成功
    if image is None:
        return []

    # 建立一个空的list来存储坐标
    points = []

    # 获取图像高和宽
    height, width, _ = image.shape

    # 遍历每一个像素点
    for y in range(height):
        for x in range(width):
            if np.array_equal(image[y, x], target_color):
                points.append((x, y))
    
    return points

# 图像路径
image_path = 'path/to/your/image.jpg'
# 目标RGB颜色
target_color = [R, G, B]  # 例如 [255, 0, 0] 表示红色

# 寻找指定颜色的坐标
coordinates = find_color_points(image_path, target_color)
print(coordinates)
