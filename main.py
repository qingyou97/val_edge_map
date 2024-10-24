def mark_white_points(A_path, B_path, output_path):
    """
    在B图中用红色标记A图中的白色点。

    参数:
    A_path (str): A图的文件路径。
    B_path (str): B图的文件路径。
    output_path (str): 输出图像的文件路径。
    """
    # 读取A图和B图
    A_img = cv2.imread(A_path, cv2.IMREAD_GRAYSCALE)
    B_img = cv2.imread(B_path)

    # 确保B图为彩色图
    if len(B_img.shape) == 2 or B_img.shape[2] == 1:
        B_img = cv2.cvtColor(B_img, cv2.COLOR_GRAY2BGR)

    # 找到A图中白色点的坐标
    white_points = np.argwhere(A_img == 255)  # 255表示白色点

    # 在B图上画出红点
    for point in white_points:
        cv2.circle(B_img, (point[1], point[0]), radius=1, color=(0, 0, 255), thickness=-1)

    # 保存输出图像
    cv2.imwrite(output_path, B_img)

# 示例调用
mark_white_points('A.png', 'B.png', 'B_with_red_dots.png')
