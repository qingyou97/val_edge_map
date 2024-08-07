import os.path

import cv2
import numpy as np


path = r'E:\Datasets\Industrial quality inspection\Menta Training\2-casting-product-image-data-for-quality-inspection\casting\gt'

img_list = os.listdir(path)
for img in img_list:
    img_path = os.path.join(path, img)
    # 读取图像
    image = cv2.imread(img_path)

    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 应用高斯模糊
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 使用 Canny 算法检测边缘
    edges = cv2.Canny(blurred, 120, 250)

    name = img.split('.')[0]


    # 转化成二值图
    # 读取图片
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # 将灰度图转换为二值图像
    _, binary_image = cv2.threshold(image, 10, 255, cv2.THRESH_BINARY)

    # 保存二值图像

    cv2.imwrite(os.path.join(r'E:\1\new', rf'{name}_canny_edge.png'), binary_image)


    print(binary_image.shape)
    print(set(list(binary_image.flatten())))
