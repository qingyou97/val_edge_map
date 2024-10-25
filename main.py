import cv2
import numpy as np

# 读取图片A和图片B
imageA = cv2.imread('imageA.jpg')
imageB = cv2.imread('imageB.jpg')

# 确保图片大小相同
if imageA.shape != imageB.shape:
    exit("图片A和图片B大小不同，无法处理。")

# 转换图片A成灰度图像
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)

# 定义白色点的阈值（假设为255）
threshold = 255

# 找到灰度图像中所有白色点的坐标
white_points = np.column_stack(np.where(grayA == threshold))

# 在图片B的相应位置涂成绿色
for point in white_points:
    imageB[point[0], point[1]] = [0, 255, 0]  # BGR格式的绿色

# 保存结果图片
cv2.imwrite('result_image.jpg', imageB)

# 显示结果图片
cv2.imshow('Result', imageB)
cv2.waitKey(0)
cv2.destroyAllWindows()
