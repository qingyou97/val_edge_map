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
if len(ellipses) >= 4:
    # 按面积排序，确保第一个和第二个是一个圆环的内外轮廓，第三个和第四个是另一个圆环的内外轮廓
    ellipses = sorted(ellipses, key=lambda e: e[1][0] * e[1][1], reverse=True)
    
    def make_circle(ellipse):
        center, axes, angle = ellipse
        max_radius = max(axes)
        return (center, (max_radius, max_radius), angle)
    
    # 调整为正圆
    ellipses[0] = make_circle(ellipses[0])
    ellipses[1] = make_circle(ellipses[1])
    ellipses[2] = make_circle(ellipses[2])
    ellipses[3] = make_circle(ellipses[3])
    
    # 绘制第一个圆环到第一个图像
    cv2.ellipse(output_image1, ellipses[0], 255, 2)  # 用白色绘制外轮廓
    cv2.ellipse(output_image1, ellipses[1], 255, 2)  # 用白色绘制内轮廓
    
    # 绘制第二个圆环到第二个图像
    cv2.ellipse(output_image2, ellipses[2], 255, 2)  # 用白色绘制外轮廓
    cv2.ellipse(output_image2, ellipses[3], 255, 2)  # 用白色绘制内轮廓

# 显示图像
cv2.imshow('Outer Circle', output_image1)
cv2.imshow('Inner Circle', output_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
