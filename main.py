import cv2
import numpy as np

# 读取图像
image = cv2.imread('your_image_path.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (224, 224))

# 二值化
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 使用霍夫圆变换检测圆
circles = cv2.HoughCircles(binary_image, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                           param1=50, param2=30, minRadius=10, maxRadius=100)

# 创建一个彩色图像来绘制红色轮廓
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# 如果检测到圆
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # 绘制外圆
        cv2.circle(output_image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        # 绘制内圆
        cv2.circle(output_image, (i[0], i[1]), i[2] - 5, (0, 0, 255), 2)

# 显示图像
cv2.imshow('Detected Circles', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
