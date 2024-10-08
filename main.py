import cv2
import numpy as np

def color_transform(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 定义深紫色和黄色的颜色范围
    deep_purple_lower = np.array([120, 0, 120])
    deep_purple_upper = np.array([180, 100, 180])

    yellow_lower = np.array([0, 220, 220])
    yellow_upper = np.array([200, 255, 255])

    # 创建掩码并应用颜色转换
    mask_purple = cv2.inRange(image, deep_purple_lower, deep_purple_upper)
    image[mask_purple > 0] = [0, 0, 0]

    mask_yellow = cv2.inRange(image, yellow_lower, yellow_upper)
    image[mask_yellow > 0] = [255, 255, 255]
    
    return image

# 使用示例
img_path = 'path_to_your_image.jpg'
transformed_image = color_transform(img_path)
cv2.imwrite('transformed_image.jpg', transformed_image)
