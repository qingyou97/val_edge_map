import cv2
import numpy as np

# 读取图像
image = cv2.imread('path_to_image')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 二值化图像
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 查找轮廓
contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 计算每个轮廓的厚度
for contour in contours:
    # 获取轮廓的旋转边界矩形
    rect = cv2.minAreaRect(contour)
    width = min(rect[1])  # 找到最小的边（假设是线条宽度）
    print(f"Line thickness: {width}")

# 显示结果（可选）
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
