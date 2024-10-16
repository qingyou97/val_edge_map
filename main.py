import cv2
import numpy as np

# 读取图像（假设是单通道的黑白图像）
image = cv2.imread('path_to_your_image.png', cv2.IMREAD_GRAYSCALE)

# 二值化（如果不是二值图像的话）
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# 定义一个修补核（比如一个小的矩形核）
kernel = np.ones((3, 3), np.uint8)

# 膨胀然后腐蚀（即开运算，填补间隙）
processed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# 保存结果
cv2.imwrite('processed_image.png', processed_image)
