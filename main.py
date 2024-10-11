import cv2
import numpy as np

def detect_and_draw_largest_arc(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print("无法读取图像")
        return

    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 高斯模糊
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 边缘检测
    edges = cv2.Canny(blurred, 50, 150, apertureSize=3)

    # 霍夫圆变换
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                               param1=50, param2=30, minRadius=0, maxRadius=0)

    # 如果检测到圆
    if circles is not None:
        circles = np.uint16(np.around(circles))
        largest_circle = max(circles[0, :], key=lambda c: c[2])  # 选择最大的圆

        # 绘制最大的圆
        cv2.circle(image, (largest_circle[0], largest_circle[1]), largest_circle[2], (0, 255, 0), 2)
        # 绘制圆心
        cv2.circle(image, (largest_circle[0], largest_circle[1]), 2, (0, 0, 255), 3)

    # 显示结果
    cv2.imshow('Largest Arc', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 使用示例
detect_and_draw_largest_arc('path_to_your_image.jpg')
