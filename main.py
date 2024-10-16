def repair_broken_lines(image_path, output_path, kernel_size=(3, 3), iterations=1):
    """
    修复黑白图像中断续的白色线段。

    参数:
    image_path (str): 输入图像的路径。
    output_path (str): 输出修复后图像的路径。
    kernel_size (tuple): 形态学操作的核大小，默认为(3, 3)。
    iterations (int): 形态学操作的迭代次数，默认为1。

    返回:
    None
    """
    # 读取图像（假设是单通道的黑白图像）
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 二值化（如果不是二值图像的话）
    _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

    # 定义一个修补核
    kernel = np.ones(kernel_size, np.uint8)

    # 膨胀然后腐蚀（即闭运算，填补间隙）
    processed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel, iterations=iterations)

    # 保存结果
    cv2.imwrite(output_path, processed_image)

# 示例调用
repair_broken_lines('path_to_your_image.png', 'processed_image.png', kernel_size=(5, 5), iterations=2)
