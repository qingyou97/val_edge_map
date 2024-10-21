import cv2
import numpy as np

# 读取图像
image = cv2.imread('your_image_path.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (224, 224))

# 二值化
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 查找轮廓
contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 创建两个空白图像来绘制两个圆环
output_image1 = np.zeros_like(image)
output_image2 = np.zeros_like(image)

# 找到并绘制圆环
ellipses = []
for contour in contours:
    # 拟合椭圆轮廓，确保轮廓具有足够的点
    if len(contour) >= 5:
        ellipse = cv2.fitEllipse(contour)
        ellipses.append(ellipse)

# 确保我们找到了两个圆环
if len(ellipses) >= 2:
    # 按面积排序，确保第一个是外侧圆环，第二个是内侧圆环
    ellipses = sorted(ellipses, key=lambda e: e[1][0] * e[1][1], reverse=True)
    
    # 绘制外侧圆环到第一个图像
    cv2.ellipse(output_image1, ellipses[0], 255, 2)  # 用白色绘制
    
    # 绘制内侧圆环到第二个图像
    cv2.ellipse(output_image2, ellipses[1], 255, 2)  # 用白色绘制

# 显示图像
cv2.imshow('Outer Circle', output_image1)
cv2.imshow('Inner Circle', output_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
