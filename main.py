import cv2
import numpy as np

# 读取图像
image = cv2.imread('path_to_your_image.png', cv2.IMREAD_GRAYSCALE)

# 二值化图像
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# 反转图像颜色（因为白色是目标，黑色是背景）
binary_image = cv2.bitwise_not(binary_image)

# 进行形态学操作（闭操作）
kernel = np.ones((3, 3), np.uint8)
closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# 使用霍夫变换检测线条
lines = cv2.HoughLinesP(closed_image, rho=1, theta=np.pi / 180, threshold=50, minLineLength=20, maxLineGap=5)

# 创建一个新的黑色背景的图像
new_image = np.zeros_like(binary_image)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        # 计算线段的角度
        angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
        # 检查是否在水平和竖直范围内
        if abs(angle) <= 15 or abs(abs(angle) - 180) <= 15 or abs(abs(angle) - 90) <= 15:
            # 绘制白色线条到新图像上
            cv2.line(new_image, (x1, y1), (x2, y2), (255), 1)

# 显示处理结果
cv2.imshow('Result', new_image) 
cv2.waitKey(0)
cv2.destroyAllWindows()
