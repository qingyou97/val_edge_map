import cv2
import numpy as np

# 读取灰度图像
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 应用直方图均衡化
equalized_image = cv2.equalizeHist(image)

# 显示原图和均衡化后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
