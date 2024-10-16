import cv2
import numpy as np

# 读取图像
image = cv2.imread('path_to_your_image.png', cv2.IMREAD_GRAYSCALE)

# 二值化图像
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# 反转图像颜色（因为白色是目标，黑色是背景）
binary_image = cv2.bitwise_not(binary_image)

# 边缘检测
edges = cv2.Canny(binary_image, 50, 150, apertureSize=3)

# 使用霍夫变换检测线条
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 180, threshold=50, minLineLength=20, maxLineGap=5)

# 创建一个空白图像用于绘制结果
result_image = np.zeros_like(binary_image)

# 筛选线段
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        # 计算线段长度
        length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        # 计算线段中点
        mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
        # 检查线段中点是否在原图的白色区域
        if binary_image[mid_y, mid_x] == 255 and length > 10:  # 你可以调整长度阈值
            cv2.line(result_image, (x1, y1), (x2, y2), 255, 1)

# 保持背景为黑色，线段为白色
result_image = cv2.bitwise_not(result_image)

# 显示处理结果
cv2.imshow('Result', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 可选：保存处理后的图像
cv2.imwrite('result_image.png', result_image)
