import cv2
import numpy as np

# 读取图像
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 使用高斯滤波来减少噪声
blurred = cv2.GaussianBlur(img, (9, 9), 2)

# 使用霍夫圆变换来检测圆
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist=20,
                            param1=50, param2=30, minRadius=0, maxRadius=0)

# 如果检测到圆
if circles is not None:
    circles = np.uint16(np.around(circles))
    max_radius = 0
    max_circle = None
    # 找到最大的圆
    for circle in circles[0, :]:
        if circle[2] > max_radius:
            max_radius = circle[2]
            max_circle = circle
    # 重新读取彩色图
    img_color = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
    # 绘制最大的圆
    if max_circle is not None:
        cv2.circle(img_color, (max_circle[0], max_circle[1]), max_circle[2], (0, 0, 255), 3)

    # 显示图像
    cv2.imshow('Detected Circles', img_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("没有检测到圆。")
