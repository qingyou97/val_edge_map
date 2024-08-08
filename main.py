import cv2
import numpy as np

def calculate_mean_edge_thickness(image_path):
    # 读取图像
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
  
    # 检测轮廓
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # 用来存储所有边缘上的厚度值
    thicknesses = []

    # 循环遍历所有检测到的边缘轮廓
    for contour in contours:
        for i in range(len(contour)):
            # 当前点
            x1, y1 = contour[i][0]

            # 下一个点
            x2, y2 = contour[(i + 1) % len(contour)][0]

            # 计算欧几里得距离 (即 thickness)
            thickness = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            thicknesses.append(thickness)
    
    # 计算平均厚度
    mean_thickness = np.mean(thicknesses)
    return mean_thickness

# 更新图片文件路径
image_path = 'path_to_your_image.png'
mean_thickness = calculate_mean_edge_thickness(image_path)
print(f'The mean edge thickness is approximately {mean_thickness} pixels.')
