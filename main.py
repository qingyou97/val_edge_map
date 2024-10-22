import cv2
import numpy as np

# 读取图像
image = cv2.imread('path_to_your_image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 边缘检测
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# 霍夫变换参数
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=20, maxLineGap=10)

# 绘制检测到的线
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 显示结果
cv2.imshow('Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
