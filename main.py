import cv2
import numpy as np

# 读取图像
image = cv2.imread('path_to_image', cv2.IMREAD_GRAYSCALE)

# 使用高斯模糊消除噪声
blurred = cv2.GaussianBlur(image, (9, 9), 2)

# 使用霍夫圆变换检测圆
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

# 确保有检测到的圆
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles:
        # 在输出图像中画圆和中心点
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

# 显示结果
cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
