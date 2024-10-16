import cv2
import numpy as np

# 读取图像
image = cv2.imread('path_to_your_image.png', cv2.IMREAD_GRAYSCALE)

# 二值化图像
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# 进行形态学操作（闭操作）
kernel = np.ones((3, 3), np.uint8)  # 窗口大小为3x3，进行闭运算来填充小孔
closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# 反转图像颜色（因为你希望黑色是背景）
closed_image = cv2.bitwise_not(closed_image)

# 使用霍夫变换检测线条
lines = cv2.HoughLinesP(closed_image, rho=1, theta=np.pi / 180, threshold=50, minLineLength=20, maxLineGap=5)
result_image = cv2.cvtColor(closed_image, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(result_image, (x1, y1), (x2, y2), (255, 255, 255), 1)  # 使用白色绘制线，颜色为 (255, 255, 255)

# 显示处理结果
cv2.imshow('Result', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
