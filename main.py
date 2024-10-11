import cv2
import numpy as np

def detect_and_draw_arcs(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    if image is None:
        print("无法读取图像")
        return

    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 二值化
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # 边缘检测
    edges = cv2.Canny(binary, 100, 200)

    # 检测轮廓
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 拟合椭圆并绘制
    for contour in contours:
        if len(contour) >= 5:  # 拟合椭圆至少需要5个点
            ellipse = cv2.fitEllipse(contour)
            cv2.ellipse(image, ellipse, (0, 255, 0), 2)

    # 显示结果
    cv2.imshow('Detected Arcs', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 使用示例
detect_and_draw_arcs('path_to_your_image.jpg')
