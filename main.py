import cv2
import numpy as np

# 读入图像
image = cv2.imread('your_image.jpg', 0)

# 二值化图像
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 创建形态操作核
kernel = np.ones((3,3), np.uint8)

# 腐蚀操作，减少边缘厚度
eroded = cv2.erode(binary, kernel, iterations=1)

# 骨架化操作
def skeletonize(image):
    skel = np.zeros(image.shape, np.uint8)
    temp = np.zeros(image.shape, np.uint8)
    eroded = np.zeros(image.shape, np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

    while True:
        eroded = cv2.erode(image, kernel)
        temp = cv2.dilate(eroded, kernel)
        temp = cv2.subtract(image, temp)
        skel = cv2.bitwise_or(skel, temp)
        image = eroded.copy()
        if cv2.countNonZero(image) == 0:
            break

    return skel

# 骨架化处理
skeleton = skeletonize(eroded)

# 显示结果
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded)
cv2.imshow('Skeletonized Image', skeleton)
cv2.waitKey(0)
cv2.destroyAllWindows()
