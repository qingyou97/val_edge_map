import cv2
import numpy as np

# 读取图像
image = cv2.imread('path_to_image', cv2.IMREAD_GRAYSCALE)

# 使用开闭运算进行处理
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# 阈值分割
_, binary_image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

# Laplace变换找到轮廓线
laplacian_kernel = np.array([[0, 1, 0], 
                             [1, -4, 1], 
                             [0, 1, 0]], dtype=float)
laplacian_output = cv2.filter2D(binary_image, cv2.CV_32F, laplacian_kernel)
laplacian_output = np.uint8(np.absolute(laplacian_output))

# 查找轮廓
contours, _ = cv2.findContours(laplacian_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 原图转换为BGR彩色图像
original_image = cv2.imread('path_to_image')
if original_image.ndim == 2:
    original_image = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)

# 提取合适的轮廓并拟合椭圆
for contour in contours:
    if len(contour) < 5:  # 拟合椭圆需要的点数最少为 5
        continue
    ellipse = cv2.fitEllipse(contour)
    color = (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))
    cv2.ellipse(original_image, ellipse, color, 2)

# 显示结果
cv2.imshow('Fitted Ellipses', original_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
