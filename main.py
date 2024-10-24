import cv2
import numpy as np

# 读取A图和B图
A_img = cv2.imread('A.png', cv2.IMREAD_GRAYSCALE)
B_img = cv2.imread('B.png')

# 确保B图为彩色图
if len(B_img.shape) == 2 or B_img.shape[2] == 1:
    B_img = cv2.cvtColor(B_img, cv2.COLOR_GRAY2BGR)

# 找到A图中白色点的坐标
white_points = np.argwhere(A_img == 255)  # 255表示白色点

# 在B图上画出红点
for point in white_points:
    cv2.circle(B_img, (point[1], point[0]), radius=1, color=(0, 0, 255), thickness=-1)

# 保存或显示B图
cv2.imwrite('B_with_red_dots.png', B_img)

# 如果要显示图像
cv2.imshow('B_with_red_dots', B_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
