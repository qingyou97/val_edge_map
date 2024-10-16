import cv2
import numpy as np

def repair_broken_lines(image_path, output_path, kernel_size=(3, 3), iterations=1):
    """
    修复黑白图像中断续的白色线段，并保持线段的单像素宽度。

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
    closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel, iterations=iterations)

    # 细化操作，保持线段的单像素宽度
    def thinning(image):
        # 使用Zhang-Suen细化算法
        size = np.size(image)
        skel = np.zeros(image.shape, np.uint8)
        ret, image = cv2.threshold(image, 127, 255, 0)
        element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        done = False

        while not done:
            eroded = cv2.erode(image, element)
            temp = cv2.dilate(eroded, element)
            temp = cv2.subtract(image, temp)
            skel = cv2.bitwise_or(skel, temp)
            image = eroded.copy()

            zeros = size - cv2.countNonZero(image)
            if zeros == size:
                done = True

        return skel

    thinned_image = thinning(closed_image)

    # 保存结果
    cv2.imwrite(output_path, thinned_image)

# 示例调用
repair_broken_lines('path_to_your_image.png', 'processed_image.png', kernel_size=(5, 5), iterations=2)
