import cv2
import numpy as np
from matplotlib import pyplot as plt

def binary_threshold(image_path, threshold_value):
    # 读取图像
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        raise ValueError("图像读取失败，请检查路径是否正确。")
    
    # 检查阈值在合理范围内
    if threshold_value < 0 or threshold_value > 255:
        raise ValueError("阈值应在0到255范围内。")

    # 应用二值化
    ret, binary_img = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)
    
    # 展示原始图像和二值化图像
    plt.figure(figsize=(10, 7))
    
    plt.subplot(1, 2, 1)
    plt.title('原始图像')
    plt.imshow(img, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title('二值化图像')
    plt.imshow(binary_img, cmap='gray')
    
    plt.show()
