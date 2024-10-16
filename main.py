import cv2
import numpy as np

# 读取图像
image = cv2.imread('path_to_your_image.png', cv2.IMREAD_GRAYSCALE)

# 二值化图像
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

# 反转图像颜色（因为白色是目标，黑色是背景）
binary_image = cv2.bitwise_not(binary_image)

# 进行形态学操作（闭操作）
kernel = np.ones((3, 3), np.uint8)  # 窗口大小为3x3，进行闭运算来填充小孔
closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

# 使用霍夫变换检测线条
lines = cv2.HoughLinesP(closed_image, rho=1, theta=np.pi / 180, threshold=50, minLineLength=20, maxLineGap=5)

# 创建一个新的黑色图像
new_image = np.zeros_like(image)

# 角度统计
angle_count = {}

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        
        # 计算线的角度
        angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
        if angle < 0:
            angle += 360  # 将角度转为正值
        
        # 将角度四舍五入为整数
        angle = round(angle)
        
        # 过滤掉角度在311到316度之间的线段
        if 311 <= angle <= 316:
            continue
        
        # 记录每个角度有几条线
        if angle in angle_count:
            angle_count[angle] += 1
        else:
            angle_count[angle] = 1
        
        # 在新的黑色图像上绘制剩余的线段
        cv2.line(new_image, (x1, y1), (x2, y2), 255, 1)

# 打印角度统计
for angle, count in sorted(angle_count.items()):
    print(f"Angle: {angle} degrees, Count: {count}")

# 显示处理结果
cv2.imshow('Result', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
