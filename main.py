import os.path

import cv2
import numpy as np

img_path = r'E:\TEED\training_data\1-Aero-engine-defect\gt'
save_path = r'E:\TEED\training_data\1-Aero-engine-defect\gt_new'
if not os.path.exists(save_path):
    os.makedirs(save_path)
img_list = os.listdir(img_path)
for img in img_list:
    img_new_path = os.path.join(img_path,img)

    # 读取图像
    image = cv2.imread(img_new_path, cv2.IMREAD_GRAYSCALE)

    # 反转图像颜色
    inverted_image = cv2.bitwise_not(image)

    # 保存反转后的图像
    cv2.imwrite(os.path.join(save_path,f'{img}'), inverted_image)
