import cv2
import numpy as np

# 读取图像
image = cv2.imread('input_image.png', cv2.IMREAD_GRAYSCALE)

# 二值化图像（假设圆环是纯白色，即像素值为255）
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 找出轮廓
contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 创建彩色图像用于绘制
color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# 筛选出两个圆环的四条轮廓
circle_contours = []

for contour in contours:
    # 计算轮廓面积以及最小外接圆
    area = cv2.contourArea(contour)
    (x, y), radius = cv2.minEnclosingCircle(contour)
    
    # 定义一个面积合理范围以识别圆环
    if area > 500 and area < 5000:
        circle_contours.append(contour)

# 确保找到两个圆环，每个圆环有内外轮廓
assert len(circle_contours) == 4, "未找到两个圆环的完整轮廓"

# 按面积极简排序后绘制轮廓，这里假设：较大的两个为外轮廓，较小的两个为内轮廓
circle_contours = sorted(circle_contours, key=cv2.contourArea, reverse=True)
for i, contour in enumerate(circle_contours):
    cv2.drawContours(color_image, [contour], -1, (0, 0, 255), 2)  # 使用红色绘制

# 保存结果
cv2.imwrite('output_image.png', color_image)

# 显示结果
cv2.imshow('Detected Circles', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
