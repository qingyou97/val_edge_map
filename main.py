import cv2
import numpy as np

# 读取灰度图像
image = cv2.imread('edge_image.png', cv2.IMREAD_GRAYSCALE)

# 阈值处理，使灰度图成为二值图
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# 查找轮廓
contours, _ = cv2.findContours(binary_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 创建一个彩色图像用于绘制凸包
color_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)

# 列表存储厚度
thickness_list = []

for contour in contours:
    # 使用多边形拟合找到凸包
    hull = cv2.convexHull(contour)
    
    # 计算轮廓边界矩形
    x, y, w, h = cv2.boundingRect(hull)
    
    # 将宽高的平均值视为该轮廓的"厚度"
    average_thickness = (w + h) / 2.0
    thickness_list.append(average_thickness)
    
    # 使用随机颜色绘制凸包
    color = tuple(np.random.randint(0, 255, 3).tolist())
    cv2.drawContours(color_image, [hull], -1, color, 2)

# 输出平均厚度
if thickness_list:
    avg_thickness = sum(thickness_list) / len(thickness_list)
    print(f"边缘的平均厚度大约是 {avg_thickness} 个像素点")
else:
    print("未检测到边缘")

# 显示结果图像
cv2.imshow('Convex Hull', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
