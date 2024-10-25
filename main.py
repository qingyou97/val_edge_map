# 在图像上绘制椭圆
for ellipse in ellipses:
    cv2.ellipse(image, ellipse, (255, 255, 255), 2)
