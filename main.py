import cv2
import numpy as np

# 读取图像
image = cv2.imread('path_to_your_image.png', cv2.IMREAD_GRAYSCALE)

# 检查图像是否成功加载
if image is None:
    print("Error: Could not load image.")
    exit()

# 将图像二值化
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 使用张苏恩算法进行骨架化处理
thinned_image = cv2.ximgproc.thinning(binary_image, thinningType=cv2.ximgproc.THINNING_ZHANGSUEN)

# 显示原始图像和骨架化后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Binary Image', binary_image)
cv2.imshow('Thinned Image', thinned_image)

# 等待按键按下后关闭所有窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
