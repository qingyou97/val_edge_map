def get_non_zero_pixels(image_path):
    # 读取灰度图像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 检查是否成功读取图像
    if image is None:
        raise ValueError("不能读取图像，检查路径是否正确")
    
    # 查找非零像素点的坐标
    non_zero_coords = np.argwhere(image > 0)
    
    # 将坐标转换为列表形式
    non_zero_coords_list = [tuple(coord) for coord in non_zero_coords]
    
    return non_zero_coords_list

# 示例使用
image_path = 'path/to/your/image.jpg'
non_zero_pixels = get_non_zero_pixels(image_path)
print(f"有值的像素点坐标: {non_zero_pixels}")
