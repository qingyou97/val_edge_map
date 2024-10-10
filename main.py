import cv2
import numpy as np

# 读取图像
image = cv2.imread('path_to_image.jpg', cv2.IMREAD_GRAYSCALE)

# 边缘检测 (可调参数)
edges = cv2.Canny(image, threshold1=50, threshold2=150, apertureSize=3)

# 霍夫圆变换 (可调参数)
circles = cv2.HoughCircles(edges, 
                           cv2.HOUGH_GRADIENT, 
                           dp=1.2, 
                           minDist=30, 
                           param1=50, 
                           param2=30, 
                           minRadius=10, 
                           maxRadius=100)

# 如果检测到圆
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0, :]:
        # 画出圆
        center = (circle[0], circle[1])
        radius = circle[2]
        cv2.circle(image, center, radius, (0, 0, 0), 2)
        cv2.circle(image, center, 2, (0, 0, 0), 3)

# 显示结果
cv2.imshow("Detected Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
