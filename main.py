import cv2
import numpy as np

def count_pixel_values(image_path):
    # 读取灰度图
    gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 检查是否成功读取图像
    if gray_image is None:
        print("Failed to load image")
        return

    # 初始化一个大小为256的数组以存放各灰度值的数量
    pixel_counts = np.zeros(256, dtype=int)

    # 计算每个灰度值的数量
    for value in range(256):
        pixel_counts[value] = np.count_nonzero(gray_image == value)

    # 打印每种灰度值及其数量
    for value, count in enumerate(pixel_counts):
        print(f"Gray Level {value}: {count}")

    return pixel_counts

# 使用上述函数
image_path = '你的图像路径.png'
counts = count_pixel_values(image_path)
