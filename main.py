import cv2
import numpy as np

# 读取图像
image = cv2.imread('your_image_path.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (224, 224))

# 二值化
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 查找轮廓
contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 创建一个彩色图像来绘制红色轮廓
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# 找到并绘制圆环
circles_found = 0
for contour in contours:
    # 拟合椭圆轮廓，确保轮廓具有足够的点
    if len(contour) >= 5:
        ellipse = cv2.fitEllipse(contour)
        # 检查轮廓周长与圆拟合周长的近似程度
        perimeter = cv2.arcLength(contour, True)
        hull_perimeter = cv2.arcLength(cv2.convexHull(contour), True)
        perimeter_ratio = perimeter / hull_perimeter
        
        # 过滤出类圆周长轮廓的形式
        if 0.8 < perimeter_ratio < 1.2:
            cv2.ellipse(output_image, ellipse, (0, 0, 255), 2)  # 用红色绘制
            circles_found += 1
            
    # 结束循环，如已找到两个圆环
    if circles_found >= 2:
        break

# 显示图像
cv2.imshow('Detected Ellipses', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
