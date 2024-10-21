import cv2
import numpy as np

# 读取黑白图像1
bw_img1 = cv2.imread('path/to/bw_image1.png', cv2.IMREAD_GRAYSCALE)
# 读取黑白图像2
bw_img2 = cv2.imread('path/to/bw_image2.png', cv2.IMREAD_GRAYSCALE)

# 找到图1的白色点的位置
coords1 = np.column_stack(np.where(bw_img1 == 255))
# 找到图2的白色点的位置
coords2 = np.column_stack(np.where(bw_img2 == 255))

# 创建一个新的与图1大小相同的彩色图像，并初始化为黑色 
height, width = bw_img1.shape
result_img = np.zeros((height, width, 3), dtype=np.uint8)

# 在新的图像上将图1中的白色点绘制为红色
for coord in coords1:
    cv2.circle(result_img, (coord[1], coord[0]), 1, (0, 0, 255), -1)

# 在新的图像上将图2中的白色点绘制为红色
for coord in coords2:
    cv2.circle(result_img, (coord[1], coord[0]), 1, (0, 0, 255), -1)

# 显示结果图像
cv2.imshow('Result Image', result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存结果图像
cv2.imwrite('path/to/result_image.png', result_img)
