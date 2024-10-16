import cv2
import numpy as np

# 读取图像
image = cv2.imread('path_to_your_image.png', cv2.IMREAD_GRAYSCALE)

# 二值化图像
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# 反转图像颜色（使背景为黑色，目标为白色）
binary_image = cv2.bitwise_not(binary_image)

# 进行形态学操作（闭操作）
kernel = np.ones((3, 3), np.uint8)
closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# 使用霍夫变换检测线条
lines = cv2.HoughLinesP(closed_image, rho=1, theta=np.pi / 180, threshold=50, minLineLength=20, maxLineGap=5)
result_image = np.zeros_like(closed_image)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        # 计算斜率
        angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
        angle = abs(angle)  # 取绝对值以处理负角度
        # 检查角度是否在允许的范围内
        if (angle <= 15) or (abs(angle - 90) <= 15):
            cv2.line(result_image, (x1, y1), (x2, y2), (255, 255, 255), 1)

# 反转图像颜色以符合原图的方案（黑色为背景，白色为线条）
result_image = cv2.bitwise_not(result_image)

# 显示处理结果
cv2.imshow('Result', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 可选：保存处理后的图像
cv2.imwrite('result_image.png', result_image)
