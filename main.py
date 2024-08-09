import cv2
import numpy as np

# 读取灰度图像
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 创建一个布尔掩码，找到所有像素值大于10的点
mask = image > 10

# 将这些点的像素值设为255
image[mask] = 255

# 保存修改后的图像
cv2.imwrite('modified_image.jpg', image)
