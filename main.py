import cv2
import numpy as np

# 读取图像
image = cv2.imread('path_to_image')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 二值化图像
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 查找轮廓
contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 计算每个轮廓的厚度并绘制
for contour in contours:
    # 获取轮廓的旋转边界矩形
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    
    # 画出旋转矩形
    cv2.drawContours(image, [box], 0, (0, 255, 0), 2)
    
    # 找到最小的边（假设是线条宽度）
    width = min(rect[1])
    print(f"Line thickness: {width}")
    
    # 画出厚度线
    if rect[1][0] < rect[1][1]:
        pt1 = tuple(box[0])
        pt2 = tuple(box[1])
    else:
        pt1 = tuple(box[1])
        pt2 = tuple(box[2])
    
    cv2.line(image, pt1, pt2, (255, 0, 0), 2)

# 显示结果
cv2.imshow('Image with Thickness', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
