import cv2
import numpy as np

# 读入图片
image1 = cv2.imread('image1.png')
image2 = cv2.imread('image2.png')

# 确保两张图片尺寸相同
if image1.shape == image2.shape:
    # 做减法
    difference = cv2.absdiff(image1, image2)
    
    # 将差异部分高亮显示
    gray_difference = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray_difference, 30, 255, cv2.THRESH_BINARY)

    # 使用红色高亮不通部分
    highlighted = image1.copy()
    highlighted[mask != 0] = [0, 0, 255]

    # 显示结果
    cv2.imshow('Difference', mask)
    cv2.imshow('Highlighted Differences', highlighted)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("两个图片的尺寸不相同")
