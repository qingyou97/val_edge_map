def annotate_image_with_red_dots(image_path, coords, output_path):
    """
    在图像上标记红色点并保存新图像。

    参数:
    - image_path: 输入图像的路径
    - coords: 坐标列表，格式为 [(x1, y1), (x2, y2), ...]
    - output_path: 输出图像的路径
    """
    # 读取黑白图像
    img_anno = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 将黑白图像转换为BGR彩色图像
    img_anno = cv2.cvtColor(img_anno, cv2.COLOR_GRAY2BGR)

    # 遍历所有坐标并标记红色点
    for item in coords:
        x = item[0]
        y = item[1]
        print(f'x: {x}, y: {y}')
        img_anno[y, x] = (0, 0, 255)  # BGR通道，红色

    # 保存新的图像
    cv2.imwrite(output_path, img_anno)

# 示例调用
image_path = './12_filtered.png'
coords = [(10, 10), (20, 20), (30, 30)]
output_path = 'annotated_images.png'
annotate_image_with_red_dots(image_path, coords, output_path)
